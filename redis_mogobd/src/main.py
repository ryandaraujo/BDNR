import pymongo
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import ListaCase as ListaUsuario
import redis


uri = "mongodb+srv://ryanaraujo:fatec@cluster0.ics2su3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
conR = redis.Redis(host='redis-17407.c244.us-east-1-2.ec2.redns.redis-cloud.com',
                  port=17407,
                  password='7gg1ZORP45xlZYfYeeovlxRsionjKv9T')
global mydb
mydb = client.Mercado_Livre

execucao = True
while execucao:
  print('''Escolha Uma Opção:\n
1 - Menu Comprar\n
2 - Menu Usuario\n
3 - Menu Produto\n
4 - Menu Redis\n
0 - Sair
''')
  escolha = input('Opção:')
  match escolha:
      case '0':
          break
      case '1':
        ListaUsuario.CaseCompra(mydb)
      case '2':
          ListaUsuario.CaseUsuario(mydb)
      case '3':
          ListaUsuario.CaseProduto(mydb)
      case '4':
        ListaUsuario.Caseredis(mydb,conR)

