# ITSOLERA PVT LTD - AI & Data Science Internship Tasks

## Overview
This repository contains the completed tasks for the AI & Data Science Internship at ITSOLERA PVT LTD.  
The internship tasks focus on developing core data science skills including data exploration, visualization, model building, and performance evaluation using Python libraries such as NumPy, pandas, matplotlib, seaborn, and scikit-learn.

**Due Date:** 20th Jan 2026  
**Intern Name:** Mubashir Naeem Janjua 

---

## Task 1: Data Handling with NumPy & Pandas (Foundations)

**Objective:**  
Build a strong foundation in data loading, cleaning, and manipulation using NumPy and pandas.

**Dataset:**  
Any structured CSV dataset (e.g., Iris, Sales, Student Performance)

**Approach:**  
- Loaded dataset using pandas  
- Inspected dataset using `.shape`, `.info()`, `.columns`, and `.head()`  
- Performed data cleaning: handled missing values and removed duplicates  
- Applied NumPy for array operations and basic statistics (mean, median, std)

**Results & Insights:**  
- Dataset was cleaned and structured  
- Calculated descriptive statistics provided insights into data distribution  
- Data ready for further analysis and modeling  

---

## Task 2: Exploring and Visualizing a Simple Dataset

**Objective:**  
Understand how to read, summarize, and visualize a dataset.

**Dataset:**  
Iris Dataset (CSV format)

**Approach:**  
- Loaded dataset using pandas  
- Displayed dataset structure with `.shape`, `.columns`, `.head()`  
- Performed visualizations using matplotlib and seaborn:  
  - Scatter plots to analyze relationships  
  - Histograms to examine data distribution  
  - Box plots to detect outliers

**Results & Insights:**  
- Visualizations revealed relationships between flower species and measurements  
- Detected outliers and variations in the dataset  
- Prepared data for potential classification modeling  

---

## Task 3: Predicting Insurance Claim Amounts

**Objective:**  
Estimate medical insurance claim amounts based on personal data.

**Dataset:**  
Medical Cost Personal Dataset

**Approach:**  
- Trained a Linear Regression model to predict charges  
- Visualized relationships between BMI, age, smoking status, and insurance charges  
- Evaluated model performance using MAE and RMSE

**Results & Insights:**  
- Smoking status and BMI significantly impact insurance charges  
- Linear regression provided a baseline for claim estimation  
- Visualizations helped identify key factors influencing charges  

---

## Task 4: Credit Risk Prediction

**Objective:**  
Predict whether a loan applicant is likely to default.

**Dataset:**  
Loan Prediction Dataset (Kaggle)

**Approach:**  
- Handled missing data and cleaned dataset  
- Visualized key features such as loan amount, income, and education  
- Trained classification models (Logistic Regression and Decision Tree)  
- Evaluated performance using accuracy and confusion matrix

**Results & Insights:**  
- Income and education were significant predictors of credit risk  
- Model accurately classified high-risk vs low-risk applicants  
- Insights can be used for informed lending decisions  

---

## Task 5: Customer Churn Prediction (Bank Customers)

**Objective:**  
Identify customers who are likely to leave the bank.

**Dataset:**  
Churn Modelling Dataset

**Approach:**  
- Cleaned and prepared the dataset  
- Encoded categorical features (Gender: Label Encoding, Geography: One-Hot Encoding)  
- Scaled numerical features  
- Trained an ANN model using Scikit-learn’s `MLPClassifier`  
- Evaluated model performance using accuracy and confusion matrix  
- Analyzed feature importance using permutation importance

**Results & Insights:**  
- Model Accuracy: ~86%  
- Key features influencing churn: Balance, CreditScore, Tenure, Geography, Age  
- Customers with low balances, low credit scores, or short tenure are most likely to churn  
- Insights can guide targeted retention campaigns

---

## Submission Guidelines

- Each task notebook includes:  
  - Introduction and problem statement  
  - Dataset description  
  - Data cleaning & preparation  
  - Exploratory Data Analysis (EDA) with graphs  
  - Model training and testing  
  - Evaluation metrics (accuracy, confusion matrix, MAE, RMSE where applicable)  
  - Conclusion summarizing key insights  

- Code is **clean, well-commented, and structured** for clarity

- GitHub Repository: https://github.com/mubashirnaeemj/Internship-Tasks-IT-Solera

- All tasks are ready for **Google Classroom submission**, along with notebooks, plots, and README.

---

## Notes

- At least 4 out of 5 tasks are required to receive credit  
- Presentation of tasks is required (10-15 minutes each)  
- Ensure explanations for code, plots, and model results are prepared for the presentation  

---

**Prepared by:** Mubashir Naeem Janjua 
**Internship:** ITSOLERA PVT LTD AI & Data Science Internship  
**Date:** 20th Jan 2026
