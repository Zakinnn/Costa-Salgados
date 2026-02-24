from flask import Flask, render_template

app = Flask(__name__)

# Lista completa de produtos com IDs baseados no seu código original
PRODUTOS_COSTA = [
    {'id': '1', 'nome': 'Pastel de Carne', 'preco': 1.30, 'cat': 'Fritos'},
    {'id': '2', 'nome': 'Pastel de Queijo', 'preco': 1.30, 'cat': 'Fritos'},
    {'id': '3', 'nome': 'Pastel de Palmito', 'preco': 1.30, 'cat': 'Fritos'},
    {'id': '4', 'nome': 'Pastel de Bacalhau', 'preco': 2.00, 'cat': 'Fritos'},
    {'id': '5', 'nome': 'Bolinha de Queijo', 'preco': 1.20, 'cat': 'Fritos'},
    {'id': '6', 'nome': 'Coxinha de Frango', 'preco': 1.20, 'cat': 'Fritos'},
    {'id': '7', 'nome': 'Coxinha de Carne', 'preco': 1.20, 'cat': 'Fritos'},
    {'id': '8', 'nome': 'Quibe', 'preco': 1.20, 'cat': 'Fritos'},
    {'id': '17', 'nome': 'Risóliz de Presunto e Queijo', 'preco': 1.20, 'cat': 'Fritos'},
    {'id': '9', 'nome': 'Esfirra de Carne', 'preco': 1.20, 'cat': 'Assados'},
    {'id': '10', 'nome': 'Esfirra de Ricota', 'preco': 1.20, 'cat': 'Assados'},
    {'id': '11', 'nome': 'Assado de Frango c/ Requeijão', 'preco': 1.30, 'cat': 'Assados'},
    {'id': '12', 'nome': 'Assado de Calabresa c/ Requeijão', 'preco': 1.30, 'cat': 'Assados'},
    {'id': '13', 'nome': 'Empadinha de Frango', 'preco': 1.30, 'cat': 'Assados'},
    {'id': '14', 'nome': 'Empadinha de Palmito', 'preco': 1.30, 'cat': 'Assados'},
    {'id': '15', 'nome': 'Enroladinho', 'preco': 1.20, 'cat': 'Assados'},
    {'id': '16', 'nome': 'Espetinho de Frango', 'preco': 1.80, 'cat': 'Assados'},
    {'id': '18', 'nome': 'Empadinha de Camarão', 'preco': 2.00, 'cat': 'Assados'},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/produtos')
def produtos():
    categorias = {}
    for p in PRODUTOS_COSTA:
        categorias.setdefault(p['cat'], []).append(p)
    return render_template('produtos.html', categorias=categorias)

@app.route('/calculadora')
def calculadora():
    return render_template('calculadora.html', produtos=PRODUTOS_COSTA)

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)