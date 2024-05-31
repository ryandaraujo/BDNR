from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import redis

print("\nConectando ao Redis...")
rd = redis.Redis(host='redis-17407.c244.us-east-1-2.ec2.redns.redis-cloud.com',
                port=17407,
                password='7gg1ZORP45xlZYfYeeovlxRsionjKv9T'
                )
print("Conectado ao Redis com sucesso")

mydb = ''
class Connect:
    global mydb
    print("\nConectando ao MongoDB...")
    uri = "mongodb+srv://ryanaraujo:fatec@cluster0.ics2su3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Conectado com sucesso ao MongoDB!\n")
    except Exception as e:
        print("Falha ao conectar")
        print(e)
    mydb = client.Mercado_Livre


class HandlerCliente:
    def insert():
        global mydb
        mycol = mydb.Cliente
        print("\n####INSERT####")
        nome = input("Nome do cliente: ")
        cpf = input("CPF do cliente: ")
        dataNasc = input("Data de nascimento do cliente: ")
        email = input("Email do cliente: ")
        ddd = int(input("DDD do telefone: "))
        telefone = int(input("Telefone do cliente: "))
        cep = input("CEP do cliente: ")
        numeroCasa = input("Número da casa do cliente: ")
        rua = input("Rua do cliente: ")
        bairro = input("Bairro do cliente: ")
        cidade = input("Cidade do cliente: ")
        estado = input("Estado do cliente: ")
        mydict = {
            "cli_nome": nome,
            "cli_cpf": cpf,
            "cli_data_nascimento": dataNasc,
            "cli_telefone": {
                "ddd": ddd,
                "numero": telefone
            },
            "cli_email": email,
            "cli_endereco": {
                "cep": cep,
                "num": numeroCasa,
                "rua": rua,
                "bairro": bairro,
                "cidade": cidade,
                "estado": estado
            }
        }
        x = mycol.insert_one(mydict)
        print(f"ID do cliente cadastrado: {x.inserted_id}")

    def findOne(nome):
        global mydb
        mycol = mydb.Cliente
        print("\n####FIND ONE####")
        query = mycol.find_one({"cli_nome": nome})
        if query: return print(query)
        else: print("Cliente não encontrado!")
        print("Erro ao buscar cliente!")

    def update(self):
        global mydb
        mycol = mydb.Cliente
        print("\n####UPDATE####")
        nome = input("Nome do cliente que será atualizado: ")
        clienteObjeto = mycol.find_one({"cli_nome": nome})
        if not clienteObjeto:
            print("\nErro ao encontrar cliente!")
            self.update()
        else: rd.set(nome, clienteObjeto)
        print(rd.get(nome))
        print("1 - Nome\n2 - CPF\n3 - Data de nascimento\n4 - Telefone\n5 - Endereço\n6 - Lista de favoritos")
        option2 = input("Opção: ")
        if option2 == '1':
            newNome = input("Novo nome: ")
            mycol.update_one({"cli_nome": nome}, {"$set": {"cli_nome": newNome}})
        elif option2 == '2':
            newCpf = input("Novo CPF: ")
            mycol.update_one({"cli_nome": nome}, {"$set": {"cli_cpf": newCpf}})
        elif option2 == '3':
            newDataNasc = input("Nova data de nascimento: ")
            mycol.update_one({"cli_nome": nome}, {"$set": {"cli_data_nascimento": newDataNasc}})
        elif option2 == '4':
            newDdd = int(input("Novo DDD: "))
            newTelefone = int(input("Novo telefone: "))
            mycol.update_one({"cli_nome": nome}, {"$set": {"cli_telefone": {"ddd": newDdd, "numero": newTelefone}}})
        elif option2 == '5':
            newCep = input("Novo CEP: ")
            newNumeroCasa = input("Novo número da casa: ")
            newRua = input("Nova rua: ")
            newBairro = input("Novo bairro: ")
            newCidade = input("Nova cidade: ")
            newEstado = input("Novo estado: ")
            mycol.update_one({"cli_nome": nome}, {"$set": {"cli_endereco": {"cep": newCep, "numero": newNumeroCasa, "rua": newRua, "bairro": newBairro, "cidade": newCidade, "estado": newEstado}}})
        elif option2 == '6':
            print("Qual operação você deseja realizar: ")
            print("1 - Adicionar um produto\n2 - Remover um produto\n")
            option3 = input("Opção: ")
            if option3 == "1":
                newFavorito = input("Nome do novo produto a ser adicionado aos favoritos: ")
                try:
                    findFavorito = HandlerProduto.findOne(newFavorito)
                    mycol.update_one({"cli_nome": nome}, {
                        "$set": {"cli_favoritos": 
                            [{findFavorito}]
                            }})
                except:
                    print("Erro ao encontrar produto!")

    def delete():
        global mydb
        mycol = mydb.Cliente
        print("\n####DELETE####")
        nome = input("Nome do cliente que será removido: ")
        mycol.delete_one({"cli_nome": nome})
        print("Deleção realizada com sucesso!")


