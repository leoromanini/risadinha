from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('resumo.html')


@app.route('/top-10')
def top():
    return render_template('top-10.html')


@app.route('/postagens')
def posts():
    return render_template('postagens.html')


@app.route('/estatisticas')
def stats():
    return render_template('estatisticas.html')


app.run(debug=True)