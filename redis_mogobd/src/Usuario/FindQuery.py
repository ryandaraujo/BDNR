from bson.objectid import ObjectId

def PegarUsuarios(mydb):
    mycol = mydb.Cliente
    print("\n####SORT####") 
    mydoc = mycol.find().sort("nome")
    for x in mydoc:
        print(x)
        print("\n")
    return mydoc

def UsuariobyID(mydb):
    PegarUsuarios(mydb)
    _id =  input('Escreva o id do usuário: ')
    mycol = mydb.Cliente
    myquery = { "_id":ObjectId (_id) }
    mydoc = mycol.find_one(myquery)
    return mydoc
