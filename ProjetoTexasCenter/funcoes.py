import readJSON
import os

estoque = readJSON.read_json() 

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def produtos():

    indice = 1
    print("=====PRODUTOS=====")
    for produto in estoque["produtos"]:
        print(indice,"-",produto["nome"])
        indice+=1
             
    opcao = int(input("\n Qual produto deseja ver?: "))
    limpar()

    if 1 <= opcao <= len(estoque["produtos"]):
        produto = estoque["produtos"][opcao - 1]
        print("=====", produto["nome"], "=====")
        print("Marca:", produto["marca"])
        print("Gênero:", produto["genero"])
        print("Tamanhos:", produto["tamanhos_disponiveis"])
        print("Cores:", produto["cores"])
        if produto["estoque"]>=1:
            print("Estoque: Disponível(", produto["estoque"],"un.)")
        else:
            print("Estoque: Indisponível")
        print("Preço: R$", produto["preco_original"])
        
        opcao= str(input("\nDeseja comprar?(S/N): ")).capitalize()
        limpar()
        if opcao=="S":
            comprar(produto)

    else:
        print("=====TEXAS CENTER=====")
        print("Opção inválida.")

def masculino():
    print("=====MASCULINO=====")
    indice = 1

    masculinos = []

    for p in estoque["produtos"]:
        if p["genero"] in ("Masculino", "Unissex"):
            masculinos.append(p)
    
    for indice, produto in enumerate(masculinos, start=1):
        print(indice, "-", produto["nome"])
                
    opcao = int(input("\nQual produto deseja ver?: "))
    limpar()
                
    if 1 <= opcao <= len(masculinos):
        produto = masculinos[opcao - 1]
        print("=====", produto["nome"], "=====")
        print("Marca:", produto["marca"])
        print("Gênero:", produto["genero"])
        print("Tamanhos:", produto["tamanhos_disponiveis"])
        print("Cores:", produto["cores"])
        if produto["estoque"] >= 1:
            print("Estoque: Disponível (", produto["estoque"], "un.)")
        else:
            print("Estoque: Indisponível")
            print("Preço: R$", produto["preco_original"])
    else:
        print("=====TEXAS CENTER=====")
        print("Opção inválida.")

def feminino():
    print("=====FEMININO=====")
    indice = 1
                
    femininos = []

    for p in estoque["produtos"]:
        if p["genero"] in ("Feminino", "Unissex"):
            femininos.append(p)
    
    for indice, produto in enumerate(femininos, start=1):
            print(indice, "-", produto["nome"])
                
    opcao = int(input("\nQual produto deseja ver?: "))
    limpar()
                
    if 1 <= opcao <= len(femininos):
        produto = femininos[opcao - 1]
        print("=====", produto["nome"], "=====")
        print("Marca:", produto["marca"])
        print("Gênero:", produto["genero"])
        print("Tamanhos:", produto["tamanhos_disponiveis"])
        print("Cores:", produto["cores"])
        if produto["estoque"] >= 1:
            print("Estoque: Disponível (", produto["estoque"], "un.)")
        else:
            print("Estoque: Indisponível")
            print("Preço: R$", produto["preco_original"])
    else:
        print("=====TEXAS CENTER=====")
        print("Opção inválida.")

def marcas():
    print("=====MARCAS=====")
    indice = 1
    for marca in estoque["marcas"]:
        print(indice,"-", marca)
        indice+=1

def comprar(produto):
    preco=[]
    print("=====COMPRAR=====")
    if produto["estoque"]>=1:
        print("Produto: ",produto["nome"])
        print("Preço: R$", produto["preco_original"])
        quantidade = int(input("Quantidade desejada: "))
        while quantidade > produto["estoque"]:
            limpar()
            print("=====COMPRAR=====")
            if produto["estoque"]>=1:
                print("Produto: ",produto["nome"])
                print("Preço: R$", produto["preco_original"])
                print("Quantidade indisponível no estoque! Tente outra quantidade.")
                quantidade = int(input("Quantidade desejada: "))

        preco=produto["preco_original"]*quantidade
        print("==========")
        print("Final compra: R$", preco)
        print("1- Débito")
        print("2- Crétido")
        print("3- PIX")
    

