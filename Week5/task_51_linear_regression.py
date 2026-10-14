# Task 51 - Linear Regression with Scikit-Learn
# Reference: https://stackabuse.com/linear-regression-in-python-with-scikit-learn/

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

hours = [1.5, 2.0, 2.5, 3.2, 4.0, 5.1, 5.5, 6.2, 7.0, 7.8, 8.3, 9.0]
scores = [40, 48, 52, 60, 62, 72, 75, 82, 85, 90, 93, 98]

data = pd.DataFrame({"Hours": hours, "Score": scores})
X = data[["Hours"]]
y = data["Score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print("Intercept:", round(model.intercept_, 2))
print("Slope (Coefficient):", round(model.coef_[0], 2))

y_pred = model.predict(X_test)
comparison = pd.DataFrame({"Actual": y_test, "Predicted": np.round(y_pred, 1)})
print("\nAbubakar's Test Predictions:\n", comparison)

print("\nMean Absolute Error:", round(metrics.mean_absolute_error(y_test, y_pred), 2))
print("Mean Squared Error:", round(metrics.mean_squared_error(y_test, y_pred), 2))
print("R-squared Score:", round(metrics.r2_score(y_test, y_pred), 3))
