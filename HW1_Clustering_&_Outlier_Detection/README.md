# Part I

You will run each clustering method by hand on small examples and see why PCA must centre the data.

## (a)

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

## (b)

Seven stalls sit along a street at positions {1, 2, 3, 8, 9, 10, 25}. Run $k$-means with $k$ = 2 and squared Euclidean cost $\phi=\sum_x\min_c(x-c)^2$.

- Initialisation A: Centroids: {1, 25}. Initialisation B: Centroids: {1, 2}. For each, list the assignments, centroids, and cost $\phi$ at every iteration until convergence.
- Which initialisation reaches the lower final cost? Is the other result a global optimum? Explain why $k$-means can converge to different solutions.
- Farthest-first initialisation picks a first centroid and then repeatedly adds the point farthest from all chosen centroids. Starting from position 1, which centroids does it choose for $k$ = 2 and for $k$ = 3? Comment on how this strategy reacts to the stall at 25.

## (c)

Along another street, five food carts stand at positions {0, 2, 3, 7, 12}; the distance between carts at $x$ and $y$ is \| x−y \|

- Run agglomerative clustering with single link (MIN) and with complete link (MAX). For each, list the clusters merged at every step with the merge height, and draw the dendrogram.
- Cut each dendrogram into two clusters. Where does the cart at 7 end up in each case? Use this example to explain the chaining effect of single link.

## (d)

Return to the seven stalls in (b). Use $\varepsilon$ = 1 and $MinPts$ = 3, where the $\varepsilon$-neighbourhood of a point includes the point itself.

- Classify every stall as core, border, or noise point, and list the resulting clusters.
- Compare with the two $k$-means solutions in (b). Which method handles stall at 25 more sensibly, and why?

# Part II

The alliance has shortlisted four genres that could suit different zones of the market and now wants concrete playlists. You will prepare the data, implement $k$-means, study its sensitivity to initialisation, and test whether the moods it finds are real.

## 1 The Dataset.
We use the Spotify Tracks Dataset, which contains 114,000 tracks from 114 genres (1,000 tracks per genre), each described by metadata and audio features computed by Spotify.

- Features: the nine audio features danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, and tempo.
- Labels (not used for fitting): 'track_genre'. Keep 'track_name' and 'artists' for inspecting individual tracks.
- Loading: download 'dataset.csv' from the dataset page, or read it directly in Colab with 'pandas.read_csv'('hf://datasets/maharshipandya/spotify-tracks-dataset/dataset.csv')
- Track map: whenever a task asks you to show results on the track map, draw a scatter plot of the standardised acousticness (horizontal axis) against the standardised energy (vertical axis).

## 2 Setup.

For a set of centroids $C$, define the cost $\phi=\sum_x\min_{c\in C}\|x-c\|_2^2$

### (a)

### (b)

### (c)

### (d)

# Part III

## (a)

## (b)

## (c)

## (d)
