import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score


# Load dataset
data = pd.read_csv("dataset/placement.csv")


print("Dataset loaded successfully")
print(data.head())


# Convert branch text into numbers

encoder = LabelEncoder()

data["branch"] = encoder.fit_transform(data["branch"])


# Split input and output

X = data.drop("placed", axis=1)

y = data["placed"]


# Train and test split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train model

model.fit(X_train, y_train)


# Prediction

y_pred = model.predict(X_test)


# Accuracy

accuracy = accuracy_score(y_test, y_pred)


print("Model Accuracy:", accuracy)
# Save trained model

joblib.dump(model, "placement_model.pkl")

print("Model saved successfully")