# Part I: Clustering and PCA

You will run each clustering method by hand on small examples and see why PCA must centre the data.

## (a) Why Centre

PCA computes the eigenvectors of the covariance matrix of the centred data.

$$
M =
\begin{bmatrix}
4 & 2 \\
2 & 4 \\
3 & 3 \\
3 & 3
\end{bmatrix}
$$

- Compute $M^\top M$ and its eigenvalues and unit eigenvectors by hand.
- Centre $M$ by subtracting the column means to obtain $\widetilde{M}$. Compute the covariance matrix $$C=\frac{1}{4}\widetilde{M}^{\top}\widetilde{M}$$, together with its eigenvalues and unit eigenvectors.
- The leading eigenvector changes after centring. Explain why, and state which direction PCA should report as the first principal component.

## (b) $k$-means by Hand

Seven stalls sit along a street at positions {1, 2, 3, 8, 9, 10, 25}. Run $k$-means with $k$ = 2 and squared Euclidean cost $\phi=\sum_x\min_c(x-c)^2$.

- Initialisation A: Centroids: {1, 25}. Initialisation B: Centroids: {1, 2}. For each, list the assignments, centroids, and cost $\phi$ at every iteration until convergence.
- Which initialisation reaches the lower final cost? Is the other result a global optimum? Explain why $k$-means can converge to different solutions.
- Farthest-first initialisation picks a first centroid and then repeatedly adds the point farthest from all chosen centroids. Starting from position 1, which centroids does it choose for $k$ = 2 and for $k$ = 3? Comment on how this strategy reacts to the stall at 25.

## (c) Hierarchical Clustering by Hand

Along another street, five food carts stand at positions {0, 2, 3, 7, 12}; the distance between carts at $x$ and $y$ is \| x−y \|

- Run agglomerative clustering with single link (MIN) and with complete link (MAX). For each, list the clusters merged at every step with the merge height, and draw the dendrogram.
- Cut each dendrogram into two clusters. Where does the cart at 7 end up in each case? Use this example to explain the chaining effect of single link.

## (d) DBSCAN by Hand

Return to the seven stalls in (b). Use $\varepsilon$ = 1 and $MinPts$ = 3, where the $\varepsilon$-neighbourhood of a point includes the point itself.

- Classify every stall as core, border, or noise point, and list the resulting clusters.
- Compare with the two $k$-means solutions in (b). Which method handles stall at 25 more sensibly, and why?

# Part II $k$-means from Scratch

The alliance has shortlisted four genres that could suit different zones of the market and now wants concrete playlists. You will prepare the data, implement $k$-means, study its sensitivity to initialisation, and test whether the moods it finds are real.

## 1. The Dataset.
We use the Spotify Tracks Dataset, which contains 114,000 tracks from 114 genres (1,000 tracks per genre), each described by metadata and audio features computed by Spotify.

- Features: the nine audio features danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, and tempo.
- Labels (not used for fitting): 'track_genre'. Keep 'track_name' and 'artists' for inspecting individual tracks.
- Loading: download 'dataset.csv' from the dataset page, or read it directly in Colab with 'pandas.read_csv'('hf://datasets/maharshipandya/spotify-tracks-dataset/dataset.csv')
- Track map: whenever a task asks you to show results on the track map, draw a scatter plot of the standardised acousticness (horizontal axis) against the standardised energy (vertical axis).

## 2. Setup.

For a set of centroids $C$, define the cost $\phi=\sum_x\min_{c\in C}\parallel x-c\parallel_2^2$ (the SSE). Let $\phi^{(0)}$ denote the cost under the initial centroids before any update, and $\phi^{(t)}$ the cost after the $t$-th iteration. For seeded initialisations, draw the first point as numpy.random.default_rng(seed).inntegers(n).

## 3. Tasks.

### (a) Data Preparation

- Keep the tracks whose track_genre is classical,, hip-hop, mandopop, or metal. Remove rows with a duplicated track_id, and then rows whose nine audio features exactly duplicate an earlier ow (the same recording released on several albums).
- Standardise each of the nine features to zero mean and unit variance using the population standard deviation (ddof=0). Call the result $Z\in\mathbb{R}^{n\times9}$. Use $Z$ in all later tasks.
- Report $n$ and the number of tracks per genre. Report the skewness of each feature, and explain in two sentences how strongly skewed features can affect distance based methods.
- Draw the track map coloured by genre. Which genre stands apart, and which genres overlap?
- Sanity check: you should keep $n$ = 3,408 tracks.

### (b) Implementation

Write a function kmeans(X, C0, max_iter=20) that returns the final assignments, the final centroids, and the cost history $\phi(0),\ldots,\phi$(max_iter).

- Assign each point to its nearest centroid, breaking ties by the smallest centroid index, and update each centroid as the mean of its assigned points. If a cluster becomes empty, keep its previous centroid.
- Vectorise the distance computation with numpy; explicit Python loops over data points are not allowed.
- Verify on $Z$ that your final SSE matches sklearn.cluster.KMeans started from the same initial centroids.

### (c) Initialisation Strategies

With $k$ = 4, compare three initialisations, each run with seeds 0, \ldots, 19:

- Random: $k$ distinct data points chosen uniformly at random.
- Farthest-first: a random first point, then repeatedly the point with the largest distance to its nearest chosen centroid.
- $k$-means++: a random first point, then each next point sampled with probability proportional to its squared distance to the nearest chosen centroid.

For each strategy, plot $\phi(t)$ against $t$ for seed `0`, and report the median $\phi(0) and the minimum, median, and maximum $\phi(20) over the 20 seeds. Which strategy starts best and which ends best?

- List the four tracks that farthest-first selects with seed 0 (name, artist, genre, and their most extreme features). Why are these tracks chosen, and what does this reveal about the sensitivity of farthest-first to outliers?
- Sanity check: the best $\phi(20)$ over all runs should be close to $1.58\times10^4$.

### (d) Choosing k and Cluster Validity

For $k = 2, \ldots, 8$, run $k$-means with $k$-means++ initialisation over seeds $0, \ldots, 9$ and keep the run with the lowest $\phi(20)$.

- Plot the best SSE (elbow plot), the mean silhouette coefficient, and the adjusted Rand index (ARI) against genre as functions of $k$.
- Which $k$ does each criterion favour? Explain why an internal criterion (silhouette) and an external one (ARI against genre) can disagree, and recommend a number of playlists to the alliance. Show the best $k$ = 4 clusters on the track map.
- Is the structure real? Build 10 null datasets by independently permuting each column of $Z$, which keeps every feature’s distribution but destroys the dependence between features. Run the same procedure on each and plot the mean null SSE alongside the real SSE for every $k$. What does the gap tell you?

# Part III Outlier Detection

Part II hinted that some tracks fit no mood: spoken recordings, live bootlegs, or pieces so quiet they are barely audible. You will now build outlier detectors from three families, check whether they agree, and evaluate them against anomalies whose identity you control.

## 1. 

## 2.
## (a)

## (b)

## (c)

## (d)
