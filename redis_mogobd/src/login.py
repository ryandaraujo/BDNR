import uuid
import json
import os
import redis
from bson import ObjectId
import pymongo
from pymongo.server_api import ServerApi

import ListaCase

conR = redis.Redis(
    host='redis-17407.c244.us-east-1-2.ec2.redns.redis-cloud.com',
    port=17407,
    password='7gg1ZORP45xlZYfYeeovlxRsionjKv9T'
)

uri = "mongodb+srv://ryanaraujo:fatec@cluster0.ics2su3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
mydb = client.Mercado_Livre


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


def Login():
    global mydb
    email = input("\nDigite o email do usuário: ")
    senha = input("Digite a senha do usuário: ")
    if email and senha:
        mycol = mydb.Cliente
        users = list(mycol.find())
        jwt = str(uuid.uuid4())
        conR.setex("token", 10, jwt)
        if users: conR.set("users", JSONEncoder().encode(users))
        print(conR.get("users"))
        os.system('cls' if os.name == 'nt' else 'clear')
        Menu(mydb)
    else:
        print("Usuário não encontrado!")

def Autenticacao():
    global token
    token = conR.get("token")
    return token

def Menu(mydb):
    global token
    Autenticacao()
    if token is None:
        conR.flushall()
        print("Você precisa fazer login novamente!")
    while token:
        Autenticacao()
        print(f"Autenticação: {Autenticacao()}")
        print('''Escolha Uma Opção:\n
    1 - Menu compras\n
    2 - Menu usuário\n
    3 - Menu produto\n
    4 - Menu vendedor\n
    0 - Sair
    ''')
        escolha = input('Opção: ')
        Autenticacao()
        if token is None:
            conR.flushall()
            print("Você precisa fazer login novamente!")
            return
        else:
            match escolha:
                case '0':
                    break
                case '1':
                    ListaCase.CaseCompra(mydb, Autenticacao, token, conR)
                case '2':
                    ListaCase.CaseUsuario(mydb, conR, Autenticacao, token)
                case '3':
                    ListaCase.CaseProduto(mydb, Autenticacao, token)
                case '4':
                    ListaCase.CaseVendedor(mydb, Autenticacao, token)
