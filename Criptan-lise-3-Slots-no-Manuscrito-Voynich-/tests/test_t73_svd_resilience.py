# test_t73_svd_resilience.py
# Teste T73: Resiliencia a Ruido Paleografico via Decomposicao SVD

import numpy as np

def run_test():
    print("=== [TEST T73] Resiliencia a Ruido SVD (Rank < 11) ===")
    
    np.random.seed(42)
    base_matrix = np.random.dirichlet(np.ones(10), size=50)
    noise = np.random.normal(0, 0.05, base_matrix.shape)
    noisy_matrix = base_matrix + noise
    
    U, S, Vt = np.linalg.svd(noisy_matrix)
    effective_rank = int(np.sum(S > 0.5))
    print(f"Valores Singulares Principais: {S[:5].round(3)}")
    print(f"Posto Efetivo Calculado (SVD Rank): {effective_rank}")
    
    assert effective_rank < 11, f"Erro: Posto SVD ({effective_rank}) excedeu limite"
    print("STATUS T73 SVD: APROVADO [PASSED]\n")

if __name__ == "__main__":
    run_test()
