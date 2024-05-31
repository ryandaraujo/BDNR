from bson.objectid import ObjectId
import Usuario.FindQuery

def AtualizarUsuarioID(mydb):
    Usuario.FindQuery.UsuariobyID(mydb)
    _id =  input(str('Escreva Numero Do ID do USuario:'))
    mycol = mydb.usuario
    Nome = input(str('escreva seu Nome:'))
    Data_Nascimento = input(str('escreva sua Data_Nascimento:'))
    Email = input(str('escreva seu Email:'))
    Telefone = input(str('escreva seu Telefone:'))
    Cpf = input(str('escreva seu Cpf:'))
    Cidade = input(str('escreva seu Cidade:'))
    Endereco = input(str('escreva seu Endereco:'))
    newvalues = { "$set": {
    "Nome":Nome,
    "Data_Nascimento":Data_Nascimento,
    "Email":Email,
    "Telefone":Telefone,
    "Cpf":Cpf,
    "Cidade":Cidade,
    "Endereco":Endereco,
    "lista_Desejo":[]
    }
    }
    print("\n#### Usuario Atualizado Com Sucesso. ####") 
    filter = { "_id":ObjectId (_id) }
    mycol.update_one(filter,newvalues)
    for x in mycol.find():
        print(x)  