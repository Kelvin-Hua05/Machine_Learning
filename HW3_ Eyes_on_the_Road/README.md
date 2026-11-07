You have joined the vision team of a Hsinchu startup that builds
low-cost roadside cameras. The team wants to know how much it gains by
moving from a hand-built neural network to a convolutional one. You will
derive backpropagation by hand, connect neural networks to SVM and
Bayesian learning, implement a neural network from scratch, and design a
CNN.

### Constraints

1.  **Part II:** NumPy only (no PyTorch, autograd or scikit-learn
    models). **Part III:** PyTorch, with no pretrained weights or
    external data.
2.  Hold out the last 5,000 training images as the validation set for
    all model selection, and evaluate on the test set only once. TA
    baseline accuracies on this split are announced on e3.
3.  All code must run on Google Colab (a free-tier GPU, when available,
    is sufficient). Keep notebook outputs and fix all random seeds to
    `0`.

### General Instructions

The assignment consists of three compulsory components:

1.  **Part I: Neurons by Hand** --- 20 points
2.  **Part II: A Neural Network from Scratch** --- 45 points
3.  **Part III: Convolutional Networks** --- 35 points

### Submission Guidelines

Submit your work through the e3 submission system, including the
following files:

1.  `A3_[ID].zip`: Your notebook(s) with all outputs and `nn_numpy.py`.
2.  `A3_[ID].pdf`: Your solutions to Part I, all requested tables and
    plots, your written analysis, and a viewable link to your Colab
    notebook.

### Late Submission Policy

  Penalty   Submission time
  --------- -------------------------------
  25%       From 15 minutes to 1 day late
  50%       From 1 day to 2 days late
  100%      More than 2 days late

------------------------------------------------------------------------

## Part I: Neurons by Hand \[20 marks\]

Before trusting a camera with thousands of images, every engineer traces
one input through a tiny network by hand. **Round all values to four
decimal places and show your working.**

### 1. The Toy Network

A 2--2--1 network has sigmoid hidden units, an identity output and the
loss

\[ J = `\frac{1}{2}`{=tex}(y-`\hat{y}`{=tex})\^2. \]

Its forward equations are

\[ h = `\sigma`{=tex}`\left`{=tex}(W^{(1)}x+b^{(1)}`\right`{=tex}),
`\qquad`{=tex} `\hat{y}`{=tex}=W^{(2)}h+b^{(2)}. \]

The parameters are

\[ W\^{(1)} =
```{=tex}
\begin{bmatrix}
0.1 & 0.3\\
0.2 & 0.4
\end{bmatrix}
```
, `\qquad `{=tex}b\^{(1)}=0, \]

\[ W\^{(2)} =
```{=tex}
\begin{bmatrix}
0.5 & -0.3
\end{bmatrix}
```
, `\qquad `{=tex}b\^{(2)}=0. \]

The input is (x=(1.0,0.5)\^`\top`{=tex}), and the target is (y=1).

### 2. Tasks

#### (a) Architecture (4 points)

A two-layer network has

\[ W^{(1)}`\in`{=tex}`\mathbb{R}`{=tex}^{K`\times`{=tex}(S+1)},
`\qquad`{=tex}
W^{(2)}`\in`{=tex}`\mathbb{R}`{=tex}^{I`\times`{=tex}(K+1)}, \]

with biases in column 0. Draw the network, including bias units, and
count its parameters for CIFAR-10 images ((S=3072), (K=100), (I=10)).

#### (b) Backpropagation (8 points)

For the toy network:

-   Compute the forward pass ((h,`\hat{y}`{=tex},J)).
-   Compute all gradients via

\[ `\delta`{=tex}\^{(2)}=`\hat{y}`{=tex}-y, `\qquad`{=tex}
`\delta`{=tex}\_i^{(1)}=`\delta`{=tex}^{(2)}W_i\^{(2)}`\sigma`{=tex}'(z_i).
\]

-   Perform one gradient descent step with (`\lambda=0.5`{=tex}).
-   Confirm that the loss decreases, and explain what goes wrong if all
    weights start at zero.

#### (c) Loss Functions (4 points)

For predicted probabilities (`\hat{y}`{=tex}=\[0.3,0.2,0.5\]) and label
(y=\[0,1,0\]):

-   Give the predicted class.
-   Compute the squared loss and the cross-entropy loss.

For scores (s=\[1.2,1.8,0.6\]) with true class 1:

-   Compute the multiclass hinge loss

\[ `\sum`{=tex}\_{j`\ne `{=tex}y}`\max`{=tex}(0,s_j-s_y+1) \]

and (`\partial `{=tex}L/`\partial `{=tex}s). - Relate it to the SVM
hinge loss.

#### (d) Connections (4 points)

With Gaussian noise (N(0,`\sigma`{=tex}\^2)) and prior
(w`\sim `{=tex}N(0,`\tau`{=tex}\^2I)):

-   Show that MAP estimation equals L2-regularized least squares and
    find (`\lambda`{=tex}).
-   Explain whether a network with five linear hidden layers and a
    softmax output is more expressive than logistic regression.

