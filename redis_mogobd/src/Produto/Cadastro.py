import datetime

global mydb

def CadastrarProduto(mydb):
    Nome =  input('Nome do produto: ')
    Descricao =  input('Descrição do produto: ')
    Preco =  float(input('Escreva seu Preço: '))
    Quantidade_Estoque =  int(input('Quantidade desse produto em estoque: '))
    NomeVendedor =  input('Nome do vendedor: ')

    mycol = mydb.Produto

    print("\n ##### Produto Inserido ###")
    mydict = {
        "nome":Nome,
        "dataProduto": datetime.datetime.now(),
        "descricao":Descricao,
        "preco":Preco,
        "quantidadeEstoque":Quantidade_Estoque,
        "vendedor":{"nomeVendedor":NomeVendedor,}
        }
        
    x = mycol.insert_one(mydict)
    print(x.inserted_id)