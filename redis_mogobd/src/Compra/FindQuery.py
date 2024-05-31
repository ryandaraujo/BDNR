from bson.objectid import ObjectId

def PegarCompras(mydb):
    mycol = mydb.Compras
    print("\n####SORT####") 
    mydoc = mycol.find().sort("nome")
    for x in mydoc:
        print(x)
    return mydoc

def ComprasbyID(mydb):
    PegarCompras(mydb)
    _id = input('Escreva seu id da compra: ')
    mycol = mydb.Compras
    print("\n####QUERY####")
    myquery = { "_id":ObjectId (_id) }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)
    return mydoc
