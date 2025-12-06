# Note and Reference
Curated resources and reusable utilities for general programming, documentation, and development workflows

## Table of Contents
- [Project Background](#project-background)
- [Project Goal](#project-goal)
- [Note](#note)
  - [SQL Syntax Related](#sql-syntax-related)
  - [Statistics Related](#statistics-related)
    - [Confusion Matrix](#confusion-matrix)
    - [ROC Curve](#roc-curve)
  - [Regression/Classification Models](#regression-classification-models)
    - [Linear Regression](#linear-regression)
    - [Logistic Regression](#logistics-regression)
    - [Linear Discriminant Analysis](#linear-discriminant-analysis)
    - [Support Vector Machine](#support-vector-machine)
    - [K-Nearest Neighbors](#k-nearest-neighbors)
    - [Decision Tree](#decision-tree)
    - [Random Forest](#random-forest)
    - [K-Means Clustering](#k-means-clustering)
    - [Hierarchical Clustering](#hierarchical-clustering)
  - [Model Related](#model-related)
    - [Feature Engineering](#feature-engineering)
    - [Feature Selection](#feature-selection)
    - [Hyperparameter Search](#hyperparameter-search)
    - [Bias & Variance](#bias--variance)
    - [Overfitting & Underfitting](#overfitting--underfitting)
    - [Imbalanced Data](#imbalanced-data)
    - [Resampling](#resampling)
    - [Cross-Validation](#cross-validation)
    - [Bootstrapping](#bootstrapping)

- [Reference](#reference)
  - [Markdown Related](#markdown-related)
  - [GitHub & Version Control](#github--version-control)

## Project Background
This document collects essential tools, reference materials, and workflow notes that support software development tasks. It serves as a personal knowledge base aimed at strengthening documentation, automation, and overall programming proficiency.

## Project Goal
To provide a centralized reference hub for commonly used techniques and websites across various programming languages and development environments.

## Note

### SQL Syntax Related
General:
- `LIMIT 1 OFFSET 1` – Skip the first row and returns the next one
- `SUM(IF(flag_col = TRUE, 1, 0))` – Count rows where flag is true by summing 1s and 0s
- `OVER(ORDER BY date_col ROWS BETWEEN 2 PRECEDING AND 1 FOLLOWING)` – Window function preceding and following data
- `DELETE FROM table WHERE id IN ()` – Delete the rows in table where id meets the standard
- `CAST(str_col AS data_type)` – Change the column data type
- `BIT_AND() / BIT_OR()` – Perform logical operations on the corresponding bits of two integers

Math related:
- `IFNULL(num_col, 0)` – Use 0 to substitute if the value is NULL
- `POWER(num_col, 3)` – Return the value raised to the 3rd power
- `SQRT(num_col)` – Return the square root of the value
- `LEAST(num_col), GREATEST(num_col)`– Return the minimal/maximal of the value
- `FLOORT(num_col), CEIL(num_col)`– Return the largest/smallest integer value that is less/greater than or equal to the value

Date and Time related
- `DATEDIFF(DAY, start_date_col, end_date_col)` – Calculate the days between start_date and end_date
- `TIMESTAMPDIFF(SECOND, start_timestamp_col, end_timestamp_col)`– Calculate the seconds between start_timestamp and end_timestamp
- `DATE_ADD(date_col, INTERVAL 10 DAY)` – Get the 10 days later of date
- `DATE_SUB(date_col, INTERVAL 10 MONTH)` – Get the 10 months prior of date
- `MONTHNAME(date_col)` – Get the month name of the date
- `DAYNAME(date_col)` – Get the day name of the date
- `WEEKDAY(date_col)` – Get the weekday index (0 = Monday, 6 = Sunday) for the date
- `WEEK(date_col)` – Get the week sequence of the year for the date
- `TIME_FORMAT(timestamp_col, '%H:%i:%s')` – Return the timestamp based on the required time format
- `SEC_TO_TIME(timestamp_col)` – Return the timestamp based on the specified seconds
- `TIME(timestamp_col) BETWEEN '11:00:00' AND '14:00:00'` – Return the timestamp in the required range

String related:
- `LENGTH(str_col)` – Return the length of a string in bytes
- `CHAR_LENGTH(str_col)` – Return the length of a string in characters
- `LEFT(str_col, 7)` – Get the first 7 characters from left
- `GROUP_CONCAT(str_col ORDER BY str_col SEPARATOR ', ')` – Group the string with separator
- `REPLACE(str_col, ' ', '')` – Remove the space in the col
- `SUBSTR(str_col, 3, 4)` – Return a substring starting at position 5 with length 3
- `SUBSTRING_INDEX(str_col, '@', -1)` – Return a substring part after the last @
- `REGEXP '^[a-zA-z][a-zA-z0-9._-]*@test\\.com$'` – Return a string follows the REGEX expression
- `REGEXP_SUBSTR(str_col, '#[A-Za-z0-9_]+')'` – Return a string part that match the REGEX expression
- `str_col LIKE '@%_'` – Return a string that follows the pattern (`%` represents zero, one, or multiple characters; `_` represents one, single character)

---

### Statistics Related

#### Confusion Matrix
*Definition*:   
| Actual/Predict | 1              | 0              |
|----------------|:--------------:|---------------:|
| 1              | True Positive  | False Negtaive |
| 0              | False Positive | True Negtaive  |

- Type I Error: False Positive				
- Type II Error: False Negative
- $Accuracy = \frac{TP+TN}{P+N}$
- $Error Rate = \frac{FP+FN}{P+N}$			
- True Positive Rate/Recall (Higher sensitivity → lower Type II error): $Sensitivity = \frac{TP}{TP+FN}$	  
- True Negative Rate (Higher specificity → lower Type I error): $Specificity = \frac{TN}{TN+FP}$	  
- Positive Predicted Value: $Precision = \frac{TP}{TP+FP}$	
- $F Score = \frac{2}{\frac{1}{Recall}+\frac{1}{Precision}} = \frac{2TP}{2TP+FP+FN}$

---

#### ROC Curve
*Definition*:   
A Receiver Operating Characteristic (ROC) curve is a diagnostic plot that illustrates the performance of a binary classifier across all possible classification thresholds. It shows the trade-off between the True Positive Rate (TPR) and the False Positive Rate (FPR) as the decision threshold varies. 

A model with a curve closer to the top-left corner demonstrates stronger discriminative ability, and the Area Under the Curve (AUC) summarizes this performance into a single metric.

![*ROC Example*](images/roc_example_20251205.png)

- x Axis: False Positive Rate ($\frac{FP}{FP+TN}$)		
- y Axis: True Positive Rate (Sensitivity, Recall, $\frac{TP}{TP+FN}$)
- Left-down corner (0, 0): All classified as N, FP = 0 and TP = 0
- Right-up corner (1, 1): All classified as T, FP = 1 and TP = 1
- ROC is robust to imbalance, unlike raw accuracy.

---

### Regression/Classification Models

#### Linear Regression
*Definition*:   
Linear regression is a regression model that assumes a linear relationship between the independent variables and the single dependent variable.

$$y_i = \beta_0 + \beta_1 x_{i1} + \dots + \beta_p x_{ip} + \varepsilon_i$$

*Assumptions*: 
1. There is a linear relationship between the dependent variables and the independent variables, meaning the model you are creating actually fits the data;
2. The residuals errors of the data are normally distributed and independent from each other;
3. There is minimal multicollinearity between independent variables;
4. Homoscedasticity: variance of error terms is the same for all values of x.

*Drawbacks*:
1. Strong assumptions that may not be true in application;
2. Cannot be used in discrete or binary outcome;
3. Cannot vary the model flexibility;
4. Very non robust.

*RMSE, RSS, R2 & Adj R2*:   
Linear Regression Solution: Minimize residual sum of squares (RSS), $R^2 = 1-\frac{RSS}{TSS}$
Total sum of squares (TSS) = Explained sum of squares (ESS) + Residual sum of squares (RSS)

RMSE, Root Mean Square Error, is the standard deviation of the residuals. Residuals are a measure of how far from the regression line data points are; RMSE is a measure of how spread out these residuals are.

$$RMSE = \sqrt{\frac{RSS}{n}} $$

$R^2$ is a statistical measure that represents the proportion of the variance for a dependent variable that's explained by the independent variables in a regression model. R2 can have a negative value when the model selected does not follow the trend of the data.

$R_Adj^2$ is a modified version of R2 which takes n (number of observations) and k (number of independent variables) into account. It can be used to compare models that have a different number of variables. $R_Adj^2$ is always lower than $R^2$.

$$R_Adj^2 = 1 - (1 - R^2)\frac{n - 1}{n - k - 1}$$

---

#### Logistic Regression
*Definition*:   
Logistic Regression is a classification model which uses the logit model to predict the binary outcome of dependent variable from a linear combination of independent variables.

$$P(Y=1 \mid X=x) = \frac{e^{\beta_0 + \beta_1 x}}{1 + e^{\beta_0 + \beta_1 x}}$$
or
$$\log \frac{P(Y=1 \mid X=x)}{P(Y=0 \mid X=x)} = \beta_0 + \beta_1 x$$

*Maximum likelihood approach*:   
The logit of the estimated probability response is a linear function of the predictor parameters.

$$\text{Log-likelihood: } \ell(\boldsymbol{\beta}) = \sum_{i=1}^n \Big[ y_i \log p_i + (1 - y_i)\log(1 - p_i) \Big], \quad p_i = \sigma(\mathbf{x}_i^\top \boldsymbol{\beta}) = \frac{1}{1 + e^{-\mathbf{x}_i^\top \boldsymbol{\beta}}}$$

---

#### Linear Discriminant Analysis
*Definition*:   
LDA is a classification method that seeks a linear combination of features that best separates the classes. It does so by maximizing between-class variance while minimizing within-class variance, effectively projecting the data onto a direction that best discriminates the groups.

LDA assumes that the feature vectors follow class-conditional multivariate normal distributions with shared covariance:

$$X \mid Y = k \sim N(\mu_k, \Sigma)$$

Under this assumption, LDA produces a linear decision boundary.

QDA (Quadratic Discriminant Analysis) extends LDA by allowing each class to have its own covariance matrix, resulting in non-linear (quadratic) boundaries.

Both LDA and QDA perform best when the classes are reasonably separable and the multivariate normality assumption approximately holds.

---

#### Support Vector Machine
*Definition*:   
SVM is a classification/regression model that aims to find the best boundary to separate different classes. 

It does this by choosing a decision hyperplane that maximizes the margin to the closest data points, and when the data are not linearly separable, the kernel trick maps them into a higher-dimensional space where a linear separator becomes possible.

---

#### K-Nearest Neighbors
*Definition*:   
KNN is a model that classifies data points based on the points that are most similar to it.

*Process*:   
To predict the class label for a new observation `X = x`, find the `K` training points closest to `x`, then assign `x` to the class that appears most often among those neighbors. Distance is measured with the Euclidean metric rather than Manhattan, since Euclidean captures straight‑line proximity instead of only horizontal/vertical steps.

---

#### Decision Tree
*Definition*:   
A decision tree is a supervised machine learning algorithm used for both classification and regression. It recursively partitions the predictor space into smaller, homogeneous regions and makes predictions using the mean (regression) or mode (classification) of the training samples in each region.

*Process*:   
1. At each node, the algorithm searches for the best split (cut point) that minimizes impurity (e.g., Gini index, entropy, RSS).
2. The process repeats recursively, creating a tree structure.
3. Pruning is used to reduce overfitting by removing branches that add little predictive power.

*Advantages*: 
1. Easy to interpret and visualize graphically;
2. Works well when the true decision boundary aligns with axis-parallel splits;
3. Easily handle qualitative predictors without the need to create dummy variables.

*Disadvantages*: 
1. Performs poorly when boundaries are diagonal or highly curved;
2. Unstable to small changes in data (high variance) without pruning; can overfit without regularization.

---

#### Random Forest
*Definition*:   
A random forest is an ensemble learning method that builds multiple randomized decision trees and aggregates their predictions (via averaging for regression or majority vote for classification). By combining many weakly correlated trees, random forest significantly reduces variance compared with a single decision tree.

*Sources of Randomness*:   
- Bootstrapped sampling (bagging): each tree is trained on a random sample of the training data.
- Feature randomness: each split considers a random subset of features, encouraging tree diversity.

---

#### K-Means Clustering
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
1. Computationally efficient, scales well to large datasets;
2. Few parameters, easy to understand;
3. Works well when clusters are spherical and well-separated;
4. Efficient memory usage

*Disadvantages*: 
1. Requires specifying the number of clusters k beforehand;
2. Different random seeds may lead to different results (local minima);
3. Performs poorly on non-globular or complex-shaped clusters;
4. Features with larger ranges dominate distance calculations unless standardized;
5. A single outlier can heavily distort cluster centroids.

---

#### Hierarchical Clustering
*Definition*:   
Hierarchical clustering is an unsupervised learning method that groups observations based on a measure of similarity.
Instead of specifying the number of clusters in advance, the algorithm builds a hierarchy of clusters that can be visualized as a dendrogram.
Compared with K-means, hierarchical clustering does not require choosing K beforehand, and the dendrogram allows users to select the number of clusters by “cutting” the tree at a chosen height.

*Main Approaches*:   
- Agglomerative (bottom-up): start with each observation as its own cluster and iteratively merge the closest pairs.
- Divisive (top-down): start with all observations in one cluster and recursively split into smaller clusters.

---

### Model Related

#### Feature Engineering
*Definition*:   
Feature engineering is the process of transforming raw features into features that better represent the underlying problem to the predictive models, resulting in improved model accuracy on unseen data.

---

#### Feature Selection
*Definition*:   
Feature selection is the process of reducing the number of input variables when developing a predictive model, aiming at reducing the computational cost of modeling and improve the performance of the model.

*Methods*:
-	Best Subset Selection: Test all subsets and find the best performance one or until some stopping criterion is met.
-	Forward Stepwise Selection: Forward selection starts with an empty set of variables and adds variables to it until some stopping criterion is met. (Might miss the optimal subset of features)
- Backward Stepwise Selection: Backward selection starts with a complete set of variables and then excludes variables from that set until some stopping criterion is met. (Might miss the optimal subset of features)

---

#### Hyperparameter Search
*Definition*:   
A hyperparameter is a parameter used to control the learning process in machine learning. Parameters are the configuration model, which are internal to the model. Hyperparameters are the explicitly specified parameters that control the training process.

*Methods*:
-	Grid search: An exhaustive search that is performed on the specific parameter values of a model.
-	Random search: The values of the hyperparameters are selected randomly.
-	Hill climbing: At each iteration selects the best direction in the hyperparameter space to choose the next hyperparameter value.
-	Bayesian optimization: Tt is an approach that uses Bayes Theorem to direct the search in order to find the minimum or maximum of an objective function. It selects the next hyperparameter value based on the function outputs in the previous iterations; but unlike hill climbing, it looks at past iterations globally and not only at the last one.

---

#### Bias & Variance
*Definition*:   
Bias is the amount that a model’s prediction differs from the target value, compared to the training data.

Variance describes how much a random variable differs from its expected value.

---

#### Overfitting & Underfitting
*Definition*:   
Overfitting is a model fits exactly against its training data and have performs badly on unobserved data. It leads to high variance and low bias model. It happens when the learning power is too high, data size is too small. It can be solved by reducing model complexity (regularization) and increase the data volume.

Underfitting means the machine learning model has very low accuracy. Its occurrence the model does not fit the data well enough.

---

#### Imbalanced Data
*Definition*:   
Imbalanced data refers to those types of datasets where the target class has an uneven distribution of observations.

An effective way to handle imbalanced data is to downsample and upweight the majority class:
- Downsampling: training on a disproportionately low subset of the majority class examples.
- Upweighting: adding an example weight to the downsampled class equal to the factor by which you downsampled.

---

#### Resampling
*Definition*:   
Resampling refers to methods that repeatedly draw samples from the available training data and recompute a model or statistic on each sample. It is used to estimate model performance, assess model stability, and quantify uncertainty.

*Methods*:
- Cross-Validation: Evaluates model prediction error by repeatedly splitting the data into different training/validation sets.
- Bootstrap: Draws samples with replacement from the training data to estimate model variance, stability, or confidence intervals.

---

#### Cross-Validation
*Definition*:   
Cross-validation is a resampling procedure used to evaluate machine learning models on a limited data sample. The simplest example of cross-validation is when you split your data into two groups: training data and testing data, where you use the training data to build the model and the testing data to test the model.

*Methods*:   
- K-Fold Cross-Validation: Partitioning a dataset into k groups, where each group is given the opportunity of being used as a held-out test set leaving the remaining groups 
- Leave One Out Cross-Validation (LOOCV): a cross-validation approach in which each observation is considered as the validation set and the rest (N-1) observations are considered as the training set (k = n).

---

#### Bootstrapping
*Definition*:   
Bootstrapping: Samples are drawn from the dataset with replacement, where those instances not drawn into the data sample may be used for the test set.
Bagging (= bootstrap aggregation) is performing it many times and training an estimator for each bootstrapped dataset.


## Reference

### Markdown Related
- [Markdown Guide: Basic Syntax](https://www.markdownguide.org/basic-syntax/) – Common formatting styles for Markdown documents.
- [readme.so](https://readme.so) – Visual tool for generating clean and readable README files.
- [shields.io](https://shields.io) – Generate custom badges for documentation, build status, and version info.
- [Mathematics in R Markdown](https://rpruim.github.io/s341/S19/from-class/MathinRmd.html) – LaTeX math expressions in Markdown.
- [Open Source Initiative](https://opensource.org) – Official resource for open source licensing and governance.

### GitHub & Version Control
- [GitHub Basics (in CN)](https://blog.csdn.net/u011296485/article/details/83717493) – Step-by-step GitHub usage tutorial in Chinese, covering commits, branches, and pull requests.
