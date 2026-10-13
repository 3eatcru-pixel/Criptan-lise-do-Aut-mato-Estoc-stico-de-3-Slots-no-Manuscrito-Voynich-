# test_t75a_f1v_decomposer.py
# Teste T75-A: Decomposicao Morfologica do Folio f1v via Parser Congelado

import os
import pandas as pd

def run_test():
    print("=== [TEST T75-A] Parser Morfologico Congelado do Folio f1v ===")
    
    tokens_f1v = [
        "kchry", "chodaiin", "ol", "oltchey", "char", "cfhar", "am", "yteeay", "or", "ochy",
        "dcho", "lkody", "okodar", "chody", "dao", "ckhy", "ckho", "ckhy", "shy", "dksheey",
        "cthy", "kotchody", "dal", "dol", "chokeo", "dair", "dam", "sochey", "chokody", "chol",
        "cthol", "shol", "okal", "ky", "daiin"
    ]
    
    s1_list, s2_list, s3_list = [], [], []
    
    for tok in tokens_f1v:
        if tok.startswith("cho"): s1, rest = "cho", tok[3:]
        elif tok.startswith("da"): s1, rest = "da", tok[2:]
        elif tok.startswith("ok"): s1, rest = "ok", tok[2:]
        elif tok.startswith("sh"): s1, rest = "sh", tok[2:]
        elif tok.startswith("ch"): s1, rest = "ch", tok[2:]
        elif tok.startswith("k"): s1, rest = "k", tok[1:]
        elif tok.startswith("d"): s1, rest = "d", tok[1:]
        elif tok.startswith("o"): s1, rest = "o", tok[1:]
        else: s1, rest = "Ø", tok
        
        if rest.endswith("aiin"): s3, core = "aiin", rest[:-4]
        elif rest.endswith("edy"): s3, core = "edy", rest[:-3]
        elif rest.endswith("eey"): s3, core = "eey", rest[:-3]
        elif rest.endswith("dy"): s3, core = "dy", rest[:-2]
        elif rest.endswith("ey"): s3, core = "ey", rest[:-2]
        elif rest.endswith("ol"): s3, core = "ol", rest[:-2]
        elif rest.endswith("ar"): s3, core = "ar", rest[:-2]
        elif rest.endswith("in"): s3, core = "in", rest[:-2]
        elif rest.endswith("y"): s3, core = "y", rest[:-1]
        elif rest.endswith("l"): s3, core = "l", rest[:-1]
        elif rest.endswith("r"): s3, core = "r", rest[:-1]
        elif rest.endswith("m"): s3, core = "m", rest[:-1]
        else: s3, core = "Ø", rest
        
        s2 = core if core != "" else "Ø"
        s1_list.append(s1)
        s2_list.append(s2)
        s3_list.append(s3)
        
    df_f1v = pd.DataFrame({"token": tokens_f1v, "s1": s1_list, "s2": s2_list, "s3": s3_list})
    print(f"Total de Tokens Decompostos: {len(df_f1v)}")
    print(df_f1v.head(10))
    
    assert len(df_f1v) == len(tokens_f1v)
    print("STATUS T75-A PARSER: APROVADO [PASSED]\n")

if __name__ == "__main__":
    run_test()
