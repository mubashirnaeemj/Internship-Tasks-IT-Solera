import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Amazon Product Recommender", layout="wide")

# Load trained files
df = joblib.load("amazon_df.pkl")
cosine_sim = joblib.load("cosine_sim.pkl")

st.title("Amazon Product Recommendation System")
st.write("Select a product to get top 5 similar recommendations.")

# Product selection
product_list = df["product_name"].tolist()
selected_product = st.selectbox("Choose a product", product_list)

def recommend(product_name, top_n=5):
    idx = df.index[df["product_name"] == product_name][0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]  # skip itself

    recommendations = []
    for i, score in sim_scores:
        rec = {
            "product_name": df.iloc[i]["product_name"],
            "similarity_score": round(score, 2),
            "category": df.iloc[i]["category"],
            "discounted_price": df.iloc[i]["discounted_price"],
            "actual_price": df.iloc[i]["actual_price"],
            "rating": df.iloc[i]["rating"],
            "img_link": df.iloc[i]["img_link"],
            "product_link": df.iloc[i]["product_link"]
        }
        recommendations.append(rec)
    return recommendations

if st.button("Recommend"):
    recs = recommend(selected_product)
    for rec in recs:
        st.markdown(f"### {rec['product_name']}")
        st.image(rec["img_link"], width=150)
        st.write(f"**Category:** {rec['category']}")
        st.write(f"**Discounted Price:** {rec['discounted_price']}  |  **Actual Price:** {rec['actual_price']}")
        st.write(f"**Rating:** {rec['rating']}")
        st.write(f"**Similarity Score:** {rec['similarity_score']}")
        st.markdown(f"[View Product]({rec['product_link']})")
        st.markdown("---")