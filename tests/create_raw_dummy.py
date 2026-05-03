import os

import numpy as np
import pandas as pd


def create_raw_dummy():
    os.makedirs("data/raw", exist_ok=True)

    rows = 100
    data = {
        "customerID": [f"ID-{i}" for i in range(rows)],
        "gender": np.random.choice(["Male", "Female"], rows),
        "SeniorCitizen": np.random.choice([0, 1], rows),
        "Partner": np.random.choice(["Yes", "No"], rows),
        "Dependents": np.random.choice(["Yes", "No"], rows),
        "tenure": np.random.randint(1, 72, rows),
        "PhoneService": np.random.choice(["Yes", "No"], rows),
        "MultipleLines": np.random.choice(["Yes", "No", "No phone service"], rows),
        "InternetService": np.random.choice(["DSL", "Fiber optic", "No"], rows),
        "OnlineSecurity": np.random.choice(["Yes", "No", "No internet service"], rows),
        "OnlineBackup": np.random.choice(["Yes", "No", "No internet service"], rows),
        "DeviceProtection": np.random.choice(["Yes", "No", "No internet service"], rows),
        "TechSupport": np.random.choice(["Yes", "No", "No internet service"], rows),
        "StreamingTV": np.random.choice(["Yes", "No", "No internet service"], rows),
        "StreamingMovies": np.random.choice(["Yes", "No", "No internet service"], rows),
        "Contract": np.random.choice(["Month-to-month", "One year", "Two year"], rows),
        "PaperlessBilling": np.random.choice(["Yes", "No"], rows),
        "PaymentMethod": np.random.choice(["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"], rows),
        "MonthlyCharges": np.random.uniform(18.0, 118.0, rows),
        "TotalCharges": [str(x) for x in np.random.uniform(18.0, 8000.0, rows)],
        "Churn": np.random.choice(["Yes", "No"], rows)
    }

    df = pd.DataFrame(data)
    df.to_csv("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv", index=False)
    print("Raw dummy data created successfully.")

if __name__ == "__main__":
    create_raw_dummy()
