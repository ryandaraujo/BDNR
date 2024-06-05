def PegarProdutos(mydb):
    mycol = mydb.Produto
    print("\n####SORT####") 
    mydoc = mycol.find().sort("Nome")
    for x in mydoc:
        print(x)
        print("\n")
    return mydoc

def ProdutosNome(mydb):
    #Query
    PegarProdutos(mydb)
    nome =  input('Escreva o nome do produto:')
    mycol = mydb.Produto
    print("\n####QUERY####")
    myquery = { "nome": nome }
    mydoc = mycol.find_one(myquery)
    print(mydoc)
    return mydoc