class HandlerCompras:
    def insert():
        global mydb
        mycol = mydb.Compras
        print("\n####INSERT####")
        lista_produtos = []
        valor_total = 0
        quantidade_produtos = int(input("""Qual a quantidade de produtos da compra que deseja adicionar a compra: """))
        for i in range(quantidade_produtos):
            produto  = input(f"Nome do produto {i}: ")
            try:
                comprando = HandlerProduto.findOne(produto)
                lista_produtos.append(comprando)
                valor_total += comprando["pro_preco"]
            except:
                print("Produto não encontrado!")
                quantidade_produtos+=1
        nome_cliente = input("Nome do cliente: ")
        try:
            cliente_encontrado = HandlerCliente.findOne(nome_cliente)
        except:
            print("Cliente não encontrado!")
        compra = {
            "com_itens": lista_produtos,
            "com_cli_id": cliente_encontrado["_id"],
            "com_preco": valor_total
        }
        x = mycol.insert_one(compra)
        print(f"Compra inserida com suceso!!\nID da compra:{x.inserted_id}")

    def findOne(compra):
        global mydb
        mycol = mydb.Compras
        print("\n####FIND ONE####")
        try:
            query = mycol.find_one({"com_id": compra})
            print(query)
        except:
            print("Compra não encontrada!")


class HandlerVendedor:
    def insert():
        global mydb
        mycol = mydb.Vendedor
        print("\n####INSERT####")
        nome = input("Nome do vendedor: ")
        cfp_cnpj = input("CPF/CNPJ do vendedor: ")
        ddd = int(input("DDD do telefone: "))
        telefone = int(input("Telefone do vendedor: "))
        email = input("Email do vendedor: ")
        cep = input("CEP do vendedor: ")
        numeroCasa = input("Número da casa do vendedor: ")
        rua = input("Rua do vendedor: ")
        bairro = input("Bairro do vendedor: ")
        cidade = input("Cidade do vendedor: ")
        estado = input("Estado do vendedor: ")
        mydict = {
            "ven_nome": nome,
            "ven_cpf_cnpj": cfp_cnpj,
            "ven_contato": {
                "telefone": {
                    "ddd": ddd,
                    "numero": telefone
                },
                "email": email
            },
            "ven_endereco": {
                "cep": cep,
                "num": numeroCasa,
                "rua": rua,
                "bairro": bairro,
                "cidade": cidade,
                "estado": estado
            }
        }
        x = mycol.insert_one(mydict)
        print(f"ID do vendedor cadastrado: {x.inserted_id}")

    def findOne(vendedor):
        global mydb
        mycol = mydb.Vendedor
        print("\n####FIND ONE####")
        try:
            query = mycol.find_one({"ven_nome": vendedor})
            print(query)
        except: print("Vendedor não encontrado!")

    def update():
        global mydb
        mycol = mydb.Vendedor
        print("\n####UPDATE####")
        nome = input("Nome do vendedor que será atualizado: ")
        print("\nO que você deseja atualizar?\n1 - Nome\n2 - CPF/CNPJ\n3 - Telefone\n4 - Email\n5 - Endereço")
        option2 = input("\nOpção: ")
        if option2 == '1':
            newNome = input("Novo nome: ")
            mycol.update_one({"ven_nome": nome}, {"$set": {"ven_nome": newNome}})
        elif option2 == '2':
            newCpfCnpj = input("Novo CPF/CNPJ: ")
            mycol.update_one({"ven_nome": nome}, {"$set": {"ven_cpf_cnpj": newCpfCnpj}})
        elif option2 == '3':
            newDdd = int(input("Novo DDD: "))
            newTelefone = int(input("Novo telefone: "))
            mycol.update_one({"ven_nome": nome}, {"$set": {"ven_contato": {"ddd": newDdd, "numero": newTelefone}}})
        elif option2 == '4':
            newEmail = input("Novo email: ")
            mycol.update_one({"ven_nome": nome}, {"$set": {"ven_contato": {"email": newEmail}}})
        elif option2 == '5':
            newCep = input("Novo CEP: ")
            newNumeroCasa = input("Novo número da casa: ")
            newRua = input("Novo nome da rua: ")
            newBairro = input("Novo bairro: ")
            newCidade = input("Nova cidade: ")
            newEstado = input("Novo estado: ")
            mycol.update_one({"ven_nome": nome}, {"$set": {"ven_endereco": {
                "cep": newCep,
                "num": newNumeroCasa,
                "rua": newRua,
                "bairro": newBairro,
                "cidade": newCidade,
                "estado": newEstado
            }}})
        else: print("Opção não entendida :( ")
        option2 = ''

    def delete():
        global mydb
        mycol = mydb.Vendedor
        print("\n####DELETE####")
        nome = input("Nome do vendedor que será removido: ")
        mycol.delete_one({"ven_nome": nome})
        print("Deleção realizada com sucesso!")


