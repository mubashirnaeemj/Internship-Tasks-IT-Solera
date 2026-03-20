import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

try:
    from xgboost import XGBClassifier
    xgb_available = True
except ImportError:
    xgb_available = False


# Load dataset
df = pd.read_csv("loan_default.csv")

# Features and target
X = df.drop(columns=["TARGET", "SK_ID_CURR"], errors="ignore")
y = df["TARGET"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Models
models = {
    "Logistic Regression": Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000, random_state=42))
    ]),
    "Random Forest": Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("model", RandomForestClassifier(n_estimators=200, random_state=42))
    ]),
}

if xgb_available:
    models["XGBoost"] = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("model", XGBClassifier(
            eval_metric="logloss",
            random_state=42
        ))
    ])

best_model = None
best_name = None
best_accuracy = 0
results = []

for name, pipeline in models.items():
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    results.append((name, acc))
    print(f"{name}: {acc:.4f}")

    if acc > best_accuracy:
        best_accuracy = acc
        best_model = pipeline
        best_name = name

print("\nBest Model:", best_name)
print("Best Accuracy:", round(best_accuracy, 4))

# Final evaluation of best model
best_pred = best_model.predict(X_test)
print("\nClassification Report:")
print(classification_report(y_test, best_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, best_pred))

# Save artifacts
joblib.dump(best_model, "best_model.pkl")
joblib.dump(results, "model_results.pkl")
joblib.dump(list(X.columns), "feature_names.pkl")

print("\nSaved:")
print("- best_model.pkl")
print("- model_results.pkl")
print("- feature_names.pkl")