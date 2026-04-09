from flask import Flask
from flask import render_template

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

if __name__ == '__main__':
    app.run(debug=True)