class HandlerProduto:
    def insert():
        global mydb
        mycol = mydb.Produto
        nome = input("Nome do produto: ")
        descricao = input("Descrição do produto: ")
        preco = input("Preço do produto: ")
        quantidade = input("Quantidade: ")
        query = {
            "pro_nome": nome,
            "pro_descricao": descricao,
            "pro_preco": preco,
            "pro_quantidade": quantidade
        }
        try:
            x = mycol.insert_one(query)
            return print(x)
        except: print("Falha ao encontrar produto.")

    def findOne(produto):
        global mydb
        mycol = mydb.Produto
        try:
            query = mycol.find_one({"pro_nome": produto})
            print(query)
        except: print("Produto não encontrado!")

    def update(self):
        global mydb
        mycol = mydb.Produto
        nome_produto = input("\nNome do produto a ser atualizado: ")
        try:
            query_procura = mycol.find_one({"pro_nome": nome_produto})
        except:
            print("Produto não encontrado!")
            self.update()
        if query_procura:
            print("\nO que você deseja atualizar?\n1 - Nome\n2 - Descrição\n3 - Preço\n4 - Quantidade\n")
            option2 = input("\nOpção: ")
            if option2 == '1':
                new_nome = input("Novo nome: ")
                mycol.update_one({"pro_nome": nome_produto}, {"$set": {"pro_nome": new_nome}})
            elif option2 == '2':
                new_desc = input("Nova descrição: ")
                mycol.update_one({"pro_nome": nome_produto}, {"$set": {"pro_descricao": new_desc}})
            elif option2 == '3':
                new_preco = int(input("Novo preço: "))
                mycol.update_one({"pro_nome": nome_produto}, {"$set": {"pro_preco": new_preco}})
            elif option2 == '4':
                new_quant = input("Nova quantidade: ")
                mycol.update_one({"pro_nome": nome_produto}, {"$set": {"pro_quantidade": new_quant}})
            else: print("Opção não entendida :( ")
            option2 = ''

    def delete():
        global mydb
        mycol = mydb.Produto
        nome_prod = input("Insira o nome do produto a ser removido: ")
        try:
            x = mycol.delete_one({"pro_nome": nome_prod})
        except:
            print("Erro ao deletar")

autenticacao = ""
usuario = ""

def menuCompras():
    global autenticacao
    global option1
    while option1 != '0' and autenticacao:
        option1 = input("""\n####MENU####
\n1 - Registrar nova compra
\n2 - Encontrar compra
\n0 - Sair\n
\nOpção: """)
        verificar_autenticacao()
        if option1 == '1':
            HandlerCompras.insert()
        elif option1 == '2':
            compra = input("ID da compra: ")
            HandlerCompras.findOne(compra)
        else:
            global option0
            option0 = ''
            print("Opção inválida")

