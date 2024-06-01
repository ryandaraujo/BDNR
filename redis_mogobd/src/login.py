import uuid
import json
import os
import redis
from bson import ObjectId

import ListaCase

conR = redis.Redis(
    host='redis-17407.c244.us-east-1-2.ec2.redns.redis-cloud.com',
    port=17407,
    password='7gg1ZORP45xlZYfYeeovlxRsionjKv9T'
)

def Login(mydb):
    email = input("\nDigite o email do usuário: ")
    senha = input("\nDigite a senha do usuário: ")
    if email and senha:
        JWT = str(uuid.uuid4())
        conR.setex("token", 50, JWT)
        os.system('cls' if os.name == 'nt' else 'clear')
        Menu(mydb)
    else:
        print("Usuário não encontrado!")

def Autenticacao():
    global token
    token = conR.get("token")

def Menu(mydb):
    global token
    Autenticacao()
    if token is None:
        conR.flushall()
        print("Você precisa fazer login novamente!")
    while token:
        Autenticacao()
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''Escolha Uma Opção:\n
    1 - Menu compras\n
    2 - Menu usuário\n
    3 - Menu produto\n
    4 - Menu vendedor\n
    0 - Sair
    ''')
        escolha = input('Opção: ')
        match escolha:
            case '0':
                break
            case '1':
                ListaCase.CaseCompra(mydb)
            case '2':
                ListaCase.CaseUsuario(mydb, conR)
            case '3':
                ListaCase.CaseProduto(mydb)
            case '4':
                ListaCase.CaseVendedor(mydb)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)