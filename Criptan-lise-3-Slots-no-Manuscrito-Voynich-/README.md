# Suite de Testes Criptanaliticos do Automato Estocastico M_Cardan

**Autor:** Marcelo Aparecido Ferreira Junior  
**DOI Zenodo:** 10.5281/zenodo.23287068  
**Licenca:** Creative Commons Attribution 4.0 International (CC-BY-4.0)

---

## Descricao do Pacote

Este repositorio contem a suite completa de codigos de teste em Python 3 e datasets CSV de validacao empirica para a verificacao do modelo **M_Cardan (Automato Estocastico de 3 Slots)** no Manuscrito Voynich.

A arquitetura de testes audita as propriedades fisico-mecanicas do codice sob a governanca dos **Portoes G1 a G6**:

* **test_t70_sparsity.py**: Teste T70 — Medicao da esparsidade da matriz de transicao inter-token (S3 -> S1, 91.58% de esparsidade).
* **test_t72_loq_20_quires.py**: Teste T72 / LOQ — Estabilidade e validacao cruzada 5-fold nos 20 quires do manuscrito (media global de 92.07%).
* **test_t73_svd_resilience.py**: Teste T73 — Decomposicao em Valores Singulares sob ruido paleografico de transcricao (Rank SVD < 11).
* **test_t74_currier_ab.py**: Teste T74 — Avaliacao da mecanicidade e presets entre Currier A e Currier B (98.1% de identidade no Slot S2).
* **test_t75a_f1v_decomposer.py**: Teste T75-A — Execucao do parser morfologico congelado de 3 slots nos tokens do folio f1v.
* **test_g4_mdl_compression.py**: Teste Portao G4 — Calculo da parcimonia e economia de descricao MDL (economia de 99.304,5 bits em relacao a lingua natural).
* **test_botanical_cooccurrence.py**: Teste de associacao estatistica dos glifos do Slot S2 com os organos vegetais da Botanica Quimerica.

---

## Como Executar

```bash
python3 run_all_tests.py
```