def menuCliente():
    global autenticacao
    global option1
    while autenticacao:
        option1 = input("""\n####MENU####
\n1 - Cadastrar
\n2 - Encontrar
\n3 - Atualizar
\n4 - Remover
\n0 - Sair
\nOpção: """)
        verificar_autenticacao()
        if option1 == '1':
            HandlerCliente.insert()
        elif option1 == '2':
            nome = input("Nome do cliente: ")
            HandlerCliente.findOne(nome)
        elif option1 == '3':
            HandlerCliente.update()
        elif option1 == '4':
            HandlerCliente.delete()
        elif option1 == '0': break
        else:
            global option0
            option0 = ''
            print("Opção inválida")

def menuVendedor():
    global autenticacao
    global option1
    while option1 != '0' and autenticacao:
        option1 = input("""\n####MENU####
\n1 - Cadastrar
\n2 - Encontrar
\n3 - Atualizar
\n4 - Remover
\n0 - Sair
\nOpção: """)
        verificar_autenticacao()
        if option1 == '1': HandlerVendedor.insert()
        elif option1 == '2':
            vendedor = input("Nome do vendedor")
            HandlerVendedor.findOne(vendedor)
        elif option1 == '3':
            HandlerVendedor.update()
        elif option1 == '4':
            HandlerVendedor.delete()
        else:
            global option0
            option0 = ''
            print("Opção inválida")

def menuProduto():
    global autenticacao
    global option1
    while autenticacao:
        option1 = input("""\n####MENU####
\n1 - Cadastrar
\n2 - Encontrar
\n3 - Atualizar
\n4 - Remover
\n0 - Sair
\nOpção: """)
        verificar_autenticacao()
        if option1 == '1': HandlerProduto.insert()
        elif option1 == '2':
            produto = input("Nome do produto: ")
            HandlerProduto.findOne(produto)
        elif option1 == '3':
            HandlerProduto.update()
        elif option1 == '4': HandlerProduto.delete()
        elif option1 == '0': break
        else:
            global option0
            option0 = ''
            print("Opção inválida")

def login():
    global autenticacao
    global usuario
    user_email = input("Email: ")
    password = input("Senha: ")

    if user_email != "" and password != "":
        try:
            rd.setex("token", 40, user_email)
            print("\nLogin bem-sucedido!")
            usuario = user_email
            autenticacao = True
            menu()
        except:
            print("\nFalha ao cadastrar usuário!\n")
    else:
        print("\nCredenciais inválidas!\n")
        login()

def verificar_autenticacao():
    global autenticacao
    print(f"\nautenticação: {autenticacao}")
    tempo = int(rd.ttl("token"))
    if tempo < 1:
        print(tempo)
        autenticacao = False
        print("\nTempo de login expirado!")
        return autenticacao
    else:
        print(rd.ttl("token"))
        autenticacao = True
        return autenticacao

def fazer_login():
    global autenticacao
    while autenticacao != True:
        print("Por favor, faça login")
        login()
    print("Usuário autenticado.")

def menu():
    while verificar_autenticacao():
        global option1
        option0 = input("""\n####MENU####\n
1 - CRUD de Produto\n
2 - CRUD de Cliente\n
3 - CRUD de Compras\n
4 - CRUD de Vendedor\n
0 - Sair\n
\nOpção: """)
        verificar_autenticacao()
        option1 = ''
        if option0 == '0':
            print("Tchau!")
        if option0 == '1':
            menuProduto()
        elif option0 == '2':
            menuCliente()
        elif option0 == '3':
            menuCompras()
        elif option0 == '4':
            menuVendedor()
        else: print("Opção não entendida!")

print(33*"#")
print("#  Bem vindo ao Mercado Livre!  #")
print(33*"#")

while True:
    print("\nMenu principal\n")
    print("1 - Entrar")
    print("2 - Sair")
    opcao = input("Opção: ")
    if opcao == '1':
        fazer_login()
    elif opcao == '2':
        break