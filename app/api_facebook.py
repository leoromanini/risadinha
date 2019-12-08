token = 'EAAHwuQJgpZAgBANK4zC8D32HFOjBrySnNS7WZCqaj5NXS6MVIJccvaaQVvOZCBrg2aE77cJ9qwpVt4zih2AoupvO9ygGP8k4ols8tg0sa54Q4yYPrdnZCw4OrfmsBL77bUMUWzsqN8qLKF9GsxABsCVlbX5zhgZBALNv2MDSwIBR7icQ0b0xuDynjIeMKRH2EK63ZBlHvo3yqJkDDaCQAT21ZAZBaGXlTX2RIXuTW9ZCiYQZDZD'



import requests
from app.models import Postagemblog, Rotulo
from app.server import db

request = requests.get('https://graph.facebook.com/DrRisadinha?fields=id,name&access_token={}', token)


#risadinha
#ID do APLICATIVO: 546152376214936


