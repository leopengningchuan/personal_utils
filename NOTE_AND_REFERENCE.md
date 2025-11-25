# Note and Reference
Curated resources and reusable utilities for general programming, documentation, and development workflows

## Table of Contents
- [Project Background](#project-background)
- [Project Goal](#project-goal)
- [Note](#note)
  - [SQL Syntax Related](#sql-syntax-related)
  - [Statistics Related](#statistics-related)
    - [Confusion Matrix](#confusion-matrix)
  - [Model Related](#model-related)
    - [Linear Regression](#linear-regression)
    - [Logistic Regression](#logistics-regression)
    - [K-Nearest Neighbors](#k-nearest-neighbors)
    - [Decision Tree](#decision-tree)
    - [Random Forest](#random-forest)
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


### Statistics Related

#### Confusion Matrix

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


### Model Related

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


#### Logistic Regression
*Definition*:   
Logistic Regression is a classification model which uses the logit model to predict the binary outcome of dependent variable from a linear combination of independent variables.

$$P(Y=1 \mid X=x) = \frac{e^{\beta_0 + \beta_1 x}}{1 + e^{\beta_0 + \beta_1 x}}$$
or
$$\log \frac{P(Y=1 \mid X=x)}{P(Y=0 \mid X=x)} = \beta_0 + \beta_1 x$$

*Maximum likelihood approach*:   
The logit of the estimated probability response is a linear function of the predictor parameters.

$$\text{Log-likelihood: } \ell(\boldsymbol{\beta}) = \sum_{i=1}^n \Big[ y_i \log p_i + (1 - y_i)\log(1 - p_i) \Big], \quad p_i = \sigma(\mathbf{x}_i^\top \boldsymbol{\beta}) = \frac{1}{1 + e^{-\mathbf{x}_i^\top \boldsymbol{\beta}}}$$


#### K-Nearest Neighbors
*Definition*:   
KNN is a model that classifies data points based on the points that are most similar to it.

*Process*:   
To predict the class label for a new observation `X = x`, find the `K` training points closest to `x`, then assign `x` to the class that appears most often among those neighbors. Distance is measured with the Euclidean metric rather than Manhattan, since Euclidean captures straight‑line proximity instead of only horizontal/vertical steps.


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


#### Random Forest
*Definition*:   
A random forest is an ensemble learning method that builds multiple randomized decision trees and aggregates their predictions (via averaging for regression or majority vote for classification). By combining many weakly correlated trees, random forest significantly reduces variance compared with a single decision tree.

*Sources of Randomness*:   
- Bootstrapped sampling (bagging): each tree is trained on a random sample of the training data.
- Feature randomness: each split considers a random subset of features, encouraging tree diversity.


## Reference

### Markdown Related
- [Markdown Guide: Basic Syntax](https://www.markdownguide.org/basic-syntax/) – Common formatting styles for Markdown documents.
- [readme.so](https://readme.so) – Visual tool for generating clean and readable README files.
- [shields.io](https://shields.io) – Generate custom badges for documentation, build status, and version info.
- [Mathematics in R Markdown](https://rpruim.github.io/s341/S19/from-class/MathinRmd.html) – LaTeX math expressions in Markdown.
- [Open Source Initiative](https://opensource.org) – Official resource for open source licensing and governance.

### GitHub & Version Control
- [GitHub Basics (in CN)](https://blog.csdn.net/u011296485/article/details/83717493) – Step-by-step GitHub usage tutorial in Chinese, covering commits, branches, and pull requests.
