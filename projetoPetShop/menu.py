import readJSON

dados = readJSON.read_json()
raca = list(dados.keys())
peso = list(dados.values())
banho = 80
totalBanho = 0
valorPix = 0


def meun():

    print("\n=====Bicho Chique=====")
    print("1-", raca[0])
    print("2-", raca[1])
    print("3-", raca[2])
    print("4-", raca[3])
    print("5-", raca[4])
    print("6-", raca[5])
    print("7- Sair")

    opcao = int(input("\nQual a raça do seu cahcoro?: "))

    if opcao == 1:
        totalBanho = banho * peso[0]
        
        print("\n===============================")
        print("Valor total para banho: R$", totalBanho)
        print("===============================")
        print("Como deseja pagar?")
        print("1- Crédito")
        print("2- Débito")
        print("3- Pix (-5%)")
        opcaoPag = int(input("Como deseja pagar?: "))

        if opcaoPag == 1:
            print("\n===============================")
            print("R$", totalBanho, "pago com sucesso!")
            print("===============================")
        elif opcaoPag == 2:
            print("\n===============================")
            print("R$", totalBanho, "pago com sucesso!")
            print("===============================")
        elif opcaoPag == 3:
            print("\n===============================")
            valorPix = totalBanho * 0.95
            print("R$", valorPix, "pago com sucesso!")
            print("===============================")
    elif opcao == 2:
        totalBanho = banho * peso[1]
        
        print("\n===============================")
        print("Valor total para banho: R$", totalBanho)
        print("===============================")
        print("Como deseja pagar?")
        print("1- Crédito")
        print("2- Débito")
        print("3- Pix (-5%)")
        opcaoPag = int(input("Como deseja pagar?: "))

        if opcaoPag == 1:
            print("\n===============================")
            print("R$", totalBanho, "pago com sucesso!")
            print("===============================")
        elif opcaoPag == 2:
            print("\n===============================")
            print("R$", totalBanho, "pago com sucesso!")
            print("===============================")
        elif opcaoPag == 3:
            print("\n===============================")
            valorPix = totalBanho * 0.95
            print("R$", valorPix, "pago com sucesso!")
            print("===============================")
    elif opcao == 2:
        totalBanho = banho * peso[2]
        
        print("\n===============================")
        print("Valor total para banho: R$", totalBanho)
        print("===============================")
        print("Como deseja pagar?")
        print("1- Crédito")
        print("2- Débito")
        print("3- Pix (-5%)")
        opcaoPag = int(input("Como deseja pagar?: "))

        if opcaoPag == 1:
            print("\n===============================")
            print("R$", totalBanho, "pago com sucesso!")
            print("===============================")
        elif opcaoPag == 2:
            print("\n===============================")
            print("R$", totalBanho, "pago com sucesso!")
            print("===============================")
        elif opcaoPag == 3:
            print("\n===============================")
            valorPix = totalBanho * 0.95
            print("R$", valorPix, "pago com sucesso!")
            print("===============================")
    elif opcao == 2:
        totalBanho = banho * peso[3]
        
        print("\n===============================")
        print("Valor total para banho: R$", totalBanho)
        print("===============================")
        print("Como deseja pagar?")
        print("1- Crédito")
        print("2- Débito")
        print("3- Pix (-5%)")
        opcaoPag = int(input("Como deseja pagar?: "))

        if opcaoPag == 1:
            print("\n===============================")
            print("R$", totalBanho, "pago com sucesso!")
            print("===============================")
        elif opcaoPag == 2:
            print("\n===============================")
            print("R$", totalBanho, "pago com sucesso!")
            print("===============================")
        elif opcaoPag == 3:
            print("\n===============================")
            valorPix = totalBanho * 0.95
            print("R$", valorPix, "pago com sucesso!")
            print("===============================")
    elif opcao == 2:
        totalBanho = banho * peso[4]
        
        print("\n===============================")
        print("Valor total para banho: R$", totalBanho)
        print("===============================")
        print("Como deseja pagar?")
        print("1- Crédito")
        print("2- Débito")
        print("3- Pix (-5%)")
        opcaoPag = int(input("Como deseja pagar?: "))

        if opcaoPag == 1:
            print("\n===============================")
            print("R$", totalBanho, "pago com sucesso!")
            print("===============================")
        elif opcaoPag == 2:
            print("\n===============================")
            print("R$", totalBanho, "pago com sucesso!")
            print("===============================")
        elif opcaoPag == 3:
            print("\n===============================")
            valorPix = totalBanho * 0.95
            print("R$", valorPix, "pago com sucesso!")
            print("===============================")
    elif opcao == 2:
        totalBanho = banho * peso[5]
        
        print("\n===============================")
        print("Valor total para banho: R$", totalBanho)
        print("===============================")
        print("Como deseja pagar?")
        print("1- Crédito")
        print("2- Débito")
        print("3- Pix (-5%)")
        opcaoPag = int(input("Como deseja pagar?: "))

        if opcaoPag == 1:
            print("\n===============================")
            print("R$", totalBanho, "pago com sucesso!")
            print("===============================")
        elif opcaoPag == 2:
            print("\n===============================")
            print("R$", totalBanho, "pago com sucesso!")
            print("===============================")
        elif opcaoPag == 3:
            print("\n===============================")
            valorPix = totalBanho * 0.95
            print("R$", valorPix, "pago com sucesso!")
            print("===============================")
    elif opcao == 7:
        print("\nSaindo...")
    else:
        print("\nOpção Inválida!")


