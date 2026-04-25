import torch
import torch.nn as nn

class ChurnMLP(nn.Module):
    """
    Arquitetura de rede neural Multi-Layer Perceptron para previsão de Churn.
    Seguindo as especificações da Etapa 2:
    - Input Layer: 31 neurônios (baseado no train_processed.csv)
    - Hidden Layers: 16 e 8 neurônios com ativação ReLU
    - Dropout: 0.2 para regularização
    - Output Layer: 1 neurônio com saída linear (para BCEWithLogitsLoss)
    """
    def __init__(self, input_dim=31):
        super(ChurnMLP, self).__init__()
        
        self.network = nn.Sequential(
            # Primeira Camada Oculta
            nn.Linear(input_dim, 16),
            nn.ReLU(),
            nn.Dropout(0.2),
            
            # Segunda Camada Oculta
            nn.Linear(16, 8),
            nn.ReLU(),
            nn.Dropout(0.2),
            
            # Camada de Saída
            nn.Linear(8, 1)
        )
        
    def forward(self, x):
        return self.network(x)

if __name__ == "__main__":
    # Teste de sanidade do modelo
    model = ChurnMLP(input_dim=31)
    test_input = torch.randn(1, 31)
    output = model(test_input)
    
    print("Modelo ChurnMLP instanciado com sucesso.")
    print(f"Estrutura da rede:\n{model}")
    print(f"Input shape: {test_input.shape}")
    print(f"Output shape: {output.shape}")
