# **Bluestone Real Estate ML Platform**
## Overview

The Bluestone Real Estate Machine Learning Platform is an end-to-end predictive analytics system designed to support real estate decision-making by forecasting:

- Rental demand probability

- Property sale price

The system uses property listing characteristics, market indicators, and customer engagement metrics to generate predictive insights.

The models are deployed as a live REST API allowing real-time predictions.

## Live API

Base URL

https://bluestone-realestate-api.onrender.com

API documentation

https://bluestone-realestate-api.onrender.com/docs

Health check

https://bluestone-realestate-api.onrender.com/

Response

{
  "message": "Bluestone Real Estate ML API running"
}
## Business Problem

Real estate companies need data-driven tools to:

- estimate property sale prices

- identify listings likely to rent quickly

- optimize pricing strategies

- improve marketing allocation

Manual analysis is time-consuming and often subjective.

This project provides machine learning models to automate predictions using historical real estate data.

## Machine Learning Models

Two predictive models were developed.

### Rental Demand Model

**Type: Classification**

Predicts whether a listing is likely to be rented.

Target variable

is_rented

Example output

{
  "prediction": 0,
  "probability": 0.24
}
### Sales Price Model

**Type: Regression**

Predicts final property sale price.

Example output

{
  "predicted_log_price": 13.19,
  "predicted_price": 539000
}

#### Model Performance
**Rental Model**
Metric	      Score
Accuracy - 0.866
Precision - 0.962
Recall - 0.445
AUC-ROC - 0.883

The model prioritizes precision, ensuring reliable identification of high-probability rental listings.

**Sales Price Model**
Metric	  Score
MAE	- 0.021
RMSE - 0.028
R² - 0.999

The regression model demonstrates strong predictive accuracy for estimating final sale prices relative to market conditions.

### Feature Engineering

#### Key engineered features include:

 Rental model

- price vs city average

- inquiry engagement

- response time metrics

- listing duration

- pricing intensity

Sales model

- offer vs market ratio

- market price comparison

- inquiry engagement score

- closing speed relative to market

These features significantly improved predictive performance.

### Technology Stack
Component	          Technology
Language	Python
Data Processing -	Pandas, NumPy
Machine Learning - Scikit-Learn
API Framework	- FastAPI
Containerization	- Docker
Container Registry	- Docker Hub
Cloud Deployment	- Render

### System Architecture

Data Sources
     │
     ▼
Data Cleaning & Feature Engineering
     │
     ▼
Model Training
(Random Forest / Gradient Boosting)
     │
     ▼
Model Evaluation
     │
     ▼
Model Serialization (Joblib)
     │
     ▼
FastAPI Prediction Service
     │
     ▼
Docker Container
     │
     ▼
Docker Hub Registry
     │
     ▼
Render Cloud Deployment
     │
     ▼
Public REST API


### API Endpoints

#### Rental Prediction

POST /predict/rental

Example request

{
  "log_price": 7.5,
  "LISTING_TYPE": "Apartment",
  "parsed_city": "Austin",
  "parsed_state": "TX",
  "parsed_zip": "78745",
  "listing_month": 3,
  "listing_quarter": 1,
  "listing_year": 2026,
  "avg_lead_score": 6,
  "avg_follow_up": 2,
  "avg_response_time": 12,
  "price_city_mean": 2100,
  "log_price_per_day_on_market": 2.5,
  "DAYS_ON_MARKET_capped": 30,
  "price_vs_city_mean_capped": 0.95,
  "inquiry_count_capped": 4
}

#### Sales Price Prediction

POST /predict/sales

Returns estimated final sale price.

### Deployment

#### Deployment pipeline

Model Training
      │
      ▼
Model Serialization
      │
      ▼
FastAPI Inference Service
      │
      ▼
Docker Container
      │
      ▼
Docker Hub
      │
      ▼
Render Cloud Deployment


#### Rebuilding the System

Train models

python train_models.py

Build container

docker build -t bluestone-realestate-api .

Push image

docker push etang1oj/bluestone-realestate-api

Redeploy on Render.

### Future Improvements

Potential enhancements include:

- automated retraining pipeline

- prediction monitoring dashboard

- model drift detection

- integration with real estate platforms

- Snowflake data warehouse integration


# **Business Value & Impact**
## Why This Project Matters

Real estate companies operate in highly competitive and dynamic markets. Decisions around pricing, marketing, and inventory management often rely on manual analysis or intuition, which can lead to inefficiencies and lost revenue.

The Bluestone Real Estate ML Platform provides data-driven predictions that support faster and more informed decision-making.

## Key Business Benefits
**1. Smarter Pricing Decisions**

The Sales Price Model predicts the likely final sale price of a property based on market conditions and buyer engagement signals.

**Business Impact**

- Helps agents price properties competitively

- Reduces the risk of overpricing, which can lead to long market times

- Prevents underpricing, which reduces seller profit

- Supports evidence-based negotiation strategies

Example use case:

A real estate agent can quickly estimate the expected sale price range before listing a property.

**2. Predicting Rental Demand**

The Rental Demand Model estimates the probability that a listing will be rented.

**Business Impact**

Identifies listings that may struggle to attract tenants

Allows agents to adjust pricing or marketing strategies early

Helps property managers prioritize high-demand listings

Example use case:

A property manager can identify which units may require pricing adjustments or promotional efforts.

**3. Optimizing Marketing and Lead Management**

The models incorporate customer inquiry engagement features, such as:

lead score

follow-up activity

response time

**Business Impact**

Helps teams understand which leads are most valuable

Encourages faster response times to increase conversions

Improves marketing ROI by targeting high-conversion opportunities

**4. Faster Decision Making**

Traditional property analysis requires manual comparison across multiple listings.

The ML system provides instant predictions via an API, enabling:

real-time property valuation

automated listing analysis

integration with real estate platforms

**Business Impact**

Reduces analysis time from hours to seconds

Enables automated insights across large portfolios

Supports scalable decision-making.

**Strategic Value for Real Estate Companies**

The platform enables organizations to transition from reactive decision-making to predictive analytics.

Key strategic advantages include:

Data-driven pricing strategies

Improved rental occupancy rates

Faster property turnover

Better customer engagement insights

Scalable analytics infrastructure


#### Example Business Workflow

A typical operational workflow with this system could look like this:

Property Listing Created
        │
        ▼
System Sends Listing Features to ML API
        │
        ▼
Rental Demand Prediction
        │
        ▼
Sales Price Prediction
        │
        ▼
Agent Dashboard Displays Insights
        │
        ▼
Agent Adjusts Pricing or Marketing Strategy

This allows agents to react quickly to market signals and optimize listing performance.


### Long-Term Business Potential

The deployed ML platform also creates opportunities for further innovation:

- Automated property valuation tools

- Real estate investment analysis

- AI-powered property recommendation systems

- market trend forecasting

As more data becomes available, the system can continuously improve through automated retraining pipelines.

### Summary

The Bluestone Real Estate ML Platform transforms raw property and inquiry data into actionable predictions that help real estate professionals:

price properties accurately

identify rental demand early

optimize marketing strategies

make faster, data-driven decisions

By deploying the models as a scalable API, the platform enables real-time analytics that can be integrated directly into real estate management systems.
