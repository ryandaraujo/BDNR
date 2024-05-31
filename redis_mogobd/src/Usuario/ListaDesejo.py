from bson.objectid import ObjectId
import Usuario.FindQuery as buscaUser
import Produto.FindQuery as Buscar

def ListaDesejos(mydb):
    buscaUser.PegarUsuarios(mydb)
    Usuario =  input('Escreva o ID do usuário:')
    Buscar.PegarProdutos(mydb)
    Produto  =  input('Escreva seu id do Produto que deseja Salvar:')

    mycol = mydb.Cliente
    mycol2 = mydb.Produto
    mydoc = mycol.find_one({"_id":ObjectId (Usuario)})
    mydoca = mycol2.find_one({"_id":ObjectId (Produto)})
    
    
    newvalues = { "$push": {
    "lista_Desejo":mydoca
    }
    }
    print("\n#### lista de desejos atualizada com sucesso ####") 
    filter = { "_id":ObjectId (Usuario) }
    mycol.update_one(filter,newvalues)
    for x in mycol.find():
        print(x) 
    execucao = True
    while execucao:
        print('''Deseja Continuar Comprando:\n
    0 - Voltar\n
    1 - Sim\n
    2 - Não\n''')
        escolha = input('Escolha Uma opção: ')
        match escolha:
            case '0':
                break
            case '1':
                ListaDesejos(mydb)
            case '2':
                return