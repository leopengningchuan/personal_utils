# Modeling Related
A curated knowledge base of modeling concepts, processes, and analytical foundations

## Table of Contents
- [Project Background](#project-background)
- [Project Goal](#project-goal)
- [Models](#models)
    - [Linear Regression](#linear-regression)
    - [Logistic Regression](#logistic-regression)
    - [Regularization ](#regularization)
    - [Linear Discriminant Analysis](#linear-discriminant-analysis)
    - [Support Vector Machine](#support-vector-machine)
    - [K-Nearest Neighbors](#k-nearest-neighbors)
    - [Decision Tree](#decision-tree)
    - [Random Forest](#random-forest)
    - [K-Means Clustering](#k-means-clustering)
    - [Hierarchical Clustering](#hierarchical-clustering)

## Project Background
This document serves as a personal knowledge base for concepts, terminology, and analytical frameworks related to analytical models and their applications in decision-making and operational analysis.

## Project Goal
The goal of this document is to provide a centralized and structured reference for core model-related knowledge, enabling clearer understanding, consistent usage of modeling terminology, and more effective analysis and application of models in practice.

## Models
### Linear Regression
*Definition*:   
Linear regression is a regression model that assumes a linear relationship between the independent variables and the single dependent variable.

$$y_i = \beta_0 + \beta_1 x_{i1} + \dots + \beta_p x_{ip} + \varepsilon_i$$

*Assumptions*: 
- There is a linear relationship between the dependent variables and the independent variables, meaning the model you are creating actually fits the data;
- The residuals errors of the data are normally distributed and independent from each other;
- There is minimal multicollinearity between independent variables;
- Homoscedasticity: variance of error terms is the same for all values of x.

*Drawbacks*:
- Strong assumptions that may not be true in application;
- Cannot be used in discrete or binary outcome;
- Cannot vary the model flexibility;
- Very non robust.

*RMSE, RSS, R2 & Adj R2*:   
Linear Regression Solution: Minimize residual sum of squares (RSS), $R^2 = 1-\frac{RSS}{TSS}$
Total sum of squares (TSS) = Explained sum of squares (ESS) + Residual sum of squares (RSS)

RMSE, Root Mean Square Error, is the standard deviation of the residuals. Residuals are a measure of how far from the regression line data points are; RMSE is a measure of how spread out these residuals are.

$$RMSE = \sqrt{\frac{RSS}{n}} $$

$R^2$ is a statistical measure that represents the proportion of the variance for a dependent variable that's explained by the independent variables in a regression model. R2 can have a negative value when the model selected does not follow the trend of the data.

$R^2_{\text{Adj}}$ is a modified version of R2 which takes n (number of observations) and k (number of independent variables) into account. It can be used to compare models that have a different number of variables. $R^2_{\text{Adj}}$ is always lower than $R^2$.

$$R^2_{\text{Adj}} = 1 - (1 - R^2)\frac{n - 1}{n - k - 1}$$

---

### Logistic Regression
*Definition*:   
Logistic Regression is a classification model which uses the logit model to predict the binary outcome of dependent variable from a linear combination of independent variables.

$$P(Y=1 \mid X=x) = \frac{e^{\beta_0 + \beta_1 x}}{1 + e^{\beta_0 + \beta_1 x}}$$
or
$$\log \frac{P(Y=1 \mid X=x)}{P(Y=0 \mid X=x)} = \beta_0 + \beta_1 x$$

*Maximum likelihood approach*:   
The logit of the estimated probability response is a linear function of the predictor parameters.

$$\text{Log-likelihood: } \ell(\boldsymbol{\beta}) = \sum_{i=1}^n \Big[ y_i \log p_i + (1 - y_i)\log(1 - p_i) \Big], \quad p_i = \sigma(\mathbf{x}_i^\top \boldsymbol{\beta}) = \frac{1}{1 + e^{-\mathbf{x}_i^\top \boldsymbol{\beta}}}$$

---

### Regularization
*Definition*:   
Regularization is adding tuning parameter (penalty term) to the error function of a model to induce smoothness in order to prevent overfitting by shrinking coefficients (which can significantly reduce the variance with some cost in bias; it can also perform variable selection).

*L1 & L2*:   
Lasso (L1): Find $\beta$ where minimize: $RSS + \lambda \sum_{i=1}^{p} |\beta_i|$

Ridge (L2): Find $\beta$ where minimize: $RSS + \lambda \sum_{i=1}^{p} \beta_i^2$

Lasso (L1) performs both coefficient shrinkage and variable selection, often producing sparse models because it can drive some coefficients exactly to zero. This makes Lasso particularly useful when the true underlying model is sparse and when interpretability or feature selection is important. 

Ridge (L2), on the other hand, only shrinks coefficients but never eliminates them, so it retains all predictors. It is especially effective when dealing with multicollinearity among features. L2 regularization handles multicollinearity better because it shrinks correlated coefficients together instead of forcing one to zero. This stabilizes the model and reduces variance when predictors are highly correlated.

*$\lambda$*:   
When $\lambda = 0$, both Lasso and Ridge become Linear Regression. When $\lambda \to \infty$, some $\beta = 0$ in Lasso, some $\beta \to 0$ in Ridge.
$\lambda$ is typically chosen using k-fold cross-validation, where we compute prediction error for a grid of $\lambda$ values and select the value that minimizes the average validation error.

*Feature Standarization*:    
We standardize features before Ridge/Lasso because the penalty depends on coefficient magnitude. If predictors are not on the same scale, the regularization will unevenly penalize them, distorting the solution. Standardization ensures fair penalization and stable estimates.

*L1 Sparce Model*:    
Because the L1 penalty uses the absolute value of coefficients, it creates a non-smooth optimization boundary with corners. During optimization, these corners promote exact zeros in the solution, which leads to automatic variable selection and sparsity. In contrast, the L2 constraint is circular and smooth, so the solution rarely lands exactly on an axis, which is why Ridge shrinks coefficients but almost never sets them exactly to zero.

*Elastic Net*:   
Elastic Net: Find $\beta$ where minimize: $RSS + \lambda_{\text{1}} \sum_{i=1}^{p} |\beta_i| + \lambda_{\text{2}} \sum_{i=1}^{p} \beta_i^2$

Elastic Net is useful when we have many correlated features and still want sparsity. It balances feature selection (L1) and coefficient stability (L2).

---

### Linear Discriminant Analysis
*Definition*:   
LDA is a classification method that seeks a linear combination of features that best separates the classes. It does so by maximizing between-class variance while minimizing within-class variance, effectively projecting the data onto a direction that best discriminates the groups.

LDA assumes that the feature vectors follow class-conditional multivariate normal distributions with shared covariance:

$$X \mid Y = k \sim N(\mu_k, \Sigma)$$

Under this assumption, LDA produces a linear decision boundary.

QDA (Quadratic Discriminant Analysis) extends LDA by allowing each class to have its own covariance matrix, resulting in non-linear (quadratic) boundaries.

Both LDA and QDA perform best when the classes are reasonably separable and the multivariate normality assumption approximately holds.

---

### Support Vector Machine
*Definition*:   
SVM is a classification/regression model that aims to find the best boundary to separate different classes. 

It does this by choosing a decision hyperplane that maximizes the margin to the closest data points, and when the data are not linearly separable, the kernel trick maps them into a higher-dimensional space where a linear separator becomes possible.

---

### K-Nearest Neighbors
*Definition*:   
KNN is a model that classifies data points based on the points that are most similar to it.

*Process*:   
To predict the class label for a new observation `X = x`, find the `K` training points closest to `x`, then assign `x` to the class that appears most often among those neighbors. Distance is measured with the Euclidean metric rather than Manhattan, since Euclidean captures straight‑line proximity instead of only horizontal/vertical steps.

---

### Decision Tree
*Definition*:   
A decision tree is a supervised machine learning algorithm used for both classification and regression. It recursively partitions the predictor space into smaller, homogeneous regions and makes predictions using the mean (regression) or mode (classification) of the training samples in each region.

*Process*:   
1. At each node, the algorithm searches for the best split (cut point) that minimizes impurity (e.g., Gini index, entropy, RSS).
2. The process repeats recursively, creating a tree structure.
3. Pruning is used to reduce overfitting by removing branches that add little predictive power.

*Advantages*: 
- Easy to interpret and visualize graphically;
- Works well when the true decision boundary aligns with axis-parallel splits;
- Easily handle qualitative predictors without the need to create dummy variables.

*Disadvantages*:
- Performs poorly when boundaries are diagonal or highly curved;
- Unstable to small changes in data (high variance) without pruning; can overfit without regularization.

---

### Random Forest
*Definition*:   
A random forest is an ensemble learning method that builds multiple randomized decision trees and aggregates their predictions (via averaging for regression or majority vote for classification). By combining many weakly correlated trees, random forest significantly reduces variance compared with a single decision tree.

*Sources of Randomness*:   
- Bootstrapped sampling (bagging): each tree is trained on a random sample of the training data.
- Feature randomness: each split considers a random subset of features, encouraging tree diversity.

---

### K-Means Clustering
*Definition*:   
K-Means is an unsupervised clustering algorithm that partitions n observations into k clusters. Each observation is assigned to the cluster with the nearest centroid, and the centroids are updated iteratively to minimize within-cluster variation.

*Elbow Method*:   
To determine an appropriate value of k, the elbow method plots:
- x-axis: number of clusters k
- y-axis: WCSS (Within-Cluster Sum of Squares), the sum of squared distances from each point to its cluster centroid
As k increases, WCSS decreases.

*Random Initialization*:   
Because K-Means is sensitive to the initial placement of centroids, the algorithm should be run multiple times with different random initializations. The best solution (lowest WCSS) is chosen to avoid poor local minima.

*Advantages*: 
- Computationally efficient, scales well to large datasets;
- Few parameters, easy to understand;
- Works well when clusters are spherical and well-separated;
- Efficient memory usage

*Disadvantages*:
- Requires specifying the number of clusters k beforehand;
- Different random seeds may lead to different results (local minima);
- Performs poorly on non-globular or complex-shaped clusters;
- Features with larger ranges dominate distance calculations unless standardized;
- A single outlier can heavily distort cluster centroids.

---

### Hierarchical Clustering
*Definition*:   
Hierarchical clustering is an unsupervised learning method that groups observations based on a measure of similarity.
Instead of specifying the number of clusters in advance, the algorithm builds a hierarchy of clusters that can be visualized as a dendrogram.
Compared with K-means, hierarchical clustering does not require choosing K beforehand, and the dendrogram allows users to select the number of clusters by “cutting” the tree at a chosen height.

*Main Approaches*:   
- Agglomerative (bottom-up): start with each observation as its own cluster and iteratively merge the closest pairs.
- Divisive (top-down): start with all observations in one cluster and recursively split into smaller clusters.