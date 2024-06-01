from FindQuery import PegarUsuarios as listar
from bson.objectid import ObjectId


def DeletarUsuarioID(mydb):
    listar(mydb=mydb)
    _id =  input('Escreva o id do usuário: ')
    mycol = mydb.Cliente
    filter = { "_id":ObjectId (_id) }
    mycol.delete_one(filter)
    print("\n#### Usuario Deletado do Banco####") 
    for x in mycol.find():
        print(x)  