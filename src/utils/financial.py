import numpy as np


def optimize_financial_threshold(
    y_true,
    y_proba,
    cost_fn: float = 500.0,
    cost_fp: float = 50.0,
    n_thresholds: int = 50,
):
    """
    Calcula o threshold de probabilidade que minimiza o prejuízo esperado
    em (custo_FN * #FN + custo_FP * #FP).

    Retorna (optimal_threshold, min_financial_loss).
    """
    y_true = np.asarray(y_true).reshape(-1)
    y_proba = np.asarray(y_proba).reshape(-1)

    thresholds = np.linspace(0.1, 0.9, n_thresholds)
    losses = []
    for t in thresholds:
        y_hat = (y_proba >= t).astype(int)
        fp = int(np.sum((y_hat == 1) & (y_true == 0)))
        fn = int(np.sum((y_hat == 0) & (y_true == 1)))
        losses.append(fn * cost_fn + fp * cost_fp)

    best_idx = int(np.argmin(losses))
    return float(thresholds[best_idx]), float(losses[best_idx])
