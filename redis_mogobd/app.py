from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import redis

rd = redis.Redis(host='redis-17407.c244.us-east-1-2.ec2.redns.redis-cloud.com',
                port=17407,
                password='7gg1ZORP45xlZYfYeeovlxRsionjKv9T'
                )


rd.set("ryanaraujo@gmail.com","Ryan Araujo")

print(rd.get("ryanaraujo@gmail.com"))

mydb = ''
class Connect:
    global mydb
    uri = "mongodb+srv://ryanaraujo:fatec@cluster0.ics2su3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
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

    def update():
        global mydb
        mycol = mydb.Cliente
        print("\n####UPDATE####")
        nome = input("Nome do cliente que será atualizado: ")
        print("1 - Nome\n2 - CPF\n3 - Data de nascimento\n4 - Telefone\n5 - Endereço")
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
    def update():
        global mydb
        mycol = mydb.Compras
        print("####UPDATE####")
        compra = ''
        id_compra = input("Informe o ID da compra a ser atualizada: ")
        try:
            compra = mycol.find_one({"com_id": id_compra})
        except:
            print("Compra não encontrada!")
        print("1 - Cliente\n2 - Itens\n")
        option2 = input("Opção: ")
        if option2 == '1':
            newNome = input("Nome do novo cliente: ")
            try:
                new_cliente = HandlerCliente.findOne(newNome)
                mycol.update_one({"com_id": id_compra}, {"$set": {"com_cli_id": new_cliente["_id"]}})
            except:
                print("Cliente não encontrado!")
        elif option2 == '2':
            new_item = input("Novo item: ")
            try:
                new_produto = HandlerProduto.findOne(new_item)
                lista_produtos = compra["com_itens"]
                lista_produtos.append(new_produto)
                mycol.update_one({"com_id": id_compra}, {"$set": {"com_itens": lista_produtos}})
            except:
                print("Produto não encotrado!")
        else:
            print("Opção não entendida!")

    def delete():
        global mydb
        mycol = mydb.Compras
        print("####DELETE####")
        cliente = input("Nome do cliente: ")
        try:
            query = mycol.delete_one({"cli_nome": cliente})
            print(query)
        except:
            print("Cliente não encontrado!")


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
        print("1 - Nome\n2 - CPF/CNPJ\n3 - Telefone\n4 - Email\n5 - Endereço")
        option2 = input("Opção: ")
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
        except: print("Falha ao registrar produto.")
    def findOne(produto):
        global mydb
        mycol = mydb.Produto
        print("\n####FIND ONE####")
        try:
            query = mycol.find_one({"pro_nome": produto})
            print(query)
        except: print("Produto não encontrado!")
    def update():
        pass
    def delete():
        global mydb
        mycol = mydb.Produto
        nome_prod = input("Insira o nome do produto a ser removido: ")
        try:
            x = mycol.delete_one({"pro_nome": nome_prod})
        except:
            print("Erro ao deletar")


def menuCompras():
    global option1
    while option1 != '0':
        option1 = input("""\n####MENU####
                        \n1 - Cadastrar
                        \n2 - Encontrar
                        \n3 - Atualizar
                        \n4 - Remover
                        \n0 - Sair\n
                        \nOpção: """)
        if option1 == '1':
            HandlerCompras.insert()
        elif option1 == '2':
            compra = input("ID da compra: ")
            HandlerCompras.findOne(compra)
        elif option1 == '3':
            HandlerCompras.update()
        elif option1 == '4':
            HandlerCompras.delete()
        else: print("Opção inválida")

def menuCliente():
    global option1
    while option1 != '0':
        option1 = input("""\n####MENU####
\n1 - Cadastrar
\n2 - Encontrar
\n3 - Atualizar
\n4 - Remover
\n0 - Sair
\nOpção: """)
        if option1 == '1':
            HandlerCliente.insert()
        elif option1 == '2':
            nome = input("Nome do cliente: ")
            HandlerCliente.findOne(nome)
        elif option1 == '3':
            HandlerCliente.update()
        elif option1 == '4':
            HandlerCliente.delete()
        else: print("Opção inválida")

def menuVendedor():
    global option1
    while option1 != '0':
        option1 = input("""\n####MENU####
\n1 - Cadastrar
\n2 - Encontrar
\n3 - Atualizar
\n4 - Remover
\n0 - Sair
\nOpção: """)
        if option1 == '1': HandlerVendedor.insert()
        elif option1 == '2':
            vendedor = input("Nome do vendedor")
            HandlerVendedor.findOne(vendedor)
        elif option1 == '3':
            HandlerVendedor.update()
        elif option1 == '4':
            HandlerVendedor.delete()
        else: print("Opção inválida")

def menuProduto():
    global option1
    while option1 != '0':
        option1 = input("""\n####MENU####
\n1 - Cadastrar
\n2 - Encontrar
\n3 - Atualizar
\n4 - Remover
\n0 - Sair
\nOpção: """)
        if option1 == '1': HandlerProduto.insert()
        elif option1 == '2':
            produto = input("Nome do produto: ")
            HandlerProduto.findOne(produto)
        elif option1 == '3': HandlerProduto.update()
        elif option1 == '4': HandlerProduto.delete()
        else: print("Opção inválida")

option0 = input("""\n####MENU####\n
1 - CRUD de Produto\n
2 - CRUD de Cliente\n
3 - CRUD de Compras\n
4 - CRUD de Vendedor\n
0 - Sair\n
\nOpção: """)
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