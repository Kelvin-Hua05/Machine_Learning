1    k-means Algorithm
Consider eight data points: A1=(2,10), A2=(2,5), A3=(8,4), A4=(5,8), A5=(7,5), A6=(6,4), A7=(1,2),
A8=(4,9). Perform k-means clustering with k=2 to group the eight points into clusters C1 and C2 .
 (A) What are the member points of C1 and C2 after one iteration of k-means?

 (B) What are the member points of C1 and C2 after the second iteration of k-means?


2    Agglomerative Clustering Algorithm
Consider the distance matrix shown below. Use agglomerative algorithm to group the data with the following
agglomerate policy.

 (A) Perform agglomerative clustering with single-link and show its dendrogram.
 (B) Perform agglomerative clustering with complete-link and show its dendrogram.

 (C) Perform agglomerative clustering with average-link and show its dendrogram.


                                    A1    A2    A3    A4   A5    A6    A7    A8
                              A1     0    45    63    57   41    28    95     6
                              A2           0    55    49   35    11     5    25
                              A3                 0    11   23    54    47    65
                              A4                       0    2     7    26     5
                              A5                            0     5    21    35
                              A6                                  0    13    27
                              A7                                        0    53
                              A8                                              0



3    Density-based Clustering Algorithm
Consider the same distance matrix in Question 2. Perform DBSCAN with Epsilon=10 and MinPoints=2 to
cluster the eight points. Show the clustering process at each iteration, listing the clusters and their member
points. Please highlight the points that are classified as outliers if any.


4    Cluster Evaluation
Evaluate and compare the clusters discovered in (i) the agglomerative clustering task with a single-link policy
and (ii) DBSCAN using the internal measurement: Silhouette Coeﬀicient. You may need to determine an
appropriate cutting threshold for the agglomerative clustering task with a single-link policy.
 (A) What does it mean if the silhouette coeﬀicient is low/high at the individual level, cluster level, and
     overall clustering?

 (B) Which clustering algorithm delivers the resulting clustering with the lowest and the highest silhouette
     coeﬀicient?
 (C) Which clustering algorithm delivers balanced resulting clusters (i.e., each cluster has a similar number
     of points)?




                                                                                                             1

5    Anomaly Detection
 (A) Supervised outlier detection approaches build a classification model to classify unseen events. Discuss
     a major challenge that classification-based techniques must address. Explain how to resolve the specific
     challenge.
 (B) Proximity-based technique is one of the unsupervised learning approaches for point-based anomaly
     detection. Discuss a scenario where density-based outlier detection may fail. Explain how to resolve
     the specific case.


6    ROC
Given the table below, plot the ROC curve for 0, 0.2, 0.4, 0.6, 0.8, and 1 on the graph in the answer booklet.
Please explain whether you would choose to use Classifier 1 or Classifier 2 and why.

                            Class   P r(P |A) Classifier1   P r(P |A) for Classifier2
                            P               0.83                      0.92
                            N               0.78                      0.62
                            P               0.62                      0.52
                            N               0.48                      0.49
                            N               0.32                      0.38
                            N               0.22                      0.28



7    Evaluation Protocols
You will evaluate a fixed classifier on a binary classification dataset using four protocols: 2-fold CV, 10-fold
CV, Leave-One-Out CV (LOOCV), and a single 70%/30% train/validation split. Unless otherwise stated,
assume i.i.d. samples and use stratified splits to preserve class ratios.

 (A) What effect will this have on your results?
 (B) Which will give you the best representative value to the “unseen test set”?
 (C) Does it matter how large your original dataset is? Will you get a different answer for a very large or a
     tiny dataset?

 (D) Which will be the fastest in terms of computation?


8    Normalization
Suppose that we have some 8-bit grayscale image data encoded as a matrix:
                                                              
                                               0  0    255 120
                                             0 56      56  25 
                                      X=   40 200 186 15 
                                                               

                                              78 160 55      0

Use Min-Max scaling to normalize these data to the interval [0, 1] (represented using real numbers).


9    PCA
Given 3 data points in two-dimensional space, (1, 1), (2, 2), and (3, 3),
 (A) What is the first principal component?
 (B) If we want to project the original data points into a 1-d space by the main component you choose, what
     is the variance of the projected data?




                                                                                                              2

