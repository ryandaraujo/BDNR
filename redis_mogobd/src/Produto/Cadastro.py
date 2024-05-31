import datetime

global mydb

def CadastrarProduto(mydb):
    Nome =  input('Nome do produto: ')
    Descricao =  input('Descrição do produto: ')
    Preco =  input(float('Escreva seu Preço: '))
    Quantidade_Estoque =  input(int('Quantidade desse produto em estoque: '))
    NomeVendedor =  input('Nome do vendedor: ')
    

    mycol = mydb.Produto
    
    print("\n ##### Produto Inserido ###")
    mydict = {
        "nome":Nome,
        "dataProduto": datetime.date(),
        "descricao":Descricao,
        "preco":Preco,
        "quantidadeEstoque":Quantidade_Estoque,
        "vendedor":{"nomeVendedor":NomeVendedor,}
        }
        
    x = mycol.insert_one(mydict)
    print(x.inserted_id)