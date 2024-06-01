from bson.objectid import ObjectId
import Usuario.FindQuery as buscaUser
import Produto.FindQuery as Buscar

def ListaDesejos(mydb):
    buscaUser.PegarUsuarios(mydb)
    Usuario =  input('Escreva o ID do usuário: ')
    Buscar.PegarProdutos(mydb)
    Produto  =  input('Escreva seu id do produto que deseja favoritar: ')

    mycol = mydb.Cliente
    mycol2 = mydb.Produto
    mydoc = mycol.find_one({"_id":ObjectId (Usuario)})
    mydoca = mycol2.find_one({"_id":ObjectId (Produto)})
    
    
    newvalues = { "$push": {
    "favoritos":mydoca
    }
    }
    print("\n#### lista de desejos atualizada com sucesso ####") 
    filter = { "_id":ObjectId (Usuario) }
    mycol.update_one(filter,newvalues)
    for x in mycol.find():
        print(x) 
    execucao = True
    while execucao:
        print('''Deseja adicionar outro produto a lista de favoritos?\n
    0 - Voltar\n
    1 - Sim\n
    2 - Não\n''')
        escolha = input('Escolha uma opção: ')
        match escolha:
            case '0':
                break
            case '1':
                ListaDesejos(mydb)
            case '2':
                return