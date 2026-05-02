import pandas as pd
import numpy as np
import os

def create_dummy_data():
    os.makedirs("data/processed", exist_ok=True)
    
    # 30 columns as seen in the notebook/preprocessor logic
    cols = [
        "num__tenure", "num__MonthlyCharges", "num__TotalCharges", "num__Charges_per_Tenure",
        "cat__gender_Male", "cat__SeniorCitizen_1", "cat__Partner_Yes", "cat__Dependents_Yes",
        "cat__PhoneService_Yes", "cat__MultipleLines_No phone service", "cat__MultipleLines_Yes",
        "cat__InternetService_Fiber optic", "cat__InternetService_No",
        "cat__OnlineSecurity_No internet service", "cat__OnlineSecurity_Yes",
        "cat__OnlineBackup_No internet service", "cat__OnlineBackup_Yes",
        "cat__DeviceProtection_No internet service", "cat__DeviceProtection_Yes",
        "cat__TechSupport_No internet service", "cat__TechSupport_Yes",
        "cat__StreamingTV_No internet service", "cat__StreamingTV_Yes",
        "cat__StreamingMovies_No internet service", "cat__StreamingMovies_Yes",
        "cat__Contract_One year", "cat__Contract_Two year",
        "cat__PaperlessBilling_Yes", "cat__PaymentMethod_Credit card (automatic)",
        "cat__PaymentMethod_Electronic check", "cat__PaymentMethod_Mailed check"
    ]
    
    # Generate 100 rows
    data = np.random.randn(100, len(cols))
    df = pd.DataFrame(data, columns=cols)
    df["Churn"] = np.random.randint(0, 2, 100)
    
    df.to_csv("data/processed/train_processed.csv", index=False)
    df.to_csv("data/processed/test_processed.csv", index=False)
    print("Dummy data created successfully.")

if __name__ == "__main__":
    create_dummy_data()
