from bson.objectid import ObjectId

def PegarUsuarios(conR): 
    mydoc = conR.get("users").decode()
    print(mydoc)
    return mydoc

def UsuariobyID(mydb):
    PegarUsuarios(mydb)
    _id =  input('Escreva o id do usuário: ')
    mycol = mydb.Cliente
    myquery = { "_id":ObjectId (_id) }
    mydoc = mycol.find_one(myquery)
    return mydoc
