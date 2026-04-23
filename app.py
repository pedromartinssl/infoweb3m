from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime

app = Flask('__name__')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato/<email>/<tel>')
def contato(email, tel):
    return render_template('contato.html', email=email, tel=tel)

@app.route('/perfil/<usuario>')
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)

@app.route('/dados')
def dados():
    return render_template('dados.html')

@app.route('/recebedados', methods=['POST', 'GET'])
def recebedados():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    email = request.form['email']
    datanasc = request.form['datanasc']
    data_objeto = datetime.strptime(datanasc, "%d-%m-%Y")
    data_formatada = data_objeto.strftime("%d-%m-%Y")
    stand = request.form['stand']
    part = request.form['part']
    poder = request.form.getlist('poder')
    return render_template('recebedados.html',  nome=nome, 
                                                sobrenome=sobrenome, 
                                                email=email,
                                                datanasc=data_formatada,
                                                stand=stand,
                                                part=part,
                                                poder=poder
                                                )

@app.route('/compras') 
def compras():
    return render_template('compras.html')

@app.route('/recebecompras', methods=['POST', 'GET'])
def recebecompras():
    itens = request.form.getlist('item')
    return render_template('lista.html', itens=itens)

@app.route('/verificaridade/<int:idade>')
def verificaridade(idade):
    if idade >= 18:
        return 'Você é MAIOR de idade'
    else:
        return 'Você é MENOR de idade'

@app.route('/verificaridade2/<int:idade>')
def verificaridade2(idade):
    return render_template('idade.html', idade=idade)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verificarlogin', methods=['POST'])
def verificarlogin():
    usuario = request.form.get('login')
    senha = request.form.get('senha')

    if usuario == 'admin' and senha == '12345':
        return redirect(url_for('arearestrita'))
    else:
        return redirect(url_for('acessonegado'))
    
@app.route('/arearestrita')
def arearestrita():
    return render_template('arearestrita.html')

@app.route('/acessonegado')
def acessonegado():
    return render_template('acessonegado.html')

@app.route('/exemplolaco')
def exemplolaco():
    return render_template('exemplolaco.html')

@app.route('/produtos')
def produtos():
    itens = [   
                {'nome':'teclado ', 'preco':'200', 'categoria':'computador', 'imagem':'https://product-data.raiadrogasil.io/images/17272704.webp'},
                {'nome':'smartphone ', 'preco':'1500', 'categoria':'celular', 'imagem':'https://m.magazineluiza.com.br/a-static/420x420/camiseta-dry-fit-preta-caveira-dark-lab/trevizosuplementos/9118-1/142392a2b4c55f9b0b7bb56b90c3649e.jpeg'},
                {'nome':'pen-drive ', 'preco':'50',  'categoria':'computador', 'imagem':'https://redeciadasaude.cdn.magazord.com.br/img/2024/07/produto/2682/creatina-nature-8-2.jpg?ims=600x600'}
             ]

    qtd = len(itens)

    return render_template('produtos.html', itens=itens, qtd = qtd)

if __name__ == '__main__':
    app.run(debug=True)