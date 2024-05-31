global mydb
from bson.objectid import ObjectId

def DeletarUsuarioID(mydb):
    _id =  input(str('escreva seu id do Usuario:'))
    mycol = mydb.Cliente
    print("\n#### Usuario Deletado do Banco####") 
    filter = { "_id":ObjectId (_id) }
    mycol.delete_one(filter)
    for x in mycol.find():
        print(x)  