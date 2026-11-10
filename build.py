"""Monta index.html do cardápio a partir de 02 ORGANIZADO/cardapio.json.
Uso: python3 build.py   (depois: git add -A && git commit && push)"""
import json, pathlib

AQUI = pathlib.Path(__file__).parent
dados = json.loads((AQUI.parent.parent / "02 ORGANIZADO" / "cardapio.json").read_text())
dados.pop("_nota", None)
for c in dados["categorias"]:
    for i in c["itens"]:
        i.pop("confirmar", None)   # marcação interna, não vai para o site
html = (AQUI / "template.html").read_text().replace("/*DADOS*/null", json.dumps(dados, ensure_ascii=False))
(AQUI / "index.html").write_text(html)
print("index.html ok,", sum(len(c["itens"]) for c in dados["categorias"]), "itens")
