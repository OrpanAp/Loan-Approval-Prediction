import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load data
df = pd.read_csv("train_u6lujuX_CVtuZ9i.csv")

# Fill missing numeric values with median
num_cols = df.select_dtypes(include=["int64", "float64"]).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# Fill missing categorical values with mode (most common)
cat_cols = df.select_dtypes(include=["object", "string"]).columns
df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

# Remove extra spaces in column names
df.columns = df.columns.str.strip()

# Drop Loan_ID (not useful)
df = df.drop(columns=["Loan_ID"])

# Define target first
y = df["Loan_Status"].map({"Y": 1, "N": 0})

# Features
X = df.drop("Loan_Status", axis=1)

# Detect categorical & numeric columns
cat_cols = X.select_dtypes(include=["object", "string"]).columns
num_cols = X.select_dtypes(exclude=["object", "string"]).columns

# Preprocessing: one-hot encode categorical columns
preproc = ColumnTransformer([
    ("onehot", OneHotEncoder(handle_unknown="ignore"), cat_cols)
], remainder="passthrough")

# Split into train & test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Pipeline: preprocessing + logistic regression
model = Pipeline([
    ("preproc", preproc),
    ("clf", LogisticRegression(max_iter=1000))
])

# Train model
model.fit(X_train, y_train)

# Make predictions on test set
y_pred = model.predict(X_test)
print("Accuracy on test set:", accuracy_score(y_test, y_pred))

# Save model
joblib.dump(model, "loan_model.pkl")

print("✅ Model trained and saved as loan_model.pkl")