from app.server import db

class Postagemblog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_blogspot = db.Column(db.Text)
    data_publicacao = db.Column(db.Text)
    data_modificacao = db.Column(db.Text)
    url = db.Column(db.Text)
    selflink_api = db.Column(db.Text)
    titulo = db.Column(db.Text)
    conteudo = db.Column(db.Text)
    autor = db.Column(db.Text)
    quantidade_respostas = db.Column(db.Integer)
    rotulos = db.relationship('Rotulo', backref='postagemblog', lazy=True)


class Rotulo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    plataforma = db.Column(db.Text)
    postagemblog_id = db.Column(db.Integer, db.ForeignKey('postagemblog.id'))


class Sugestao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    palavra_origem = db.Column(db.Text)
    criado_em = db.Column(db.DateTime, default=db.func.current_timestamp())


class Postagemface(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reacoes = db.Column(db.Integer)
    postagemblog_id = db.Column(db.Integer, db.ForeignKey('postagemblog.id'))