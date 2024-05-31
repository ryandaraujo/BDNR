global mydb
from bson.objectid import ObjectId
import Produto.FindQuery

def AtualizarProdutoID(mydb):
    Produto.FindQuery.ProdutosbyID(mydb)
    id =  input(str('Escreva O NumeroInscricao do Produto:'))
    mycol = mydb.Produtos
    Nome =  input(str('escreva seu Nome Produto:'))
    Data_Produto =  input(str('escreva seu Data Produto:'))
    Descricao =  input(str('escreva uma Descrição:'))
    Preco =  input(str('escreva seu Preço:'))
    Quantidade_Estoque =  input(str('escreva Quantidade Estoque desse Produto:'))
    NomeVendedor =  input(str('escreva O Nome do Vendedor:'))
    Telefone =  input(str('escreva O Telefone do Vendedor:'))
    NumeroInscricao =  input(str('escreva O NumeroInscricao do Vendedor:'))
    print("\n#### Produto Atualizado no Banco ####") 
    newvalues = { "$set": {
    "Nome":Nome,
    "Data_Produto":Data_Produto,
    "Descricao":Descricao,
    "Preco":Preco,
    "Quantidade_Estoque":Quantidade_Estoque,
    "Vendedor":{"NomeVendedor":NomeVendedor,
    "Telefone":Telefone,
    "NumeroInscricao":NumeroInscricao}}
    }
    filter = { "_id":ObjectId (id) }
    mycol.update_one(filter,newvalues)
    for x in mycol.find():
        print(x)  