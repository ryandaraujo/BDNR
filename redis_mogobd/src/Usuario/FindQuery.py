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
    #Query
    PegarUsuarios(mydb)
    _id =  input(str('escreva seu id do Usuario:'))
    mycol = mydb.Cliente
    print("\n####QUERY####")
    myquery = { "_id":ObjectId (_id) }
    mydoc = mycol.find_one(myquery)
    return mydoc