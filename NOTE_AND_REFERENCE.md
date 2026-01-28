# Note and Reference
Curated resources and reusable utilities for general programming, documentation, and development workflows

## Table of Contents
- [Project Background](#project-background)
- [Project Goal](#project-goal)
- [Note](#note)
  - [SQL Syntax Related](#sql-syntax-related)
  - [Statistics Related](#statistics-related)
    - [P-Value](#p-value)
    - [Coefficient Value](#coefficient-value)
    - [Collinearity](#collinearity)
    - [Confidence Intervals & Prediction Intervals](#confidence-intervals--prediction-intervals)
    - [Confusion Matrix](#confusion-matrix)
    - [ROC Curve](#roc-curve)
    - [Hypothesis Testing](#hypothesis-testing)
    - [F-Test](#f-test)
    - [Chi-square Test](#chi-square-test)
    - [Covariance & Correlation](#covariance--correlation)
    - [PCA](#pca)
    - [z-distribution & t-distribution](#z-distribution--t-distribution) 
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

#### P-Value
*Definition*:   
Assuming the null hypothesis is true, the probability of obtaining a result equal to or "more extreme" than what was actually observed.

The p-value in the table is the minimum α (the level of significance, a user defined value) at which the coefficient is relevant. The lower the p-value, the more important is the variable in predicting the price.

---

#### Coefficient Value
*Definition*:   
Holding other variables in the model constant, how much the mean of the dependent variable changes if the independent variable changes by one unit.

---

#### Collinearity
*Definition*:   
Ttwo or more independent variables are closely related to one another

VIF, variance inflation factor, is a measure of the amount of multicollinearity in a set of multiple regression variables. If VIF > 10, the multicollinearity is severe.

---

#### Confidence Intervals & Prediction Intervals
*Definition*:   
Confidence intervals tell you how well you have determined a parameter of interest.
Prediction intervals tell you where you can expect to see the next data point sampled. 

Confidence interval shows the likely range of values associated with some statistical parameter of the data, such as the population mean.
Prediction intervals predicts in what range a future individual observation will fall. 
Confidence interval CI are about the parameter of the population; prediction Interval PI are about outcomes. CI are much lower than PI.

---

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

![*ROC Example*](images/roc_example_20251205.jpg)

- x Axis: False Positive Rate ($\frac{FP}{FP+TN}$)		
- y Axis: True Positive Rate (Sensitivity, Recall, $\frac{TP}{TP+FN}$)
- Left-down corner (0, 0): All classified as N, FP = 0 and TP = 0
- Right-up corner (1, 1): All classified as T, FP = 1 and TP = 1
- ROC is robust to imbalance, unlike raw accuracy.

---

#### Hypothesis Testing
*Definition*:   
Hypothesis testing is a form of statistical inference that uses data from a sample to draw conclusions about a population parameter or a population probability distribution.

---

#### F-Test
*Definition*:   
An F-test is any statistical test that uses an F-distributed test statistic under the null hypothesis.
The F-statistic is typically constructed as a ratio of two independent variance estimates (mean squares), each scaled by their degrees of freedom.
It is used to compare variability across groups, compare statistical models, or test joint hypotheses about parameters.

**F-test in Linear Regression (Model Significance Test)**
The F-statistic tells if any of the independent variables is related to the dependent variable.

Hypotheses:

$$H_0: \beta_1 = \beta_2 = ... = \beta_k = 0$$

$$H_1: \text{At least one} \beta_i ≠ 0$$

Relationship between F-test and t-test:
In simple linear regression (one predictor), the overall F-test is mathematically equivalent to the t-test for the slope, because:

$$F = t^2$$

This equivalence holds only when the model has a single predictor. In multiple regression, ANOVA, or variance tests, F-tests serve different purposes and are not interchangeable with t-tests.

**F-test in ANOVA (Analysis of Variance)**
The F-statistic tells if the means of two or more population are equal.

Hypotheses:

$$H_0: \mu_1 = \mu_2 = ... = \mu_k$$

In ANOVA, the F-statistic compares:
- Between-group variance: how far the group means are from each other
- Within-group variance: random variation inside each group
F is the ratio of between-group mean square to within-group mean square.
If the group means are truly equal, the differences between groups should be no larger than random noise, so the two variances are similar and F ≈ 1.
But if between-group variance is much larger than within-group variance, the observed differences cannot be explained by randomness alone, meaning the group means must differ.

**F-test of Equal Variances**
The F-statistic tells if whether two normal populations have the same variance.

Hypotheses:

$$H_0: \sigma_1^2 = \sigma_2^2$$

---

#### Chi-square Test
*Definition*:   
The Chi-square test is a statistical hypothesis test used to compare observed frequencies with expected frequencies under a given null hypothesis.

$$\chi^2 = \sum_{i=1}^{r} \sum_{j=1}^{c} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$

**Chi-square Goodness-of-fit Test**
The Chi-square Goodness-of-fit test examines whether a sample distribution is consistent with a specified theoretical distribution.
It compares the observed frequencies of a single categorical variable to the frequencies expected under a specified theoretical distribution.

**Chi-square Test of Independence**
The Chi-square Test of independence examines whether there is a statistically significant association between two categorical variables.
It compares the observed frequencies in a contingency table to the frequencies expected if the two categorical variables are independent.

**Chi-square Test of Homogeneity**
The Chi-square test of homogeneity is a statistical hypothesis test used to determine whether different populations have the same distribution of a categorical variable.
It compares the observed frequencies across groups to the frequencies expected if all populations share an identical distribution.

---

#### Covariance & Correlation
*Definition*:   
Covariance indicates the direction of the relationship between two variables but is scale-dependent and difficult to interpret in magnitude. 

Correlation standardizes covariance by the variables’ standard deviations, providing a unit-free measure of both the strength and direction of their linear relationship.

Pearson correlation measures linear association only. Variables can be positively related in a nonlinear or monotonic way while exhibiting low or zero Pearson correlation.

---

#### PCA
*Definition*:   
PCA (Principal Component Analysis) is a dimensionality reduction technique that projects high-dimensional data onto a lower-dimensional linear subspace.

The projection is chosen such that the first principal component captures the maximum possible variance in the data, and each subsequent component captures the maximum remaining variance subject to being orthogonal to the previous ones.

The resulting principal components define the best low-dimensional linear approximation of the original data in terms of minimizing reconstruction error.

---

#### z-distribution & t-distribution
The z-distribution is the standard normal distribution with mean 0 and standard deviation 1. It is used when the population standard deviation is known, or when the sample size is large (more than 30 in practice) and the Central Limit Theorem applies.

The t-distribution is similar to the z-distribution but has heavier tails. It is used when the population standard deviation is unknown and must be estimated from the sample. The shape of the t-distribution depends on the sample size (degrees of freedom); with smaller samples, it is more spread out and produces wider confidence intervals.

As the sample size increases, the t-distribution converges to the z-distribution.

---

## Reference

### Markdown Related
- [Markdown Guide: Basic Syntax](https://www.markdownguide.org/basic-syntax/) – Common formatting styles for Markdown documents.
- [readme.so](https://readme.so) – Visual tool for generating clean and readable README files.
- [shields.io](https://shields.io) – Generate custom badges for documentation, build status, and version info.
- [Mathematics in R Markdown](https://rpruim.github.io/s341/S19/from-class/MathinRmd.html) – LaTeX math expressions in Markdown.
- [Open Source Initiative](https://opensource.org) – Official resource for open source licensing and governance.

### GitHub & Version Control
- [GitHub Basics (in CN)](https://blog.csdn.net/u011296485/article/details/83717493) – Step-by-step GitHub usage tutorial in Chinese, covering commits, branches, and pull requests.
