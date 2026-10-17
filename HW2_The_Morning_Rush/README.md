# Constraints

1. Use **linear models only**: `LinearRegression`, `Ridge`, `Lasso`, and `SGDRegressor` from `scikit-learn`, optionally with `PolynomialFeatures`. Tree ensembles and neural networks are **not** allowed.
2. Fit every scaler and encoder on training data only, inside a `sklearn.pipeline.Pipeline`.
3. All code must run on Google Colab. Start from the provided guided notebook `A2_starter.ipynb`, do not clear its outputs before submitting, and fix all random seeds to `0`.

# Part I: Least Squares

Before dispatching a fleet of trucks, every operator practises on a single station. In this part you will fit, regularize, and rescale a tiny regression model by hand.

## 1. Notation

Let $X \in \mathbb{R}^{N \times d}$ be the design matrix and $y \in \mathbb{R}^N$ the targets. Ordinary least squares (OLS) and ridge regression minimize, respectively,

$$
J_{\text{OLS}}(w) = \frac{1}{2}\lVert y - Xw \rVert_2^2, \qquad
J_{\text{ridge}}(w) = \frac{1}{2}\lVert y - Xw \rVert_2^2 + \frac{\lambda}{2}\lVert w \rVert_2^2, \quad \lambda > 0.
$$

For a single feature $x$ with intercept $w_0$ and slope $w_1$, let $S_{xx} = \sum_i \left(x^{(i)} - \bar{x}\right)^2, \qquad$ and $S_{xy} = \sum_i \left(x^{(i)} - \bar{x}\right)\left(y^{(i)} - \bar{y}\right).$ The intercept is **not** penalized, so the ridge slope is $w_1 = \frac{S_{xy}}{S_{xx} + \lambda}.$

## 2. The Toy Dataset

## 3. Tasks


# Part II: Feature Engineering and Scaling

The operations centre has shared one month of real rental logs. You will turn raw timestamps and weather readings into features that capture how Taipei commutes.

## 1. The Dataset: Taipei YouBike 2.0 Hourly Demand (Jan-Jun 2026)

## 2. Tasks

### (a)

### (b) 

### (c)

# Part II: Learning Curves and Forecasting

A model that looks good on one split may still be starved of data or drowning in parameters. In this part, you will diagnose your models, fix them, and face the final week of March.

## 1. Setup

## 2. Tasks

### (a)

### (b) 

### (c)
