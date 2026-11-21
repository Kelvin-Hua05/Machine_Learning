"""NumPy-only neural-network building blocks for HW3 Part II (no autograd, no sklearn)."""
import numpy as np

# ---------------------------------------------------------------- layers
def affine_forward(X, W, b):
    Z = X @ W + b
    return Z, (X, W)

def affine_backward(dZ, cache):
    X, W = cache
    return dZ @ W.T, X.T @ dZ, dZ.sum(axis=0)          # dX, dW, db

def relu_forward(X):
    return np.maximum(0, X), X

def relu_backward(dA, cache):
    return dA * (cache > 0)

def sigmoid_forward(X):
    A = 1.0 / (1.0 + np.exp(-X))
    return A, A

def sigmoid_backward(dA, cache):
    return dA * cache * (1.0 - cache)

# ---------------------------------------------------------------- losses
def softmax_ce_loss(S, y):
    """Mean softmax cross-entropy over the batch and dJ/dS."""
    N = S.shape[0]
    Z = S - S.max(axis=1, keepdims=True)                # numerical stability
    logsum = np.log(np.exp(Z).sum(axis=1, keepdims=True))
    logp = Z - logsum
    loss = -logp[np.arange(N), y].mean()
    dS = np.exp(logp)
    dS[np.arange(N), y] -= 1.0
    return loss, dS / N

def hinge_loss(S, y, delta=1.0):
    """Mean multiclass hinge loss sum_{j!=y} max(0, s_j - s_y + delta) and dJ/dS."""
    N = S.shape[0]
    idx = np.arange(N)
    margins = np.maximum(0.0, S - S[idx, y][:, None] + delta)
    margins[idx, y] = 0.0
    loss = margins.sum() / N
    dS = (margins > 0).astype(S.dtype)
    dS[idx, y] = -dS.sum(axis=1)
    return loss, dS / N

# ---------------------------------------------------------------- gradient check
def numerical_gradient(f, x, h=1e-5):
    """Centered finite differences of scalar function f w.r.t. array x (x is perturbed in place, then restored)."""
    grad = np.zeros_like(x)
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        i = it.multi_index
        old = x[i]
        x[i] = old + h; fp = f()
        x[i] = old - h; fm = f()
        x[i] = old
        grad[i] = (fp - fm) / (2 * h)
        it.iternext()
    return grad

def rel_error(a, n):
    return np.max(np.abs(a - n) / np.maximum(1e-8, np.abs(a) + np.abs(n)))

# ---------------------------------------------------------------- fully-connected net
class FCNet:
    """affine - act - affine - act ... - affine, with L2 regularisation  J = data + 0.5*reg*sum(W^2)."""
    def __init__(self, dims, act='relu', init='he', std=1e-2, reg=0.0, loss='softmax',
                 dtype=np.float32, seed=0):
        rng = np.random.RandomState(seed)
        self.act, self.reg, self.loss_name, self.L = act, reg, loss, len(dims) - 1
        self.p = {}
        for i in range(self.L):
            fi, fo = dims[i], dims[i + 1]
            if init == 'zero':   w = np.zeros((fi, fo))
            elif init == 'he':   w = rng.randn(fi, fo) * np.sqrt(2.0 / fi)
            else:                w = rng.randn(fi, fo) * std      # 'small' / 'large' / baseline: pass std
            self.p[f'W{i+1}'] = w.astype(dtype)
            self.p[f'b{i+1}'] = np.zeros(fo, dtype=dtype)
        self._f = relu_forward if act == 'relu' else sigmoid_forward
        self._b = relu_backward if act == 'relu' else sigmoid_backward

    def loss(self, X, y=None):
        caches, A = [], X
        for i in range(1, self.L + 1):
            A, c = affine_forward(A, self.p[f'W{i}'], self.p[f'b{i}']); caches.append(('a', c))
            if i < self.L:
                A, c = self._f(A); caches.append(('n', c))
        if y is None:
            return A
        lf = softmax_ce_loss if self.loss_name == 'softmax' else hinge_loss
        data_loss, dS = lf(A, y)
        reg_loss = 0.5 * self.reg * sum((self.p[f'W{i}'] ** 2).sum() for i in range(1, self.L + 1))
        grads, d, i = {}, dS, self.L
        for kind, c in reversed(caches):
            if kind == 'a':
                d, dW, db = affine_backward(d, c)
                grads[f'W{i}'] = dW + self.reg * self.p[f'W{i}']
                grads[f'b{i}'] = db
                i -= 1
            else:
                d = self._b(d, c)
        return data_loss + reg_loss, grads

    def predict(self, X, bs=1000):
        return np.concatenate([self.loss(X[i:i+bs]).argmax(1) for i in range(0, len(X), bs)])

