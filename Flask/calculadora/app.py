from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST'])
def index():
    
    from flask import request
    if request.method == 'GET':
        return render_template('calculadora.html')

    
    from calculadora import calcular
    return calcular()

if __name__ == '__main__':
    app.run(debug=True)
