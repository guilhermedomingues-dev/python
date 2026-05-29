import math

from flask import render_template, request


def calcular():
    
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]

    
    if operacao == "sqrt":
        
        if num1 < 0:
            resultado = "Erro"
            etapas = f"Não existe raiz real de {num1}."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"

    elif operacao == "log":
        
        if num1 <= 0:
            resultado = "Erro"
            etapas = f"Logaritmo indefinido para {num1} (precisa ser > 0)."
        else:
            resultado = math.log(num1)
            etapas = f"ln({num1}) = {resultado}"

    elif operacao == "bhaskara":
        
        num2_val = request.form.get("num2", "").strip()
        num3_val = request.form.get("num3", "").strip()

        if not num2_val or not num3_val:
            return render_template(
                "calculadora.html",
                etapas="Para Bhaskara informe os coeficientes a, b e c.",
                resultados="",
            )

        a = num1
        b = float(num2_val)
        c = float(num3_val)
        delta = b**2 - 4 * a * c

        if delta < 0:
            resultado = "Sem raizes reais"
            etapas = (f"Delta = {b}^2 - 4*{a}*{c} = {delta} -> Delta < 0, "
              f"nao ha raizes reais.")
        elif delta == 0:
            x = -b / (2 * a)
            resultado = f"x = {x}"
            etapas = (f"Delta = {delta} -> x = {-b} / (2*{a}) = {x}")
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            resultado = f"x1 = {x1:.4f}  |  x2 = {x2:.4f}"
            etapas = (f"Delta = {b}^2 - 4*{a}*{c} = {delta} -> "
            f"x1 = ({-b} + sqrt({delta})) / {2*a} = {x1:.4f}  |  "
             f"x2 = ({-b} - sqrt({delta})) / {2*a} = {x2:.4f}")

        return render_template("calculadora.html", etapas=etapas, resultados=resultado)

    else:
        
        num2_valor = request.form.get("num2", "").strip()

        if not num2_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
            )

        num2 = float(num2_valor)

        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"

        elif operacao == "-":
            resultado = num1 - num2
            etapas = f"{num1} - {num2} = {resultado}"

        elif operacao == "*":
            resultado = num1 * num2
            etapas = f"{num1} × {num2} = {resultado}"

        elif operacao == "/":
            if num2 == 0:
                resultado = "Erro"
                etapas = f"Divisão por zero é indefinida."
            else:
                resultado = num1 / num2
                etapas = f"{num1} ÷ {num2} = {resultado}"

        elif operacao == "**":
            resultado = num1 ** num2
            etapas = f"{num1} ^ {num2} = {resultado}"

        else:
            resultado = "Operação inválida"
            etapas = "Selecione uma operação válida."

    return render_template("calculadora.html", etapas=etapas, resultados=resultado)
