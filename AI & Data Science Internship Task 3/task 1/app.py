import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

st.set_page_config(page_title="Loan Default Prediction", layout="wide")

# Load files
model = joblib.load("best_model.pkl")
results = joblib.load("model_results.pkl")
feature_names = joblib.load("feature_names.pkl")
df = pd.read_csv("loan_default.csv")

st.title("Loan Default Prediction System")
st.write("Predict whether an applicant is likely to default on a loan.")

# Sidebar inputs
st.sidebar.header("Applicant Information")

age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=35)
annual_income = st.sidebar.number_input("Annual Income", min_value=0.0, value=50000.0)
loan_amount = st.sidebar.number_input("Loan Amount", min_value=0.0, value=20000.0)
employment_years = st.sidebar.number_input("Employment Years", min_value=0, max_value=50, value=5)
credit_score = st.sidebar.number_input("Credit Score", min_value=300, max_value=900, value=650)
existing_loans = st.sidebar.number_input("Existing Loans", min_value=0, max_value=20, value=1)

input_data = pd.DataFrame({
    "AGE": [age],
    "ANNUAL_INCOME": [annual_income],
    "LOAN_AMOUNT": [loan_amount],
    "EMPLOYMENT_YEARS": [employment_years],
    "CREDIT_SCORE": [credit_score],
    "EXISTING_LOANS": [existing_loans]
})

col1, col2 = st.columns(2)

with col1:
    st.subheader("Prediction")
    if st.button("Predict"):
        prediction = model.predict(input_data)[0]

        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(input_data)[0][1]
        else:
            probability = None

        if prediction == 1:
            st.error("Applicant is likely to default.")
        else:
            st.success("Applicant is not likely to default.")

        if probability is not None:
            st.write(f"Default Probability: {probability:.2%}")

with col2:
    st.subheader("Input Data")
    st.dataframe(input_data)

# Dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Model results
st.subheader("Model Accuracy Comparison")
results_df = pd.DataFrame(results, columns=["Model", "Accuracy"])
st.dataframe(results_df)

fig1, ax1 = plt.subplots()
ax1.bar(results_df["Model"], results_df["Accuracy"])
ax1.set_ylabel("Accuracy")
ax1.set_title("Model Accuracy Comparison")
st.pyplot(fig1)

# Feature importance
st.subheader("Feature Importance")

try:
    final_model = model.named_steps["model"]

    if hasattr(final_model, "feature_importances_"):
        importances = final_model.feature_importances_
        feat_imp = pd.DataFrame({
            "Feature": feature_names,
            "Importance": importances
        }).sort_values(by="Importance", ascending=False)

        fig2, ax2 = plt.subplots()
        ax2.barh(feat_imp["Feature"], feat_imp["Importance"])
        ax2.invert_yaxis()
        ax2.set_title("Feature Importance")
        st.pyplot(fig2)

    elif hasattr(final_model, "coef_"):
        importances = np.abs(final_model.coef_[0])
        feat_imp = pd.DataFrame({
            "Feature": feature_names,
            "Importance": importances
        }).sort_values(by="Importance", ascending=False)

        fig2, ax2 = plt.subplots()
        ax2.barh(feat_imp["Feature"], feat_imp["Importance"])
        ax2.invert_yaxis()
        ax2.set_title("Feature Importance")
        st.pyplot(fig2)

    else:
        st.info("Feature importance is not available for this model.")

except Exception as e:
    st.warning(f"Could not display feature importance: {e}")