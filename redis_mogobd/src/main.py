import pymongo
from pymongo.server_api import ServerApi
import os

from login import Login

uri = "mongodb+srv://ryanaraujo:fatec@cluster0.ics2su3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(uri, server_api=ServerApi('1'))

global mydb
mydb = client.Mercado_Livre


while True:
  print(32*"#")
  print('# Bem-vindo ao Mercado Livre! #')
  print(32*"#")
  print("1 - Entrar")
  print("0 - Sair")
  option = int(input("Digite a opção desejada: "))
  match(option):
    case 1:
      Login(mydb)
    case 2:
      os.system('cls' if os.name == 'nt' else 'clear')
      break
