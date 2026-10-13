# run_all_tests.py
# Executador da Suite Completa de Testes de Criptanalise Voynich (Modelo M_Cardan)

import time
from tests import (
    test_t70_sparsity,
    test_t72_loq_20_quires,
    test_t73_svd_resilience,
    test_t74_currier_ab,
    test_t75a_f1v_decomposer,
    test_g4_mdl_compression,
    test_botanical_cooccurrence
)

def run_suite():
    print("=" * 70)
    print("SUITE DE TESTES E AUDITORIA - AUTOMATO ESTOCASTICO M_CARDAN")
    print("Autor: Marcelo Aparecido Ferreira Junior")
    print("DOI Zenodo: 10.5281/zenodo.23287068")
    print("=" * 70 + "\n")
    
    start_time = time.time()
    
    test_modules = [
        test_t70_sparsity,
        test_t72_loq_20_quires,
        test_t73_svd_resilience,
        test_t74_currier_ab,
        test_t75a_f1v_decomposer,
        test_g4_mdl_compression,
        test_botanical_cooccurrence
    ]
    
    passed = 0
    failed = 0
    
    for mod in test_modules:
        try:
            mod.run_test()
            passed += 1
        except Exception as e:
            print(f"FALHA NO TESTE {mod.__name__}: {e}\n")
            failed += 1
            
    elapsed = time.time() - start_time
    print("=" * 70)
    print(f"RESUMO DA EXECUCAO DA SUITE:")
    print(f"Total de Testes Executados: {len(test_modules)}")
    print(f"Aprovados [PASSED]: {passed}")
    print(f"Reprovados [FAILED]: {failed}")
    print(f"Tempo Total: {elapsed:.3f} segundos")
    print("=" * 70)

if __name__ == "__main__":
    run_suite()
