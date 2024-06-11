from bson.objectid import ObjectId
import json

import Usuario.FindQuery as buscaUser
import Produto.FindQuery as Buscar


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
    

def ListaDesejos(mydb, conR):
    buscaUser.PegarUsuarios(conR)
    Usuario =  input('Escreva o ID do usuário: ')
    Buscar.PegarProdutos(mydb)
    Produto  =  input('Escreva seu id do produto que deseja favoritar: ')

    mycol2 = mydb.Produto
    mydoca = mycol2.find_one({"_id":ObjectId (Produto)})
    user_key = f"user:{Usuario}:favoritos"  # Chave para armazenar no Redis
    conR.sadd(user_key, json.dumps(mydoca, default=str))

    print("\n#### Lista de desejos atualizada com sucesso no Redis ####")

    execucao = True
    while execucao:
        print('''Deseja adicionar outro produto a lista de favoritos?\n
    0 - Voltar\n
    1 - Sim\n
    2 - Não\n''')
        escolha = input('Escolha uma opção: ')
        match escolha:
            case '0':
                MigrarDadosRedisMongoDB(mydb, conR)
                break
            case '1':
                ListaDesejos(mydb)
            case '2':
                MigrarDadosRedisMongoDB(mydb, conR)
                return

def MigrarDadosRedisMongoDB(mydb, conR):
    for user_key in conR.keys("user:*:favoritos"):
        user_id = user_key.decode().split(":")[1]
        favoritos = [produto.decode() for produto in conR.smembers(user_key)]
        mycol = mydb.Cliente
        mycol.update_one({"_id": ObjectId(user_id)}, {"$addToSet": {"favoritos": {"$each": favoritos}}})
        # Remover os dados do Redis após a migração
        conR.delete(user_key)
        users = list(mycol.find())
        conR.set("users", JSONEncoder().encode(users))
    print("\n#### Dados migrados do Redis para o MongoDB com sucesso ####")
