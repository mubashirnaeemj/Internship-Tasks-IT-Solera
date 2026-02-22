# ITSOLERA PVT LTD - AI & Data Science Internship Tasks (Advanced)

## Overview
This repository contains the **completed advanced tasks** for the AI & Data Science Internship at **ITSOLERA PVT LTD**.  
These tasks focus on developing advanced data science skills, including classification, clustering, time series forecasting, explainable AI (XAI), and business intelligence, using Python libraries such as NumPy, pandas, scikit-learn, XGBoost, SHAP, Prophet, matplotlib, seaborn, and Streamlit.

**Due Date:** 20th February 2026  
**Intern Name:** Mubashir Naeem Janjua  

---

## Task 1: Term Deposit Subscription Prediction (Bank Marketing)
**Objective:**  
Predict whether a bank customer will subscribe to a term deposit as a result of a marketing campaign.

**Dataset:**  
Bank Marketing Dataset (UCI Machine Learning Repository)

**Approach:**  
- Loaded and explored dataset using pandas  
- Encoded all categorical features properly  
- Trained classification models (Logistic Regression, Random Forest)  
- Evaluated models using Confusion Matrix, F1-Score, and ROC Curve  
- Applied SHAP to explain at least 5 model predictions

**Results & Insights:**  
- Classification models achieved strong predictive performance  
- Key features impacting subscription: campaign contact, age, balance  
- SHAP analysis provided explainable insights for customer behavior

---

## Task 2: Customer Segmentation Using Unsupervised Learning
**Objective:**  
Cluster customers based on spending habits and propose marketing strategies tailored to each segment.

**Dataset:**  
Mall Customers Dataset

**Approach:**  
- Conducted Exploratory Data Analysis (EDA)  
- Applied K-Means Clustering to segment customers  
- Visualized clusters using PCA/t-SNE  
- Proposed marketing strategies for each segment

**Results & Insights:**  
- Identified distinct customer segments based on spending patterns  
- Segmentation allows targeted marketing strategies  
- Clusters visualized clearly in 2D space using PCA/t-SNE

---

## Task 3: Energy Consumption Time Series Forecasting
**Objective:**  
Forecast short-term household energy usage using historical patterns.

**Dataset:**  
Household Power Consumption Dataset

**Approach:**  
- Parsed and resampled the time series data  
- Engineered time-based features (hour of day, weekday/weekend)  
- Compared ARIMA, Prophet, and XGBoost models  
- Plotted actual vs. forecasted energy usage

**Results & Insights:**  
- XGBoost and Prophet provided accurate short-term forecasts  
- Hourly and daily patterns significantly influenced energy consumption  
- Visualizations helped understand temporal trends

---

## Task 4: Loan Default Risk with Business Cost Optimization
**Objective:**  
Predict the likelihood of a loan default and optimize the decision threshold based on cost-benefit analysis.

**Dataset:**  
Home Credit Default Risk Dataset

**Approach:**  
- Cleaned and preprocessed the dataset  
- Trained Logistic Regression and CatBoost models  
- Defined business costs for false positives and negatives  
- Adjusted model thresholds to minimize total business cost

**Results & Insights:**  
- Models accurately predicted high-risk applicants  
- Income, past payment behavior, and loan amount were key features  
- Optimized thresholds reduced expected financial losses

---

## Task 5: Interactive Business Dashboard in Streamlit
**Objective:**  
Develop an interactive dashboard for analyzing sales, profit, and segment-wise performance.

**Dataset:**  
Global Superstore Dataset

**Approach:**  
- Cleaned and prepared dataset  
- Built Streamlit dashboard with filters (Region, Category, Sub-Category)  
- Displayed KPIs including Total Sales, Profit, and Top 5 Customers  
- Created interactive charts for visual insights

**Results & Insights:**  
- Dashboard allows real-time exploration of business performance  
- Visual KPIs helped identify top-performing regions, categories, and customers  
- Supports data-driven decision-making for business stakeholders

---

## ⚠️ Removed Large Files

Some datasets were too large (>100MB) for GitHub. These files were **removed from the repository**:

- `AI & Data Science Internship Task 2/Task 03/household_power_consumption.txt` (124 MB)  
- `AI & Data Science Internship Task 2/Task 04/application_train.csv` (158 MB)  

**Note:** These datasets can be downloaded from the original sources if needed.

---

## Submission Guidelines

Each task notebook includes:  
- Problem statement and objective  
- Dataset description and loading  
- Data cleaning & preprocessing  
- Exploratory Data Analysis (EDA) with graphs  
- Model training and testing  
- Evaluation metrics (accuracy, F1-score, MAE, RMSE where applicable)  
- Final conclusion and key insights  

**Code Quality:** Clean, well-structured, and commented for readability  

**GitHub Repository:** [https://github.com/mubashirnaeemj/Internship-Tasks-IT-Solera](https://github.com/mubashirnaeemj/Internship-Tasks-IT-Solera)

---

## Notes

- At least 4 out of 5 tasks are required for internship completion  
- Presentation of each task (10–15 minutes) is required  
- Prepare explanations for code, plots, and model results for presentations  

**Prepared by:** Mubashir Naeem Janjua  
**Internship:** ITSOLERA PVT LTD – AI & Data Science Internship  
**Date:** 20th February 2026
