import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import confusion_matrix, mean_absolute_error,mean_squared_error,r2_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.linear_model import LinearRegression

df = pd.read_csv("KC_House_Data.csv")
# The value we want to predict
target="price"
if target not in df.columns:
    raise ValueError(f"Expected a '{target}' column. Check csv column names.")
df=df.dropna(subset=target)
X=df.drop(columns=[target,'id','date'],errors='ignore')
y=df[target]

# Identify numeric and categorical columns
numeric_features=X.select_dtypes(include=np.number).columns.to_list()
categorical_features=X.select_dtypes(include=['object','category']).columns.tolist()


# Impute missing values and scale numeric features.
# One-hot encode categories; do not scale category labels.
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("one_hot", OneHotEncoder(handle_unknown="ignore")),
])

preprocessor = ColumnTransformer(transformers=[
    ("numeric", numeric_pipeline, numeric_features),
    ("categorical", categorical_pipeline, categorical_features),
])

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=42
)
price_cutoffs = np.quantile(y_train, [1 / 3, 2 / 3])
price_labels = ["Low", "Medium", "High"]
models={
    "Linear Regression":Pipeline([
        ('preprocessor',preprocessor),
        ('model',LinearRegression())
    ]),
    "KNN Regression":Pipeline([
        ('preprocessor',preprocessor),
        ("model",KNeighborsRegressor(n_neighbors=5,weights="distance")),
    ])
}
# Train, predict, and compare
scores={}

for name ,model in models.items():
    model.fit(X_train,y_train)
    predictions=model.predict(X_test)

    actual_classes = np.digitize(y_test, bins=price_cutoffs)
    predicted_classes = np.digitize(predictions, bins=price_cutoffs)
    matrix = confusion_matrix(actual_classes, predicted_classes, labels=[0, 1, 2])
    print(f"\n{name} price-category confusion matrix:")
    print(pd.DataFrame(matrix, index=price_labels, columns=price_labels))
    
    scores[name]={
        'MAE':mean_absolute_error(y_test,predictions),
        'RMSE':np.sqrt(mean_squared_error(y_test,predictions)),
        'R2':r2_score(y_test,predictions),
    }
results=pd.DataFrame(scores).T.sort_values('RMSE')
print(results.round(3))

rmse_difference = (
    scores["KNN Regression"]["RMSE"]
    - scores["Linear Regression"]["RMSE"]
)
print(f"\nRMSE difference (KNN - Linear Regression): ${rmse_difference:,.2f}")
print(f"Absolute RMSE gap: ${abs(rmse_difference):,.2f}")

if rmse_difference < 0:
    print("KNN has the lower RMSE on this test set.")
elif rmse_difference > 0:
    print("Linear Regression has the lower RMSE on this test set.")
else:
    print("Both models have the same RMSE on this test set.")