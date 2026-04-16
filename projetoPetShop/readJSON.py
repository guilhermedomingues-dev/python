import json

path = r'H:\python\projetoPetShop\dados.json'

def read_json():
    with open(path, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        return dados

def save_json(path, dados):
    with open(path, "w") as dados:
        return json.dump(path, dados)