10    Decision Tree
We consider a toy dataset from an online retail e-commerce platform. The task is to predict whether an
order qualifies for free shipping (binary class {T, F }) based on three Boolean features: IsPrimeMember,
Over$35Cart, and IsMarketplaceSeller.

                     ID   IsPrimeMember       Over$35Cart     IsMarketplaceSeller   Class
                     1            1                 0                  0              T
                     2            1                 0                  1              F
                     3            0                 1                  0              F
                     4            1                 1                  1              F
                     5            1                 1                  0              T


 (A) What is the entropy of the root node? Show your working.
 (B) Draw the complete decision tree.
 (C) Are there feature(s) that are redundant?


11    Decision Tree
Consider the matrix below, which summarizes six online orders. Each column of M T is one order (sample),
and each row is a feature:
                               f1 = a normalized Order Value Index(110),
                             f2 = a normalized Items per Order Index(110), and
                               f3 = a normalized Account Tenure Index(110).
The label vector indicates whether an order is flagged for manual review (1) or not (0).
                                                                 
                                                3 5 8 1 6 4
                                        M =  2 7 6 3 4 5                                                 (1)
                                                5 7 9 2 8 6
where M T represents 6 sample points, each with three features f1 , f2 , and f3 .
The data labels are                                         T
                                            1 0 1 0 1 0                                                    (2)
We would like to build a decision tree of depth 2 by hand to classify the data.

 (A) What is the entropy of the root node? Show your working.

 (B) What is the rule for the first split? (Write it in a rule format, e.g., f1 > 2.) Show your working.
 (C) What is the rule for the second split? Show your working.
 (D) Should you have a third split? Explain your answer.


12    Linear Regression
Suppose that we have a regularized form of linear regression, where we wish to minimize the following loss:

                                         1 X
                                              N
                                  L(w) =       (yi − (wT xi + b))2 + γ∥w∥22
                                         N i=1

As we increase γ from 0 to infinity, describe how each of the following changes:
 (A) the model’s overfitting behaviour,

 (B) the values and magnitude of w,
 (C) the bias and variance of the model (Note: here bias is not referring to b).



                                                                                                            3

13    Naïve Bayes
 (A) Assume that the following likelihoods for each word are part of a positive or negative movie review and
     equal prior probabilities for each class. What class will Naïve Bayes assign to the sentence “I always
     like sci-fi movies.”?

                                                         pos        neg
                                                I        0.09       0.16
                                                always   0.07       0.06
                                                like     0.29       0.06
                                                sci-fi   0.04       0.15
                                                movies   0.08       0.11


 (B) Suppose that you are trying to solve a binary classification problem, and your data set has four attributes.
     Each attribute can take three possible values. If you modeled the full joint distribution of the attributes
     and the class label, how many parameters would you need?


14    Naïve Bayes
You are hiking a section of the Appalachian Trail in the United States. Along the way, you notice various
wild berries. Some are safe, while others are not. Using fictitious prior knowledge in the following table (Note:
The table is entirely fabricated and does not reflect real life; do not use it to identify wild berries), determine
which berries are poisonous.

            Example      IsRound     IsBlueOrPurple      IsClustered       HasCalyxCrown   Poisonous
            A                1              1                   0                1             -
            B                0              1                   1                0             +
            C                1              0                   1                0             +
            D                1              0                   0                0             -
            E                0              1                   0                1             -
            F                1              1                   1                0             +
            G                1              0                   0                1             -
            H                0              0                   1                0             +


 (A) Train your classifier on the labeled data (A-H). Compute and report the eight conditional probabilities
     of attributes given the class values (e.g., P (IsRound | ¬Poisonous)) and the class priors.
 (B) You have no labels for U and V. Using a naive Bayes classifier trained in (A), predict the labels for
     berries U and V. Try both without and with smoothing corrections.

            Example      IsRound     IsBlueOrPurple      IsClustered       HasCalyxCrown   Poisonous
            U                1              1                   0                0             ?
            V                1              0                   0                1             ?



