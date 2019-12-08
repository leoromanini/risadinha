import pdb
from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from auth import AUTH

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{AUTH}@127.0.0.1/risadinha2'
db = SQLAlchemy(app)


@app.route('/')
def index():
    consulta = db.engine.execute('SELECT count(*) nome FROM postagemblog')
    numero_postagens = [row[0] for row in consulta][0]

    consulta = db.engine.execute('SELECT count(*) nome FROM rotulo')
    numero_rotulos = [row[0] for row in consulta][0]

    consulta = db.engine.execute('SELECT sum(reacoes) nome FROM postagemface')
    numero_reacoes = [row[0] for row in consulta][0]

    consulta = db.engine.execute('SELECT count(DISTINCT r.nome) FROM rotulo r INNER JOIN postagemface p ON p.postagemblog_id = r.postagemblog_id')
    numero_rotulos_envolvidos = [row[0] for row in consulta][0]

    consulta = db.engine.execute('SELECT count(*) nome FROM sugestao')
    numero_sugestoes = [row[0] for row in consulta][0]

    consulta = db.engine.execute('SELECT min(data_publicacao) FROM risadinha2.postagemblog')
    primeiro_post = datetime.strptime([row[0] for row in consulta][0][:19], '%Y-%m-%dT%H:%M:%S')

    consulta = db.engine.execute('SELECT max(data_publicacao) FROM risadinha2.postagemblog')
    ultimo_post = datetime.strptime([row[0] for row in consulta][0][:19], '%Y-%m-%dT%H:%M:%S')

    periodo_ativo = ultimo_post - primeiro_post
    media_postagens = round(numero_postagens / (periodo_ativo.days/12))


    return render_template('resumo.html',
                           numero_postagens=numero_postagens,
                           numero_rotulos=numero_rotulos,
                           media_postagens=media_postagens,
                           numero_rotulos_envolvidos=numero_rotulos_envolvidos,
                           numero_reacoes=numero_reacoes,
                           numero_sugestoes=numero_sugestoes,
                           primeiro_post=primeiro_post.strftime('%d/%m/%Y %H:%M'),
                           ultimo_post=ultimo_post.strftime('%d/%m/%Y %H:%M'))

@app.route('/top-10')
def top():
    consulta = db.engine.execute('SELECT count(*), nome FROM rotulo GROUP BY nome order by count(*) desc limit 10')
    top10 = {}
    for item in consulta:
        top10[item[1]] = item[0]

    return render_template('top-10.html', top10=top10)


@app.route('/sugestoes')
def sugestoes():
    consulta = db.engine.execute(r'SELECT DISTINCT * FROM sugestao WHERE nome NOT LIKE "%%-%%" ORDER BY RAND() LIMIT 10')
    sugestoes =[]
    for item in consulta:
        sugestoes.append([item[1], item[2], item[3]])
    return render_template('sugestoes.html', sugestoes=sugestoes)


@app.route('/estatisticas')
def stats():
    consulta = db.engine.execute('SELECT count(nome), nome FROM rotulo GROUP BY nome ORDER BY count(nome) desc')
    blog = {}
    for item in consulta:
        blog[item[1]] = item[0]

    consulta = db.engine.execute('SELECT nome, p.reacoes FROM rotulo r INNER JOIN postagemface p ON p.postagemblog_id = r.postagemblog_id')
    reacoes = {}
    for item in consulta:
        reacoes[item[0]] = item[1]

    return render_template('estatisticas.html', blog=blog, reacoes=reacoes)
