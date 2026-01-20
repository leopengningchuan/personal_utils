# Marketing Related
Organized knowledger and resources for marketing related filed

## Table of Contents
- [Project Background](#project-background)
- [Project Goal](#project-goal)
- [Note](#note)
  - [CAC](#cac)
  - [LTV](#lvt)
  - [ROAS](#roas)
  - [Incrementality](#incrementality)
  - [MMM](#mmm)

## Project Background
This document collects terms and knowledge that support data related to marketing. It serves as a personal knowledge base aimed at understanding the intersection of data and marketing.

## Project Goal
To provide a centralized reference hub for commonly used terms and information related to marketing and data field related to marketing.

## Note
### CAC
*Definition*:   
CAC (Customer Acquisition Cost) measures the spending to acquire one paying customer.

$$CAC = Total Marketing and Sales Spend/Number of New Pay Customers$$

If CAC is going up but revenue is still growing, we need to compare whether the CAC is more than the LTV to decide whether it is healthy.

---

### LTV
*Definition*:   
LTV (Lifetive Value) measures how much revenue a customer generates over their lifetime.

$$LTV  = ARPU(Average Revenue Per User)*Retention Time = ARPU/ChurnRate$$

LTV/CAC > 3 is a signal of a healthy increasement.

--- 

### ROAS
*Definition*:   
ROAS (Return on Ad Spend) measures the revenue generated for every dollar spent on advertising (media efficiency, not business profitability).

$$ROAS = Ad Revenue / Ad Spend$$

The ROAS can be high, but there is still loss: 
- High return and cancellation rate
- High fulfillment cost
- HIgh fixed operation cost
- Low gross margin

In the long term, LTV/CAC is more important than ROAS.

--- 

### Incrementality
*Definition*:   
Incrementality measures the true causal impact of a marketing channel—what conversions would not have happened without the intervention. Unlike standard A/B tests that measure surface-level lift, incrementality isolates net-new behavior using holdout or geo-based experimentation. It’s critical for avoiding over-attribution and allocating budget to channels that truly drive growth.

Methods:
- Holdout Test
- Geo Test

A/B testing compares two variants under intervention and tells us which performs better, while holdout testing removes the intervention entirely to measure true incremental lift. Holdout tests answer the causal question of whether the marketing effort creates net-new conversions, not just redistributed ones.

--- 

### MMM
*Definition*:   
Marketing Mix Modeling (MMM) is a regression-based approach that estimates the incremental impact of each marketing channel on sales or conversions. Unlike attribution or A/B testing, MMM works with aggregated data and can measure channels where user-level data is not available, such as TV, influencers, or brand campaigns.

MMM is essential because it quantifies the true incremental lift of each channel and enables budget optimization. It answers questions like: “If we increase spend on Facebook by 10%, how much sales will we gain?”

What does MMM Output?
- Incremental contribution
- Diminishing return curves
- Elasticity
- Optimal budget allocation


Why use linear regression for MMM since channels are not independent?   
Marketing channels are not independent and often influence each other. MMM doesn’t assume independence; instead, linear regression is used to estimate the marginal effect of each channel while controlling for others.

Because channels are highly correlated, MMM typically relies on regularization methods like Ridge or Elastic Net to stabilize coefficients and avoid over-attribution. The goal isn’t to perfectly model the causal structure, but to produce stable, interpretable estimates that can guide budget allocation decisions.


Adstock:   
MMM uses adstock transformations to capture carryover effects, because marketing impact often persists over time rather than disappearing immediately after spend.

Saturation:   
MMM models diminishing returns using saturation curves, allowing teams to estimate marginal ROI and allocate budget more efficiently across channels.