15    k-Nearest Neighbors
Consider k-NN using Euclidean distance on the following dataset, where each point belongs to one of two
classes: red or blue.

 (A) Please draw the decision boundary for the following dataset using the 1-NN classification rule.
 (B) Would the decision boundary be different if another blue point was added to the data set at (6.1; 3.1)?
     Why or why not?




                                                                                                                 4

16    Decision Boundaries
Consider the following k-NN classification decision boundaries (a)-(d) as a result of different values of k and
distance metrics. The three classes of training data are represented by {red, green, yellow}, respectively.
Please match each decision boundary with the most possible k-NN settings below (A)-(D) and briefly provide
the justification for your pairing. (Note: Euclidean and Manhattan distance measures can be formally defined
as follows.)
  • Euclidean distance is defined as the square root of the sum of the squared differences between the
    coordinates of a pair of points x and y on a D-dimensional plane.
                                                       v
                                                       uD
                                                       uX
                                           dE (x, y) = t (xi − yi )2                               (3)
                                                              1


  • Manhattan distance is defined as the absolute differences between coordinates of pair of points x and y
    on D-dimensional plane.
                                                       XD
                                          dM (x, y) =     |(xi − yi )|                                  (4)
                                                          1




 (A) k = 1, Euclidean Distance.


                                                                                                             5

 (B) k = 15, Euclidean Distance.
 (C) k = 1, Manhattan Distance.
 (D) k = 15, Manhattan Distance.


17    Bias and Variance
As k in the k-NN model increases, what behavior would you expect for bias and variance? Please provide
your justification for your answer.


18    Linearly Separable Data: Hard-margin SVMs
Recall that the desirable decision boundary in linear hard-margin SVMs is the linear hyperplane that maxi-
mizes the distance/margin from its closest points. Please complete the following questions with your reasons
provided.
                                           2
                               max
                                w,b     ||w||22
                                        s.t. (w · xi + b)yi ≥ 1       ∀i = 1, . . . , n.

 (A) True or False? The linear hyperplane is defined by support vectors.
 (B) True or False? Moving points other than support vectors a little do not affect the decision boundary.

 (C) True or False? We only need to store the support vectors to predict labels for new points.
 (D) Given the following training set for two-class classification in one-dimension space, what are the values
     of w and b by a hard-margin SVM?


                                                point      label
                                                x1 =3      y1 =1
                                                x2 =1      y2 =1
                                                x3 =-1     y3 =-1



19    Non-Linearly Separable Data: Soft-margin SVMs
Recall that soft-margin SVMs allow the possibility of errors in classification. This is realized by relaxing the
optimization constraints with the introduction of slack variables ξi ≥> 0 ∀i = 1, ..., n. The soft-margin SVM
in its primal form is formulated as follows with ξi ≥ 0 for all i:

                                        1             Xn
                               min        ||w||22 + C     ξi
                               w,b,ξ    2             i=1
                                        s.t. ξi ≥ 0    ∀i = 1, . . . , n
                                        (w · xi + b)yi ≥ (1 − ξi )     ∀i = 1, . . . , n.

Which of the following are true of soft-margin SVMs? Please provide your justification for your answer.
 (A) Increasing the hyperparameter C tends to decrease the training error.
 (B) Increasing the hyperparameter C tends to decrease the margin.

 (C) The hard-margin SVM is a special case of the soft-margin with the hyperparameter C set to zero.
 (D) Increasing the hyperparameter C tends to decrease the sensitivity to outliers.




                                                                                                              6

20    Decision Boundaries
Consider the following four SVM decision boundaries (a)-(d) as a result of different kernels and/or slack
penalties. The two classes of training data with labels yi ∈ {−1, 1} are represented by triangles and squares,
respectively. The support vectors are depicted as solid triangle and squares. Please match each decision
boundary with the most possible optimization setting below (A)-(D) and briefly provide the justification for
your pairing.
 (A) A soft-margin linear SVM with C = 10−1 .
 (B) A soft-margin linear SVM with C = 102 .
                                                                             
 (C) A hard-margin kernel SVM with K(u, v) = exp −10−1 ∥u − v∥2
                                                               
 (D) A hard-margin kernel SVM with K(u, v) = exp −102 ∥u − v∥2


