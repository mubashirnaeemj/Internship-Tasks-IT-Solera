import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib

# Load dataset
df = pd.read_csv("amazon.csv")

# Fill missing values with empty string
df["product_name"] = df["product_name"].fillna("")
df["category"] = df["category"].fillna("")
df["about_product"] = df["about_product"].fillna("")

# Combine features into a single string for each product
df["combined_features"] = df["product_name"] + " " + df["category"] + " " + df["about_product"]

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["combined_features"])

# Cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Save artifacts
joblib.dump(df, "amazon_df.pkl")
joblib.dump(cosine_sim, "cosine_sim.pkl")

print("Recommender training done. Files saved:")
print("- amazon_df.pkl")
print("- cosine_sim.pkl")