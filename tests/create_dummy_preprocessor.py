import joblib
import os
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

def create_dummy_preprocessor():
    os.makedirs("models", exist_ok=True)
    
    # 30 dummy columns
    cols = [f"col_{i}" for i in range(30)]
    X = pd.DataFrame(np.random.randn(10, 30), columns=cols)
    
    # Simple preprocessor that just scales everything
    preprocessor = ColumnTransformer([
        ('scale', StandardScaler(), cols)
    ])
    preprocessor.fit(X)
    
    joblib.dump(preprocessor, "models/preprocessor.pkl")
    print("Dummy preprocessor created successfully.")

if __name__ == "__main__":
    create_dummy_preprocessor()
