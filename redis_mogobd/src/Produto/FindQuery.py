from bson.objectid import ObjectId

def PegarProdutos(mydb):
    mycol = mydb.Produto
    print("\n####SORT####") 
    mydoc = mycol.find().sort("Nome")
    for x in mydoc:
        print(x)
        print("\n")
    return mydoc

def ProdutosbyID(mydb):
    #Query
    PegarProdutos(mydb)
    _id =  input(str('Escreva o id do seu produto:'))
    mycol = mydb.Produto
    print("\n####QUERY####")
    myquery = { "_id":ObjectId (_id) }
    mydoc = mycol.find_one(myquery)
    print(mydoc)
    return mydoc