import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
import os

class ChurnDataset(Dataset):
    """
    Dataset customizado para carregar os dados de Churn Telco pré-processados.
    """
    def __init__(self, csv_path):
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {csv_path}")
            
        data = pd.read_csv(csv_path)
        
        # Separando features e target
        # Assume-se que a coluna alvo é 'Churn'
        if 'Churn' not in data.columns:
            raise ValueError(f"A coluna 'Churn' não foi encontrada no arquivo {csv_path}")
            
        self.X = torch.tensor(data.drop('Churn', axis=1).values, dtype=torch.float32)
        self.y = torch.tensor(data['Churn'].values, dtype=torch.float32).unsqueeze(1)
        
    def __len__(self):
        return len(self.y)
        
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

def get_dataloader(csv_path, batch_size=32, shuffle=True):
    """
    Retorna um DataLoader para o dataset de Churn.
    """
    dataset = ChurnDataset(csv_path)
    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)

if __name__ == "__main__":
    # Teste rápido de carregamento
    train_path = "data/processed/train_processed.csv"
    if os.path.exists(train_path):
        ds = ChurnDataset(train_path)
        print(f"Dataset carregado com {len(ds)} amostras.")
        print(f"Shape das features: {ds.X.shape}")
        print(f"Shape do target: {ds.y.shape}")
    else:
        print(f"Arquivo de treino não encontrado em: {train_path}")
