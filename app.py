from flask import Flask, render_template

#criação de um obj, servindo para localizar arquivos
app = Flask(__name__)

#rotas
#Diz ao Flask que quando alguém visitar a página inicial
#definimos uma função que vai ser executada quando acessar essa rota
#render_template é usado para renderizar uma página no navegador
@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/categorias')
def categorias():
    return render_template('Categorias.html')

@app.route('/populares')
def populares():
    return render_template('Populares.html')

@app.route('/ofertasAni')
def ofertas():
    return render_template('OfertasAni.html')

@app.route('/lancamentos')
def lancamentos():
    return render_template('Lancamentos.html')

@app.route('/contate')
def contate():
    return render_template('Contate.html')

#essa linha serve para que a aplicaçao seja acessada atravez de um navegador
if __name__ == '__main__':
    app.run()
