import os
import pandas as pd
from sklearn.model_selection import train_test_split
import sys

# Garante que o Python enxergue o pacote 'src' a partir do root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.utils.seed_config import set_seeds
from src.features.build_features import engineer_features, preprocess_data

def main():
    # 1. Aplicando semente para reprodutibilidade rigorosa
    set_seeds(42)
    
    # Resolvendo o path absoluto da raiz do projeto
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    
    raw_data_path = os.path.join(project_root, 'data', 'raw', 'WA_Fn-UseC_-Telco-Customer-Churn.csv')
    
    print(f"Carregando dados brutos de: {raw_data_path}...")
    try:
        df = pd.read_csv(raw_data_path)
    except FileNotFoundError:
        print(f"Arquivo não encontrado! Certifique-se de baixar o dataset em: {raw_data_path}")
        return
        
    print("Executando Feature Engineering e Sanidade de Tipos...")
    df_engineered = engineer_features(df)
    
    # Separando Features (X) e Target (y)
    X = df_engineered.drop(columns=['Churn'])
    y = df_engineered['Churn']
    
    print("Separando Treino e Teste (80/20)...")
    # Utilizamos stratify=y para garantir a mesma proporção de Churn em ambos os splits
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    print("Construindo Pipeline, Fit-Transform no Treino e Transform no Teste...")
    model_path = os.path.join(project_root, 'models', 'preprocessor.pkl')
    X_train_processed, X_test_processed, preprocessor = preprocess_data(X_train, X_test, save_path=model_path)
    
    # Reatribuindo o 'Churn' ao dataframe para salvar como CSVs fechados
    train_final = X_train_processed.copy()
    train_final['Churn'] = y_train.values
    
    test_final = X_test_processed.copy()
    test_final['Churn'] = y_test.values
    
    # Preparando as rotas de saída
    out_dir = os.path.join(project_root, 'data', 'processed')
    os.makedirs(out_dir, exist_ok=True)
    
    train_path = os.path.join(out_dir, 'train_processed.csv')
    test_path = os.path.join(out_dir, 'test_processed.csv')
    
    # Salvando em disco
    train_final.to_csv(train_path, index=False)
    test_final.to_csv(test_path, index=False)
    
    print("\n--- RESUMO DA EXTRAÇÃO E PRÉ-PROCESSAMENTO ---")
    print(f"Model Transformer salvo em: {model_path}")
    print(f"Base de Treino salva em: {train_path} | Shape: {train_final.shape}")
    print(f"Base de Teste salva em: {test_path} | Shape: {test_final.shape}")
    print("Processamento modular concluído com sucesso!")

if __name__ == "__main__":
    main()
