import pdb

import requests
from app.models import Postagemblog, Rotulo
from app.server import db

request = requests.get('https://www.googleapis.com/blogger/v3/blogs/9116849055447065240/posts?key=AIzaSyCs7gmJiyrN22rgW9gZLEdY4xUNQUWMFIs&maxResults=500')

for item in request.json()['items']:

    if not Postagemblog.query.filter_by(id_blogspot=item['id']).first():
        nova_postagem = Postagemblog()
        nova_postagem.id_blogspot = item['id']
        nova_postagem.data_publicacao = item['published']
        nova_postagem.data_modificacao = item['updated']
        nova_postagem.url = item['url']
        nova_postagem.selflink_api = item['selfLink']
        nova_postagem.titulo = item['title']
        nova_postagem.conteudo = item['content']
        nova_postagem.autor = item['author']['displayName']
        nova_postagem.quantidade_respostas = item['replies']['totalItems']

        db.session.add(nova_postagem)
        db.session.commit()

        if 'labels' in item.keys():
            for rotulo in item['labels']:
                novo_rotulo = Rotulo()
                novo_rotulo.plataforma = 'Blog'
                novo_rotulo.nome = rotulo
                novo_rotulo.postagemblog_id = nova_postagem.id
                db.session.add(novo_rotulo)
                db.session.commit()

