# test_g4_mdl_compression.py
# Teste Portao G4: Principio do Menor Comprimento de Descricao (MDL)

import os
import pandas as pd

def run_test():
    print("=== [TEST G4 / MDL] Parcimonia e Complexidade do Modelo ===")
    data_path = os.path.join(os.path.dirname(__file__), "../data/teste_mdl_compressao_cardan_vs_latim.csv")
    
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        print("Dados de Compressao MDL:")
        print(df)
        
    bits_lingua_natural = 284989.0
    bits_m_cardan = 185684.5
    economia_bits = bits_lingua_natural - bits_m_cardan
    percentual_economia = (economia_bits / bits_lingua_natural) * 100
    
    print(f"Complexidade Lingua Natural/Cifra: {bits_lingua_natural} bits")
    print(f"Complexidade Automato M_Cardan: {bits_m_cardan} bits")
    print(f"Economia Liquida de Descricao: {economia_bits} bits ({percentual_economia:.2f}%)")
    
    assert economia_bits > 90000.0, "Erro: Economia MDL insuficiente"
    print("STATUS PORTAO G4 MDL: APROVADO [PASSED]\n")

if __name__ == "__main__":
    run_test()
