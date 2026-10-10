# PACOTE DE REPRODUÇÃO E DOCUMENTAÇÃO AUTÔNOMA
## Criptanálise do Autômato Estocástico de 3 Slots ($M_{\text{Cardan}}$) no Manuscrito Voynich

**Pesquisador Responsável:** Marcelo Aparecido Ferreira Junior  
**Contato:** 3eatcru@gmail.com  
**Licença:** Creative Commons Attribution 4.0 International (CC-BY-4.0)  
**Data:** Outubro de 2026  

---

### 🏛️ Estrutura do Pacote
```text
Pacote_Replicacao_Voynich_M_Cardan/
├── 01_DOCUMENTOS_ACADEMICOS/        <- Artigo v3 (DOCX), Cover Letter, Painel e Manual PDF
├── 02_DATASETS_E_FIXTURES/          <- CSVs de decomposição, adjacência e derivas do operador
├── 03_SCRIPTS_REPRODUCAO_E_AUDITORIA/<- Script em Python 3.12 e logs de auditoria T77
├── 04_DIAGRAMAS_E_GABARITOS/         <- Visualizações de esparsidade, entropia e gabarito da Volvelle
├── README.md                         <- Este guia de instruções
├── MANIFESTO_SUBMISSAO_ZENODO_DOI-v2.md <- Metadados de publicação e registros Zenodo
└── SHA256SUMS.txt                    <- Hashes de verificação criptográfica de integridade
```

---

### 💻 Como Executar a Verificação Autônoma

Para reproduzir e verificar as métricas estocásticas do autômato em qualquer sistema com Python 3.12:

```bash
cd 03_SCRIPTS_REPRODUCAO_E_AUDITORIA/
python3 reproduzir_testes_voynich.py
```

### 📊 Principais Métricas Auditadas

1. **Esparsidade Inter-Token (Teste T70):** **91,58%** de redução no espaço cartesiano ($S_3 \to S_1$).
2. **Estabilidade em 20 Quires (Teste LOQ / T72):** Esparsidade média de **92,07%**.
3. **Resiliência a Ruído Paleográfico (Teste T73):** Posto matricial **Rank SVD < 11** mantido sob 20% de ruído.
4. **Economia de Compressão MDL (Portão G4):** Redução de **99.304,5 bits (34,85%)** em relação a modelos linguísticos.
5. **Governança Semântica (Portão G6):** Restrição estrita à arquitetura gerativa e proibição de traduções lexicais não fundamentadas.
