from Produto.FindQuery import ProdutosbyID
from Usuario.FindQuery import UsuariobyID
from bson.json_util import dumps
import json
from bson.objectid import ObjectId


def SetUsuarios(mydb,conR):
    user = UsuariobyID(mydb)
    conR.hset("user:" + user['email'], user['nome'], dumps(user['senha']))
    resultado = conR.hget('user:' + user['email'] ,user['nome'])
    decorador = json.loads(resultado.decode())
    print(decorador)

def setListaFavoritos(mydb,conR):
    user = UsuariobyID(mydb) 
    mycol = mydb.Cliente
    conR.hset("user:" + user['email'],user['nome'], dumps(user['favoritos']))
    buscarUser = mycol.find_one({'email': user['email']})

    execucao = True
    while execucao:
        print('''Deseja Continuar favoritando mais Produtos:\n
    1 - Sim\n
    2 - Não\n
        ''')
        escolha = input('Escolha Uma opção: ')
        match escolha:
            case '0':
                break
            case '1':
                Produtos = ProdutosbyID(mydb)
                conR.hset("user:" + user['Email'],Produtos['Nome'],dumps(Produtos))
                break
            case '2':
                return('Enviado com sucesso')
    resultado = conR.hkeys('user:' + user['Email'])
    resultante = []
    for dado in resultado:
        resultante.append(json.loads(conR.hget('user:' + user['Email'], dado.decode())))
        
    mydict = {
    "nome":buscarUser['nome'],
    "dataNascimento":buscarUser['dataNascimento'],
    "email":buscarUser['email'],
    "senha":buscarUser['senha'],
    "telefone":buscarUser['telefone'],
    "cpf":buscarUser['cpf'],
    "favoritos":resultante,
    "cidade":buscarUser['cidade'],
    "endereco":buscarUser['endereco'],
    "verificado":'verificado'
    }                           
    mycol.update_one({'_id':ObjectId(buscarUser['_id'])},{'$set':mydict} , upsert=True)
    print('Enviado com sucesso',conR.hkeys('user:' + user['Email']))


def getUsuariosRedis(conR):
    print(conR.keys())


def deletaRedis(conR):
    print(conR.keys())
    Nome =  input('Escreva seu nome usuário: ')
    conR.delete(Nome)
    print('\n Usuário Retirado Do Redis Com Sucesso.')

def SetToken(mydb,conR):
    mycol = mydb.Cliente
    print(conR.keys())
    user_Email =  input('Escreva seu email: ')
    user_Nome =  input('Escreva seu nome: ')
    Verificar = conR.hget("user:" + user_Email , user_Nome)
    verificado = json.loads(Verificar.decode())
    buscarUser = mycol.find_one({'Email': user_Email})
    mydict = {
    "nome":buscarUser['nome'],
    "dataNascimento":buscarUser['dataNascimento'],
    "email":buscarUser['email'],
    "senha":buscarUser['senha'],
    "telefone":buscarUser['telefone'],
    "cpf":buscarUser['cpf'],
    "favoritos":buscarUser['favoritos'],
    "cidade":buscarUser['cidade'],
    "endereco":buscarUser['endereco'],    
    "verificado":'verificado'
    }
    print(verificado)
    x = mycol.replace_one({'email': user_Email, 'nome':user_Nome}, mydict, upsert=True)
    print(x)

