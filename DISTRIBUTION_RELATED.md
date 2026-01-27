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
Normal distribution is a probability distribution that is symmetric about the mean, showing that data near the mean are more frequent in occurrence than data far from the mean.

$$
N(\mu,\sigma^2) = \frac{1}{\sigma\sqrt{2\pi}}
e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

where:
- $X$ is a continuous random variable;
- $x$ is a specific value of $X$;
- $\mu$ is the mean of the distribution;
- $\sigma$ is the standard deviation of the distribution, with $\sigma > 0$;
- $\sigma^2$ is the variance of the distribution.

*Mean*: $E(X) = \mu $
*Variance*: $V(X)= \sigma^2$

*Properties*:
- Unimodal (Only one mode);
- Symmetrical (left and right halves are mirror images);
- Bell-shaped (maximum height (mode) at the mean);
- Mean, Mode, and Median are all located in the center;
- Asymptotic.

A normal random variable with $\mu = 0$ and $\sigma^2 = 1$ is said to be a standard normal distribution and is denoted $Z$.

Z-score: tells how many standard deviations are away from the mean:
- 1 standard deviation: 68%
- 2 standard deviations: 95%
- 3 standard deviations: 99%

---

### Discrete Probability Distribution
*Definition*:   
Discrete probability distribution of a discrete random variable (RV) is a table or graph that assigns a probability to each possible value of the random variable.

*Mean*: $E(X) = \mu = \sum_{x} x\, P(X = x)$
*Variance*: $V(X)= \sum_{x} (x - \mu)^2\, P(X = x)$

--- 

### Uniform Distribution
*Definition*:   
Uniform distribution is a probability distribution in which every possible result is equally likely.

$$U(a, b) = \frac{1}{b - a}, \quad a \le x \le b$$

where:
- $X$ is a continuous random variable uniformly distributed on the interval $[a, b]$;
- $x$ is a specific value of the random variable $X$;
- $a$ and $b$ are the lower and upper bounds of the distribution, with $a \lt b$.

*Mean*: $E(X) = \frac{a + b}{2}$   
*Variance*: $V(X) = \frac{(b - a)^2}{12}$

--- 

### Binomial Distribution
*Definition*:   
Binomial distribution is a probability distribution of obtaining one of two outcomes under a given number of parameters.

$$P(Y = y) = \binom{n}{y} p^y (1 - p)^{n - y}, \quad y = 0, 1, 2, \dots, n$$

where:
- $Y$ is a random variable representing the number of successes;
- $n$ is the number of independent trials;
- $p$ is the probability of success in each trial;
- $y$ is the number of successes.

*Assumption*:
- the trials are independent;
- only one outcome for each trial;
- the chance (for success $p$) is the same for every trial.

*Mean*: $E(X) = np$   
*Variance*: $V(X) = np(1 - p)$

--- 

### Bernoulli Distribution
*Definition*:   
Bernoulli distribution is a special case of the binomial distribution where a single trial is conducted.

$$P(Y = 1) = p, \quad P(Y = 0) = 1 - p$$

where:
- $Y$ is a Bernoulli random variable;
- $1$ represents success and $0$ represents failure;
- $p$ is the probability of success, with $0 \le p \le 1$.

*Mean*: $E(X) = p$   
*Variance*: $V(X) = p(1-p)$

--- 

### Poisson Distribution
*Definition*: 
Poisson distribution is a probability distribution of how many times an event is likely to occur over a specified period.

$$P(X = x) = \frac{e^{-\lambda} \lambda^x}{x!}, \quad x = 0, 1, 2, \dots$$

where:
- $X$ is a random variable representing the number of events occurring in a fixed interval;
- $x$ is a specific observed number of events;
- $\lambda$ is the average rate (mean number) of events per period, with $\lambda \gt 0$.

*Assumption*:
- the events are independent;
- two events cannot occur at exactly the same instant;
- the rate of events stays the same.

*Mean*: $E(X) = \lambda$   
*Variance*: $V(X) = \lambda$   

Poisson distribution can be approximated with normal distribution ($\mu = \lambda, \sigma^2 = \lambda$) when λ is large ($\lambda \ge 20$).   

Poisson distribution is the limiting case of binomial distribution when $n$ is very large and $p$ is very small ($\lambda = np$). 

--- 

### Exponential Distribution
*Definition*:   
Exponential distribution is a probability distribution of the time between events in a Poisson point process, a process in which events occur continuously and independently at a constant average rate.

*Mean*: $E(X) = \frac{1}{\lambda}$   
*Variance*: $V(X) = \frac{1}{\lambda^2}$   

Poisson distribution deals with the number of occurrences in a fixed period of time, and exponential distribution deals with the time between occurrences of successive events as time flows by continuously.