# A3: Eyes on the Road — validation practice leaderboard

Use the original CIFAR-10 training order: first 45,000 images for training and last 5,000 for validation. This leaderboard uses only the last 5,000 training images. Original test images are not included.

## Files

| File | Purpose |
|---|---|
| A3_Handout.pdf | Original assignment handout, unchanged |
| A3_Kaggle_starter.ipynb | Data split, preprocessing and prediction export; model implementation left to you |
| a3_submission.py | Validates and exports 5,000 integer predictions |
| validation_images.npz | uint8 RGB images, shape (5000,32,32,3), and original zero-based IDs; no labels |
| validation_ids.csv | Maps submission IDs to torchvision CIFAR-10 training indices |
| class_names.csv | Integer-to-class mapping, 0 through 9 |
| sample_submission.csv | Correct CSV format with dummy class-0 labels; not a baseline |

## Workflow

1. Download the official CIFAR-10 Python data, or use the torchvision loader in the starter.
2. Split before shuffling. Fit preprocessing and train only on the first 45,000 images.
3. Predict the last 5,000 images; use their original IDs 45000–49999.
4. Export `submission.csv` with exactly `id,label`, 5,000 rows, no dataframe index and labels 0–9.
5. Upload your model predictions and identify Part II or Part III in the submission description.
6. Keep all assignment code, analysis and final test results in your e3 submission.

Accuracy on all 5,000 validation images is correct predictions / 5,000. Frozen epoch-10 TA baselines: NumPy 1083/5000 = 21.66%; CNN 3621/5000 = 72.42%. The Kaggle host must configure the full validation set for the displayed score; a subset leaderboard is not directly comparable to these full-set numbers.

These are public CIFAR-10 validation images with recoverable labels, so this is a practice comparison rather than an independent hidden evaluation. Submit model outputs; do not train on validation examples or copy validation labels into submissions. Your code and report are needed to assess the assignment.

The handout controls the formal assignment requirements. The starter does not load or evaluate the official test set. After model selection, evaluate final models on that test set only as instructed in the handout.

Data: https://www.cs.toronto.edu/~kriz/cifar.html
Dataset loader: https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.CIFAR10.html
Credit: Alex Krizhevsky, Learning Multiple Layers of Features from Tiny Images, 2009.
