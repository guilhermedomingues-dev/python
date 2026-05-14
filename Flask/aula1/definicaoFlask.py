from flask import Flask

app = Flask(__name__)

@app.route('/')
def paginaInicial():
    return("Para descobrir o que é o Decorator, copie e cole '/decorator' na barra de pesquisa no navegador")

@app.route('/decorator')
def paginadecorator():
    definicao = """
    <h1>O que é um Decorator em Python</h1>
    <p>
        Um decorator em Python é um recurso da linguagem que permite modificar ou estender o comportamento de uma função ou classe sem alterar diretamente o seu código original. Isso é possível porque, em Python, funções são objetos de primeira classe, ou seja, podem ser armazenadas em variáveis, passadas como argumento para outras funções e retornadas como resultado. Um decorator funciona como uma função que recebe outra função como parâmetro, adiciona alguma lógica antes e/ou depois da execução dela e retorna uma nova função modificada. A sintaxe com o símbolo @ é apenas uma forma mais elegante de aplicar essa transformação. Quando utilizamos essa notação acima de uma função, estamos indicando que ela será passada para o decorator e substituída pela versão retornada por ele.
    </p>

    <h1>Para que Serve um Decorator</h1>
    <p>
        Os decorators são amplamente utilizados para aplicar comportamentos repetitivos em várias funções sem duplicar código. Eles permitem adicionar funcionalidades como validação de dados, controle de acesso, registro de logs, medição de tempo de execução ou qualquer outra lógica que precise envolver a execução principal da função. Em vez de inserir essas instruções manualmente em cada função do sistema, o desenvolvedor centraliza essa responsabilidade em um único decorator, promovendo organização, reutilização de código e maior clareza estrutural.
    </p>

    <h1>Como o Decorator é Utilizado no Flask</h1>
    <p>
        No framework Flask, os decorators são fundamentais para definir rotas da aplicação web. Quando utilizamos a anotação @app.route("/home") acima de uma função, estamos registrando essa função como responsável por responder às requisições feitas para a URL especificada. Internamente, o método route retorna um decorator que recebe a função, armazena sua referência na estrutura interna de rotas do framework e depois a devolve. Dessa forma, quando o servidor recebe uma requisição correspondente àquela rota, ele executa automaticamente a função associada. Assim, no contexto do Flask, o decorator atua como um mecanismo declarativo que conecta as URLs da aplicação à lógica implementada pelo desenvolvedor.
    </p>
    """
    return definicao

if __name__ == '__main__':
    app.run(debug=True)