def train(net, Xtr, ytr, Xva, yva, lr=1e-3, epochs=10, bs=200, lr_decay=1.0, momentum=0.0, seed=0, verbose=True):
    """Mini-batch SGD (optional momentum). Returns history dict. Data loss + reg is logged per epoch."""
    rng = np.random.RandomState(seed)
    vel = {k: np.zeros_like(v) for k, v in net.p.items()}
    hist = dict(loss=[], train_acc=[], val_acc=[])
    N = len(Xtr)
    for ep in range(epochs):
        perm, tot = rng.permutation(N), 0.0
        for i in range(0, N, bs):
            idx = perm[i:i+bs]
            l, g = net.loss(Xtr[idx], ytr[idx])
            tot += float(l) * len(idx)
            for k in net.p:
                vel[k] = momentum * vel[k] - lr * g[k]
                net.p[k] += vel[k]
        lr *= lr_decay
        hist['loss'].append(tot / N)
        hist['train_acc'].append(float((net.predict(Xtr[:5000]) == ytr[:5000]).mean()))
        hist['val_acc'].append(float((net.predict(Xva) == yva).mean()))
        if verbose:
            print(f"epoch {ep+1:3d} loss {hist['loss'][-1]:.4f} train {hist['train_acc'][-1]:.4f} val {hist['val_acc'][-1]:.4f}")
    return hist

def layer_grad_magnitudes(net, X, y):
    """Mean |dJ/dW| of every layer at the current weights (used for the vanishing-gradient plot)."""
    _, g = net.loss(X, y)
    return [float(np.abs(g[f'W{i}']).mean()) for i in range(1, net.L + 1)]

# ---------------------------------------------------------------- self test
def run_gradcheck(verbose=True):
    """Gradient check in float64 on a small random network; returns {name: relative error}."""
    rng = np.random.RandomState(0)
    N, D, H, C = 12, 5, 4, 4
    X = rng.randn(N, D); y = rng.randint(0, C, N)
    Wt, bt = rng.randn(D, H), rng.randn(H)
    G = rng.randn(N, H)                                      # upstream gradient for the layer checks
    res = {}
    # affine
    Z, c = affine_forward(X, Wt, bt); dX, dW, db = affine_backward(G, c)
    f = lambda: (affine_forward(X, Wt, bt)[0] * G).sum()
    res['affine dX'] = rel_error(dX, numerical_gradient(f, X))
    res['affine dW'] = rel_error(dW, numerical_gradient(f, Wt))
    res['affine db'] = rel_error(db, numerical_gradient(f, bt))
    # activations
    Xa = rng.randn(N, H)
    for name, fw, bw in [('relu', relu_forward, relu_backward), ('sigmoid', sigmoid_forward, sigmoid_backward)]:
        _, c = fw(Xa); da = bw(G, c)
        res[f'{name} dX'] = rel_error(da, numerical_gradient(lambda: (fw(Xa)[0] * G).sum(), Xa))
    # losses
    S = rng.randn(N, C)
    for name, lf in [('softmax_ce', softmax_ce_loss), ('hinge', hinge_loss)]:
        _, dS = lf(S, y)
        res[f'{name} dS'] = rel_error(dS, numerical_gradient(lambda: lf(S, y)[0], S))
    # whole network, both activations / losses
    for act in ['relu', 'sigmoid']:
        for ls in ['softmax', 'hinge']:
            net = FCNet([D, 7, 6, C], act=act, init='he', reg=0.1, loss=ls, dtype=np.float64)
            for k in net.p: net.p[k] += 0.1 * rng.randn(*net.p[k].shape)
            _, g = net.loss(X, y)
            for k in net.p:
                n = numerical_gradient(lambda: net.loss(X, y)[0], net.p[k])
                res[f'net[{act},{ls}] {k}'] = rel_error(g[k], n)
    if verbose:
        for k, v in res.items():
            print(f'{k:28s} {v:.2e}  {"OK" if v < 1e-6 else "FAIL"}')
        print('ALL < 1e-6:', all(v < 1e-6 for v in res.values()))
    return res

if __name__ == '__main__':
    run_gradcheck()
