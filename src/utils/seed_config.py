import os
import random

import numpy as np


def set_seeds(seed: int = 42):
    """
    Define a seed para reprodutibilidade nas principais bibliotecas matemáticas e de Machine Learning.
    Isso garante que os treinamentos da Rede Neural e os splits do Pandas gerem os mesmos resultados sempre.
    """
    # Python built-in random
    random.seed(seed)

    # Numpy
    np.random.seed(seed)

    # Variável de ambiente OS
    os.environ['PYTHONHASHSEED'] = str(seed)

    # PyTorch (tratamento de exceção caso o Torch não esteja instalado na máquina local ainda)
    try:
        import torch
        torch.manual_seed(seed)
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed) # Para suporte multi-GPU
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    except ImportError:
        pass
