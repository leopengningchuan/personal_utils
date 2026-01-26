# Marketing Related
A curated knowledge base for distribution concepts, processes, and analytical foundations

## Table of Contents
- [Project Background](#project-background)
- [Project Goal](#project-goal)
- [Concepts](#concepts)
  - [Normal Distribution](#normal-distribution)
  - [Discrete Probability Distribution](#discrete-probability-distribution)
  - [Uniform Distribution](#uniform-distribution)
  - [Binomial Distribution](#binomial-distribution)
  - [Bernoulli Distribution](#bernoulli-distribution)
  - [Poisson Distribution](#poisson-distribution)
  - [Exponential Distribution](#exponential-distribution)

## Project Background
This document serves as a personal knowledge base for concepts, terminology, and analytical frameworks related to distribution systems and operations. It focuses on organizing key ideas that support understanding and analysis of distribution processes, performance, and decision-making.

## Project Goal
The goal of this document is to provide a centralized and structured reference for core distribution-related knowledge, enabling clearer understanding, consistent usage of terminology, and more effective analysis in distribution planning and operations.

## Concepts
### Normal Distribution
*Definition*:   

---

### Discrete Probability Distribution
*Definition*:   

--- 

### Uniform Distribution
*Definition*:   

--- 

### Binomial Distribution
*Definition*:   
Binomial distribution is a probability distribution of obtaining one of two outcomes under a given number of parameters.

$$
P(Y = y) = \binom{n}{y} p^y (1 - p)^{n - y}, \quad y = 0, 1, \dots, n

where:
- \(n\) is the number of independent trials,
- \(p\) is the probability of success in each trial,
- \(y\) is the number of successes.
$$

*Assumption*:
- the trials are independent;
- only one outcome for each trial;
- the chance (for success $p$) is the same for every trial

*Mean*: $E(X) = np$   
*Variance*: $V(X) = np(1-p)$

--- 

### Bernoulli Distribution
*Definition*:   
Bernoulli distribution is a special case of the binomial distribution where a single trial is conducted.

$$P(Y = 1) = p, \quad P(Y = 0) = 1 - p$$

*Mean*: $E(X) = p$   
*Variance*: $V(X) = p(1-p)$

--- 

### Poisson Distribution
*Definition*: 
Poisson distribution is a probability distribution of how many times an event is likely to occur over a specified period.

$$
P(X = x) = \frac{e^{-\lambda} \lambda^x}{x!}, \quad x = 0, 1, \dots, n
$$

*Assumption*:
- the events are independent;
- two events cannot occur at exactly the same instant;
- the rate of events stays the same.

*Mean*: $E(X) = \lambda$   
*Variance*: $V(X) = \lambda$   

Poisson distribution can be approximated with normal distribution (μ = λ, σ^2 = λ) when λ is large (λ>=20).   

Poisson distribution is the limiting case of binomial distribution when n is very large and p is very small (λ=np). 

--- 

### Exponential Distribution
*Definition*: 