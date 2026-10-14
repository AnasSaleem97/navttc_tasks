# Task 52 - Logistic Regression with Scikit-Learn
# Reference: https://www.datacamp.com/community/tutorials/understanding-logistic-regression-python

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = {
    "study_hours": [1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9],
    "attendance":  [60, 65, 70, 72, 75, 78, 80, 85, 82, 88, 90, 92, 95, 96, 98, 99],
    "passed":      [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)
X = df[["study_hours", "attendance"]]
y = df["passed"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Actual labels:   ", list(y_test))
print("Predicted labels:", list(y_pred))

acc = accuracy_score(y_test, y_pred)
print(f"\nAccuracy Score for Abubakar's model: {acc * 100:.1f}%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))
