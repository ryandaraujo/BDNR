import Usuario.FindQuery as Procurar
import Produto.FindQuery as ProcurarProduto
from bson.objectid import ObjectId

def Compra(mydb, conR):
    mycol = mydb.Compras
    mycol2 = mydb.Produto
    mycol3= mydb.Cliente
    Procurar.PegarUsuarios(conR)
    Usuario =  input('Escreva seu id de usuário: ')
    ProcurarProduto.PegarProdutos(mydb)
    Produto  =  input('Escreva o id do produto: ')

    mydoc = mycol3.find_one({"_id":ObjectId (Usuario)})
    mydoca = mycol2.find_one({"_id":ObjectId (Produto)})
    preco = mydoca["preco"]
    vendedor = mydoca["vendedor"]
    NomeVendedorid = vendedor["nomeVendedor"]
    Telefone = vendedor["telefone"]
    
    mydict = {
        "usuarioID":{"_id":ObjectId (Usuario) },
        "produtoID":{"_id":ObjectId (Produto) },
        "totalCompra":mydoca["nome"],
        "preco":preco,
        "nomeVendedor":NomeVendedorid,
        "telefone":Telefone,
    }
    print(mydict)
    print("\n ##### Compra Inserida ###")

    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    execucao = True
    while execucao:
        print('''Deseja Continuar Comprando:\n
    1 - Sim\n
    2 - Não\n
        ''')
        escolha = input('Escolha Uma Opção: ')
        match escolha:
            case '0':
                break
            case '1':
                Compra(mydb)
            case '2':
                return

