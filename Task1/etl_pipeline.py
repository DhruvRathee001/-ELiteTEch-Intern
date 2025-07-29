import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

# === EXTRACT ===
print("📤 Extracting data...")
df = pd.read_csv("titanic.csv")
print("Initial shape:", df.shape)

# Drop unnecessary columns
df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])

# Separate features and label
X = df.drop("Survived", axis=1)
y = df["Survived"]

# Identify column types
numeric_cols = X.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = X.select_dtypes(include=['object']).columns

# Numeric pipeline: Impute missing values, then scale
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])

# Apply numeric pipeline
X[numeric_cols] = numeric_pipeline.fit_transform(X[numeric_cols])

# Encode categorical columns manually
for col in categorical_cols:
    X[col] = X[col].fillna(X[col].mode()[0])
    X[col] = LabelEncoder().fit_transform(X[col])

# Final transformed data
processed_df = pd.concat([X, y], axis=1)

# === LOAD ===
processed_df.to_csv("processed_titanic.csv", index=False)
print("✅ ETL complete. Processed file saved.")