------------------------------------------------------------------------

## Part II: A Neural Network from Scratch \[45 marks\]

The team's first prototype uses no deep learning library, so that every
engineer understands what happens inside.

### 1. The Dataset: CIFAR-10

CIFAR-10 has 60,000 color images of size (32`\times32`{=tex}) in 10
classes, split into 50,000 training and 10,000 test images.

Download it with
[`torchvision.datasets.CIFAR10`](https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.CIFAR10.html),
convert it to NumPy, scale pixel values to (\[0,1\]), flatten each image
to 3072 values, and subtract the mean training image (computed on the
45,000 training images only).

Dataset reference:
[CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html).

### 2. The Module

Implement the following in `nn_numpy.py`, with each forward function
returning a cache for its backward function:

  ------------------------------------------------------------------------------
  Function                             Description
  ------------------------------------ -----------------------------------------
  `affine_forward/backward`            (Z=XW+b) and gradients for (X), (W), (b)

  `relu_forward/backward`,             Activations and their gradients
  `sigmoid_forward/backward`           

  `softmax_ce_loss(S, y)`,             Mean loss over the batch and
  `hinge_loss(S, y)`                   (`\partial `{=tex}J/`\partial `{=tex}S)

  `numerical_gradient(f, x, h=1e-5)`   Centered finite differences
  ------------------------------------------------------------------------------

### 3. Tasks

#### (a) Gradient Check (15 points)

Vectorize all functions (no loops over examples). On a small random
network in `float64`, report the relative error

\[ `\max`{=tex}\_i `\frac{|a_i-n_i|}{\max(10^{-8},|a_i|+|n_i|)}`{=tex}
\]

between analytic and numerical gradients for every layer and both
losses. Each should be below (10\^{-6}).

#### (b) Training (15 points)

Train a two-layer affine--ReLU--affine network with L2 regularization
and mini-batch SGD.

1.  First, overfit 50 images as a sanity check.
2.  Then tune the hidden size, learning rate, and regularization on the
    validation set.
3.  Report at least four configurations in one table.
4.  Plot the loss and accuracy curves of your best model.

For full marks, your model must beat the TA baseline:

-   100 hidden units
-   Weights drawn from (N(0,10\^{-4}))
-   Zero biases
-   No regularization
-   Softmax loss
-   Plain SGD with learning rate (10\^{-3})
-   Batch size 200
-   10 epochs

Finally, compare softmax and hinge loss as the output loss.

#### (c) Design Issues (15 points)

With five hidden layers, compare:

1.  **Weight initialization:** zero, small (std (=10\^{-2})), large (std
    (=1)) and He (std (=`\sqrt{2/\text{fan\_in}}`{=tex})) Gaussian
    initialization.
2.  **Activation functions:** sigmoid and ReLU under the same
    initialization. Plot the mean absolute gradient of each layer's
    weights at the start of training.
3.  **L2 regularization:** at least three L2 strengths.

Explain each result using the design issues from lecture, such as
vanishing gradients and overfitting.

### References

1.  A. Krizhevsky. *Learning Multiple Layers of Features from Tiny
    Images*. Technical Report, University of Toronto, 2009.
2.  [CIFAR-10 dataset](https://www.cs.toronto.edu/~kriz/cifar.html)
3.  [torchvision.datasets.CIFAR10
    documentation](https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.CIFAR10.html)

------------------------------------------------------------------------

## Part III: Convolutional Networks \[35 marks\]

A fully connected network ignores the structure of images. You will now
measure how much a CNN improves and test it on the test set once.

### (a) From Pixels to Filters (5 points)

Six (5`\times5`{=tex}`\times3`{=tex}) filters with stride 1 and no
padding are applied to a (32`\times32`{=tex}`\times3`{=tex}) image.

-   Give the output size and parameter count.
-   Compare them with a fully connected layer of the same output size.
-   Explain why weight sharing helps.

### (b) Your CNN (15 points)

Design and train your own CNN.

-   Report its layers (output shape and parameter count) in one table.
-   Justify your design choices.
-   Plot its loss and accuracy curves.

For full marks, it must beat the TA baseline CNN on the validation set:

``` text
conv3x3(32)
→ ReLU
→ maxpool2x2
→ conv3x3(64)
→ ReLU
→ maxpool2x2
→ linear(10)
```

Baseline settings:

-   Padding: 1
-   Optimizer: Adam
-   Learning rate: (10\^{-3})
-   Batch size: 64
-   Epochs: 10
-   No augmentation

### (c) Sensitivity Study (10 points)

Vary one configuration (e.g., learning rate, depth, dropout, batch
normalization or augmentation) over at least four values.

-   Plot validation accuracy against it.
-   Identify the best value.
-   Relate your findings to underfitting and overfitting.

### (d) Final Evaluation (5 points)

Evaluate your final model once on the test set.

-   It must beat the TA baseline CNN's test accuracy for full marks.
-   Compare it with Part II.
-   Briefly comment on whether your validation accuracy was a reliable
    estimate.
