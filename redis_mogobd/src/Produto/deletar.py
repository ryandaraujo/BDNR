global mydb
from bson.objectid import ObjectId
import Produto.FindQuery


def DeletarProdutoID(mydb):
    Produto.FindQuery.PegarProdutos(mydb)
    _id = input(str('escreva seu id De Produto:'))
    mycol = mydb.Produto
    print("\n#### Produtos Deletado do Banco ####") 
    filter = { "_id":ObjectId (_id) }
    mycol.delete_one(filter)
    for x in mycol.find():
        print(x)
    return mycol  