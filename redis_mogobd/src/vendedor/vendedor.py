from Produto.FindQuery import ProdutosbyID
from Usuario.FindQuery import UsuariobyID
from bson.json_util import dumps
import json
from bson.objectid import ObjectId


def setVendedor(mydb):
    mycol = mydb.Vendedor
    nome = input('Escreva o nome do vendedor:')
    Data_Nascimento = input('Escreva sua data de nascimento(DD/MM/AAAA): ')
    Email = input('Escreva seu email:')
    Senha = input('Escreva seu senha:')
    Telefone = input('Escreva seu telefone:')
    Cpf = input('Escreva seu cpf:')
    Cidade = input('Escreva seu cidade:')
    cep = input('Escreva seu endereco:')
    print("\n #####insert Usuario Inserido Com Sucesso. ###")
    mydict = {
    "nome":nome,
    "dataNascimento":Data_Nascimento,
    "email":Email,
    "senha":Senha,
    "telefone":Telefone,
    "cpf":Cpf,
    "endereco": {
        "cep": cep,
        "cidade":Cidade,
        }
    }
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

def atualizarVendedor(mydb):
    mycol = mydb.Vendedor
    listVendedor(mydb)
    _id =  input('Escreva o id do vendedor: ')
    filter = { "_id":ObjectId (_id) }
    print("\nO que você deseja atualizar?\n1 - Nome\n2 - CPF/CNPJ\n3 - Telefone\n4 - Email\n5 - Endereço")
    option2 = input("\nOpção: ")
    if option2 == '1':
        newNome = input("Novo nome: ")
        mycol.update_one(filter, {"$set": {"nome": newNome}})
    elif option2 == '2':
        newCpfCnpj = input("Novo CPF/CNPJ: ")
        mycol.update_one(filter, {"$set": {"cpf": newCpfCnpj}})
    elif option2 == '3':
        newTelefone = input("Novo telefone: ")
        mycol.update_one(filter, {"$set": {"telefone": newTelefone}})
    elif option2 == '4':
        newEmail = input("Novo email: ")
        mycol.update_one(filter, {"$set": {"email": newEmail}})
    elif option2 == '5':
        newCep = input("Novo CEP: ")
        newNumeroCasa = input("Novo número da casa: ")
        newRua = input("Novo nome da rua: ")
        newBairro = input("Novo bairro: ")
        newCidade = input("Nova cidade: ")
        newEstado = input("Novo estado: ")
        mycol.update_one(filter, {"$set": {"endereco": {
            "cep": newCep,
            "num": newNumeroCasa,
            "rua": newRua,
            "bairro": newBairro,
            "cidade": newCidade,
            "estado": newEstado
        }}})
    option2 = ''
    execucao = True
    while execucao:
        print('''Deseja atualizar mais algum vendedor?\n
    1 - Sim\n
    2 - Não\n
        ''')
        escolha = input('Escolha Uma opção: ')
        match escolha:
            case '0':
                break
            case '1':
                atualizarVendedor(mydb)
            case '2':
                return


def deleteVendedor(mydb):
    listVendedor(mydb=mydb)
    _id =  input('Escreva o id do vendedor: ')
    mycol = mydb.Vendedor
    filter = { "_id":ObjectId (_id) }
    mycol.delete_one(filter)
    print("\n#### Vendedor excluído ####") 
    for x in mycol.find():
        print(x)  

def listVendedor(mydb):
    mycol = mydb.Vendedor
    print("\n####SORT####") 
    mydoc = mycol.find().sort("nome")
    for x in mydoc:
        print(x)
    return mydoc
