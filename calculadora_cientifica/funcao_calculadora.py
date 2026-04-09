import soma
import subtrair
import multiplicar
import divisao
import potencia
import raizquadrada
import cotacao
def calculadora():
    

    tipo=int(input("----------\nTipo da operação: \n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Potência\n6. Raiz Quadrada\n7. Cotação Dólar\n\nDigite sua escolha: "))
    
    if tipo == 1:
        numA=int(input("Informe o número a: "))
        numB=int(input("Informe o número b: "))
        print("\nSoma: ",soma.somar(numA,numB))
    elif tipo == 2:
        numA=int(input("Informe o número a: "))
        numB=int(input("Informe o número b: "))
        print("\nSubtração: ",subtrair.subtrair(numA,numB))
    elif tipo == 3:
        numA=int(input("Informe o número a: "))
        numB=int(input("Informe o número b: "))
        print("\nMultiplicação: ",multiplicar.multiplicacao(numA,numB))
    elif tipo == 4:
        numA=int(input("Informe o número a: "))
        numB=int(input("Informe o número b: "))
        print("\nDivisão: ",divisao.divisao(numA,numB))
    elif tipo == 5:
        numA=int(input("Informe o número a: "))
        numB=int(input("Informe o número b: "))
        print("\nPotência: ",potencia.potencia(numA,numB))
    elif tipo == 6:
        numA=int(input("Informe o número a: "))
        numB=int(input("Informe o número b: "))
        print("\nRaiz Quadrada: ",raizquadrada.raiz(numA,numB))
    elif tipo == 7:
        print("\nA cotação do dolar agora: USD$", cotacao.cotacao_dolar())
        opcao=int(input("Deseja converter algum valor para dólar?\n1. Sim \n2. Não\nDigite sua opção: "))
        if opcao == 1:
            valor = float(input("Informe o valor: R$"))
            dolar = float(cotacao.cotacao_dolar())
            conversao = valor / dolar
            print("O valor convertido é: R$", conversao)

    else:
        print("\nEscolha inválida!")