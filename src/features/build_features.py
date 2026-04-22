import pandas as pd
import numpy as np
import joblib
import os
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica as regras de limpeza baseadas na EDA e cria features sintéticas.
    """
    df = df.copy()
    
    # Tratar TotalCharges (Sanidade)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.dropna(subset=['TotalCharges'], inplace=True)
    
    # Remover IDs desnecessários
    if 'customerID' in df.columns:
        df.drop(columns=['customerID'], inplace=True)
        
    # Tratamento da variável Alvo
    if 'Churn' in df.columns and df['Churn'].dtype == 'object':
        df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
        
    # Feature Engineering
    if 'TotalCharges' in df.columns and 'tenure' in df.columns:
        # np.where para evitar que tenures = 0 gerem valores nulos/infinitos
        df['Charges_per_Tenure'] = np.where(df['tenure'] > 0, df['TotalCharges'] / df['tenure'], 0)
        
    return df

def preprocess_data(X_train: pd.DataFrame, X_test: pd.DataFrame, save_path: str = "models/preprocessor.pkl"):
    """
    Constrói e treina o ColumnTransformer (Pipeline) nos dados de treino.
    Aplica a transformação no treino e no teste.
    Salva o preprocessor ajustado via joblib.
    """
    # Identificar colunas pelas categorias
    num_features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'Charges_per_Tenure']
    cat_features = [col for col in X_train.columns if col not in num_features]
    
    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    cat_pipeline = Pipeline([
        ('ohe', OneHotEncoder(drop='first', handle_unknown='ignore', sparse_output=False))
    ])
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', num_pipeline, num_features),
            ('cat', cat_pipeline, cat_features)
        ],
        remainder='drop'
    )
    
    # Fit e Transform no TREINO
    X_train_processed_array = preprocessor.fit_transform(X_train)
    feature_names = preprocessor.get_feature_names_out()
    X_train_processed = pd.DataFrame(X_train_processed_array, columns=feature_names, index=X_train.index)
    
    # Transform apenas no TESTE (para evitar Data Leakage)
    X_test_processed_array = preprocessor.transform(X_test)
    X_test_processed = pd.DataFrame(X_test_processed_array, columns=feature_names, index=X_test.index)
    
    # Salvar o objeto Sklearn na pasta models
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    joblib.dump(preprocessor, save_path)
    
    return X_train_processed, X_test_processed, preprocessor
