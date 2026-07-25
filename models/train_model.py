import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load the dataset
df = pd.read_csv("../data/time_series_covid19_confirmed_global.csv")

# Prepare the data
date_data = df.iloc[:, 4:]
total_cases = date_data.sum()

prediction_df = pd.DataFrame({
    "Day": range(len(total_cases)),
    "Cases": total_cases.values
})

# Split into features and target
X = prediction_df[["Day"]]
y = prediction_df["Cases"]

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the trained model
joblib.dump(model, "outbreak_model.pkl")

print("Model trained and saved successfully!")