21    Kernelization
Recall that in hard-margin primal SVM, we have the following kernelized SVM in its dual form with the
product of xi · xj replaced by k(xi , xj ), where k(., .) can be any kernel function:
                                                                                  
                                       1X    n Xn                            X
                                                                              n    
                                max −               αi αj yi yj k(xi , xj ) +   αi
                                 α  2                                             
                                               i=1 j=1                      i=1

                                       X
                                       n
                                s.t.         αi yi = 0, ∀i = 1, 2, ..., n
                                       i=1
                                       αi ≥ 0, ∀i = 1, 2, ..., n


 (A) Given the raw features vectors xi and xj in a 2-dimensional plane, do you think that k(xi , xj ) =
     x2i1 x2j1 + x2i2 x2j2 is a valid kernel function? Why and why not?
                                                                                                               
                                                                                                   −∥xi −xj ∥22
 (B) Suppose we train an RBF kernelized SVM with kernel function defined as k(xi , xj ) = exp         σ 2

     for a classification problem. We find that the training accuracy is 0.99 but the testing accuracy is only
     0.61. What measures on the kernel width σ would you suggest to improve the testing accuracy?


22    Connection to Shallow Machine Learning
Consider two multi-class classifiers, C1 and C2 . C1 is a multi-layer neural network with five hidden layers.
The linear activation function is chosen for its hidden units across five hidden layers and the linear activation
for its last layer. C2 is a multi-class logistic regression classifier.


                                                                                                               7

 (A) Please draw neural network architectures for both C1 and C2 .




 (B) Are both of them capable of approximating the same set of functions? Please briefly provide your
     reasons.



23     Feed Forward and Backpropagation
Given a two-layer neural network, let S be the number of input features, K be the number of hidden units,
and I be the number of outputs. Suppose we have parameter matrices W (1) in the first layer and W (2) in
the second layer. The shapes of W (1) and W (2) are K × (S + 1) and I × (K + 1), respectively.
                                             (1)       (1)          (1)
                                                                         
                                              W10 W11 · · · W1S
                                             (1)       (1)          (1) 
                                            W20 W21 · · · W2S 
                                       (1)
                                    W = .                       .. 
                                                      ..     ..          
                                             ..       .        .  . 
                                                (1)     (1)         (1)
                                              WK0 WK1 · · · WKS
                                             (2)        (2)         (2)
                                                                         
                                              W10 W11 · · · W1K
                                             (2)        (2)         (2) 
                                            W20 W21 · · · W2K 
                                       (2)
                                    W = .                        .. 
                                                       ..    ..          
                                             ..        .       .   . 
                                                (2)      (2)         (2)
                                              WI0 WI1 · · · WIK

23.1   Network Details
Recall the gradient computation for a multi-layer neural network in weeks 10-11; complete the following
backward pass on the neural network.
 (A) By examining the shapes of the parameter matrices, please draw the neural network diagram.




                                                                                                       8

 (B) How many neurons do we have in the first hidden layer of the neural network without the bias neuron
     included?


 (C) How many output neurons does our neural network have?



24    Backward Propagation
Let y represent our true output in the form of a one-hot vector, and ŷ represent the predicted output of the
network. Suppose our loss function J(ŷ, y) is defined as follows:
                                                            1         2
                                               J(ŷ, y) =     ∥y − ŷ∥ .                                  (5)
                                                            2
Complete the following questions in order to derive the matrix and vector forms for the backpropagation
algorithm.
 (A) Let the partial derivatives for W (1) in the first layer be ∂J/∂W(1) . What is the shape of ∂J/∂W(1) ?
 (B) Let the partial derivatives for W (2) in the first layer be ∂J/∂W(2) . What is the shape of ∂J/∂W(2) ?
                                                               (1)         (1)
 (C) What are the partial derivatives for parameters Wij (∂J /∂Wij ) in terms of ŷ and y?
                                                               (2)         (2)
 (D) What are the partial derivatives for parameters Wjk (∂J /∂Wjk ) in terms of ŷ and y?


