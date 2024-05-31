
global mydb


def CadastrarUsuario(mydb):
    nome = input('escreva seu nome:')
    Data_Nascimento = input('escreva sua Data_Nascimento:')
    Email = input('escreva seu Email:')
    Senha = input('escreva seu Senha:')
    Telefone = input('escreva seu Telefone:')
    Cpf = input('escreva seu Cpf:')
    Cidade = input('escreva seu Cidade:')
    cep = input('escreva seu Endereco:')
    mycol = mydb.Cliente
    print("\n #####insert Usuario Inserido Com Sucesso. ###")
    mydict = {
    "nome":nome,
    "dataNascimento":Data_Nascimento,
    "email":Email,
    "senha":Senha,
    "telefone":Telefone,
    "cpf":Cpf,
    "favoritos":[],
    "endereco": {
        "cep": cep,
        "cidade":Cidade,
    }
    
}
    x = mycol.insert_one(mydict)
    
    print(x.inserted_id)