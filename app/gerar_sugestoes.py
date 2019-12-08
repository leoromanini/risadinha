import requests
import logging

from app.server import db
from app.models import Sugestao

log_file = r'log_sugestoes.log'

logging.basicConfig(filename=log_file,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)


rotulos_aleatorios = db.engine.execute('''SELECT DISTINCT nome FROM rotulo ORDER BY RAND() LIMIT 100''')

sugestoes_inseridas = 0
for rotulo in rotulos_aleatorios:

    if sugestoes_inseridas >= 10:
        break

    try:
        rotulo_ingles_json = requests.post('https://translate.yandex.net/api/v1.5/tr.json/translate'
                                           '?key=trnsl.1.1.20191201T010343Z.2bab416b221c7a9d.08071f159f851969b4c2bf086f1f8dfbe285f463'
                                           '&text={}&lang=pt-en'.format(str(rotulo).split(' ')[0])).json()

        rotulo_ingles = rotulo_ingles_json['text'][0].split("'")[1]

        if rotulo_ingles.startswith('The') or rotulo_ingles.startswith('the'):
            rotulo_ingles = rotulo_ingles[4:]

        termo_relacionado = requests.get(r'https://id.nlm.nih.gov/mesh/lookup/term?label={}&match=contains'.format(rotulo_ingles)).json()[0]['label']

        termo_relacionado_traduzido = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate'
                                                   '?key=trnsl.1.1.20191201T010343Z.2bab416b221c7a9d.08071f159f851969b4c2bf086f1f8dfbe285f463'
                                                   '&text={}&lang=en-pt'.format(termo_relacionado)).json()['text'][0]

        sugestao = Sugestao()
        sugestao.nome = termo_relacionado_traduzido
        sugestao.palavra_origem = rotulo[0]
        db.session.add(sugestao)
        db.session.commit()
        logging.info('Rotulo: {} - Sugestao: {} - INSERIDO COM SUCESSO'.format(rotulo[0], termo_relacionado_traduzido))
        sugestoes_inseridas += 1

    except:
        logging.warning('Rotulo: {} - FALHA AO GERAR SUGESTAO RELACIONADO'.format(rotulo[0]))