25    NN Prediction
Recall that for prediction, the model estimates one probability per class for each instance. We typically use
the argmax of the output layer. Given a new instance x, let the predicted outputs for x be ŷ and the true
class in one-hot vector form for x be y. Suppose the values of ŷ and y are as follows, respectively:
  • ŷ=[0.3,0.2,0.5] with yˆ1 =0.3, yˆ2 =0.2, yˆ3 =0.5.
  • y=[0,1,0] with y1 =0, y2 =1, and y3 =0.

Which class would the model predict for the new instance x? What is the estimated loss in this example
according to Eq. (5)?



26    GNN and CNN Analogy
Graph Neural Networks (GNNs) can be understood through the lens of message passing. Recall the materials
and draw an analogy between CNNs operating on image grids and GNNs operating on graphs. Please briefly
explain your answer to the following questions.

 (A) How is the message passing mechanism in GNNs analogous to convolution operations in CNNs (consider
     what is being aggregated and from where)?


 (B) What fundamental property of graphs makes GNNs more flexible but also more challenging than CNNs?



27    GNN Variants
Recall three main GNN variants introduced in our lecture week 13: Graph Convolutional Networks (GCNs),
Graph Attention Networks (GATs), and Neural Message Passing with edge embeddings. Each has differ-
ent capabilities and computational characteristics. Compare GCNs and Neural Message Passing with edge
embeddings for the following questions.

 (A) Identifying ONE key advantage that Neural Message Passing has over GCNs.
 (B) Explaining ONE significant disadvantage of Neural Message Passing and why this matters in practice.


                                                                                                           9

28    AdaBoost II
The figure below shows two binary SVM classifiers h1 , h2 in a 2D space. These classifiers have been trained
and will be used as weak learners in the AdaBoost algorithm. Initially, each training example is assigned an
equal weight. In each iteration, AdaBoost selects the weak learner with the minimum weighted classification
error, and computes its corresponding importance weight αt is using the standard AdaBoost formula. The
distribution wt (i) over the training examples {(x(i) , y (i) )}ni=1 is updated at every step according to whether
each example is correctly or incorrectly classified. Use the information below to answer the following questions.


                                              (a)
                                       h1
                                                                         h2

                                                                              (b)

                                              (c)


                                            +
                                                    −              (d)




 (A) Using only the initial weights (i.e., uniform over all training examples), which of the regions among
     (a) to (d) would be classified as +1 by the AdaBoost classifier after the first round, if the selected
     weak learner is h1 . (Hint: Use the decision boundary of h1 and assume the AdaBoost classifier is just
     sign(α1 h1 (x(i) )) after the first round.)
 (B) Suppose that after Round 1, h1 is chosen, and it correctly classifies the point in region (c), but misclas-
     sifies the point in region (d). Describe qualitatively what happens to the weights w2 (c) and w2 (d) in
     the updated distribution.
 (C) In Round 2, based on the updated distribution w2 , suppose h2 is selected as the next weak learner. If
     h2 misclassifies region (c) but correctly classifies region (d), describe the change in weights w3 (c) and
     w3 (d) after the second update.


29    Random Forest
Consider random forest, which of the following statement is True? Select All that apply.

 (A) It is generally better for the trees to be highly correlated, as this reduces the variance of the ensemble.
 (B) The number of trees in the forest is a hyperparameter that can be tuned.
 (C) The number of training examples used to train each individual tree is a hyperparameter that can be
     tuned in a random forest.

 (D) The size of the feature subset considered at each split is a hyperparameter that can be tuned in a
     random forest.
 (E) The specific features selected for splits in each tree is a hyperparameter that can be tuned in a random
     forest.




                                                                                                               10
```

## Original Figures

The following page images preserve the diagrams and plotted figures included in the original worksheet.

### Page 5 — Question 15 data points and Question 16 decision-boundary diagrams

![Page 5 figures](readme_assets/page-05.png)

### Page 7 — Question 20 SVM decision-boundary diagrams

![Page 7 figures](readme_assets/page-07.png)

### Page 8 — Question 22 neural-network architecture diagrams

![Page 8 figures](readme_assets/page-08.png)

### Page 10 — Question 28 AdaBoost diagram

![Page 10 figures](readme_assets/page-10.png)

