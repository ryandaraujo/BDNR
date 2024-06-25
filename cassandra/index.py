from pprint import pprint
from astrapy import DataAPIClient

class ConnectDB:
    def __init__(self):
        # Initialize the client
        self.client = DataAPIClient("AstraCS:zSgfcmWrbSGFlwbyAgiaSpPP:a71b0905e0ee58560c97c0559a8799353cc29d77039e4c13b099fa823a09ee55")
        self.db = self.client.get_database_by_api_endpoint(
        "https://6906b3dd-e144-4650-9cf1-ff6f2caf83cd-us-east-2.apps.astra.datastax.com"
        )
        print(f"Connected to DB: {self.db.list_collection_names()}")


connect = ConnectDB()
collUsuario = connect.db.get_collection("usuario")
collVendedor = connect.db.get_collection("vendedor")
collCompra = connect.db.get_collection("compra")
collProduto = connect.db.get_collection("produto")


class Vendedor:
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj


class Usuario:
    def __init__(self, nome, sobrenome, email, senha, cpf, telefone, enderecos, favoritos):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.telefone = telefone
        self.enderecos = enderecos
        self.favoritos = favoritos


class Produto:
    def __init__(self, nome, descricao, valor, vendedor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.vendedor = vendedor


class Compra:
    def __init__(self, usuario, produtos, valor, data):
        self.usuario = usuario
        self.produtos = produtos
        self.valor = valor
        self.data = data


def cadastrar_usuario():
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    cpf = input("CPF: ")

    print("Cadastrando telefone")
    ddd = input("DDD: ")
    numero = input("Número: ")
    telefone = {"ddd": ddd, "numero": numero}

    enderecos = []
    while True:
        logradouro = input("Logradouro: ")
        numero = input("Numero: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        codigoPostal = input("Código Postal: ")
        endereco = {"logradouro": logradouro, "numero": numero, "bairro": bairro, "cidade": cidade, "estado": estado, "codigoPostal": codigoPostal}
        enderecos.append(endereco)
        opcao = input("Deseja cadastrar mais um endereço? (s/n): ")
        if opcao.lower() != 's':
            break

    favoritos = selecionar_produtos("favoritos")

    usuario = Usuario(nome, sobrenome, email, senha, cpf, telefone, enderecos, favoritos)
    collUsuario.insert_one(usuario.__dict__)    

def cadastrar_vendedor():
    nome = input("Nome do vendedor: ")
    cnpj = input("CNPJ do vendedor: ")

    vendedor = Vendedor(nome, cnpj)
    collVendedor.insert_one(vendedor.__dict__)

def cadastrar_produto():
    nome = input("Nome do produto: ")
    descricao = input("Descrição do produto: ")
    valor = float(input("Valor do produto: R$ "))
    vendedores = list(collVendedor.find())

    if not vendedores:
        print("Nenhum vendedor cadastrado. Cadastre um vendedor antes de continuar.")
        return

    print("Selecione o vendedor para associar ao produto:")
    for i, vendedor in enumerate(vendedores):
        print(f"{i}: {vendedor['nome']} ({vendedor['cnpj']})")

    id_vendedor = int(input("Digite o número correspondente: "))
    vendedor = vendedores[id_vendedor]

    produto = Produto(nome, descricao, valor, vendedor)
    collProduto.insert_one(produto.__dict__)


def cadastrar_compra():
    from time import localtime
    usuarios = list(collUsuario.find())
    produtos = list(collProduto.find())

    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    usuario = selecionar_usuario(usuarios)
    produtos_compra = selecionar_produtos("compra")

    valor_total = sum(produto.valor for produto in produtos_compra)
    data = f"{localtime().tm_mday}/{localtime().tm_mon}/{localtime().tm_year} {localtime().tm_hour}:{localtime().tm_min}:{localtime().tm_sec}"
    produtos_compra_dicts = [produto.__dict__ for produto in produtos_compra]
    compra = Compra(usuario, produtos_compra_dicts, valor_total, data)
    collCompra.insert_one(compra.__dict__)


def atualizar_usuario():
    usuarios = list(collUsuario.find())

    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    usuario = selecionar_usuario(usuarios)

    nome = input("Novo nome: ")
    sobrenome = input("Novo sobrenome: ")
    email = input("Novo email: ")
    senha = input("Nova senha: ")
    print("Atualizando telefone")
    ddd = input("Novo DDD: ")
    numero = input("Novo número: ")
    telefone = {"ddd": ddd, "numero": numero}

    enderecos = []
    while True:
        logradouro = input("Novo logradouro: ")
        numero = input("Novo número: ")
        bairro = input("Novo bairro: ")
        cidade = input("Nova cidade: ")
        estado = input("Novo estado: ")
        codigoPostal = input("Novo Código Postal: ")
        endereco = {"logradouro": logradouro, "numero": numero, "bairro": bairro, "cidade": cidade, "estado": estado, "codigoPostal": codigoPostal}
        enderecos.append(endereco)
        opcao = input("Deseja cadastrar mais um endereço? (s/n): ")
        if opcao.lower() != 's':
            break

    favoritos = selecionar_produtos("favoritos")

    usuario_atualizado = Usuario(nome, sobrenome, email, senha, usuario['cpf'], telefone, enderecos, favoritos)
    collUsuario.update_one({"_id": usuario["_id"]}, {"$set": usuario_atualizado.__dict__})


def listar_produtos():
    produtos = list(collProduto.find())

    if not produtos:
        print("Nenhum produto cadastrado.")

    for produto in produtos:
        pprint(produto)

def excluir_compra():
    compras = list(collCompra.find())

    if not compras:
        print("Nenhuma compra cadastrada.")
        return

    print("Selecione a compra que deseja excluir:")
    for i, compra in enumerate(compras):
        pprint({i: compra})

    id_compra = int(input("Digite o número correspondente: "))
    collCompra.delete_one({"_id": compras[id_compra]["_id"]})

def selecionar_usuario(usuarios):
    print("Selecione o usuário:")
    for i, user in enumerate(usuarios):
        print(f"{i}: {user['nome']} {user['sobrenome']} ({user['cpf']})")

    id_usuario = int(input("Digite o número correspondente: "))
    return usuarios[id_usuario]

def selecionar_produtos(tipo):
    produtos = list(collProduto.find())

    if not produtos:
        print("Nenhum produto cadastrado.")
        return []

    selecionados = []
    run = True
    while run:
        print(f"Selecione produtos para adicionar aos {tipo}:")
        for i, produto in enumerate(produtos):
            print(f"{i}: {produto['nome']} - {produto['descricao']} - R${produto['valor']}")
        id_produto = int(input("Digite o número correspondente ou -1 para sair: "))
        if id_produto == -1:
            run = False
        elif 0 <= id_produto < len(produtos):
            produto_obj = Produto(
                nome=produtos[id_produto]['nome'],
                descricao=produtos[id_produto]['descricao'],
                valor=produtos[id_produto]['valor'],
                vendedor=produtos[id_produto]['vendedor']
            )
            selecionados.append(produto_obj)
        else:
            print("Número inválido, tente novamente.")

    return selecionados


def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cadastrar Usuário")
        print("2 - Cadastrar Vendedor")
        print("3 - Cadastrar Produto")
        print("4 - Cadastrar Compra")
        print("5 - Atualizar Usuário")
        print("6 - Listar Produtos")
        print("7 - Excluir Compra")
        print("0 - Sair")
        opcao = int(input("Selecione a opção desejada: "))
        if opcao == 1: cadastrar_usuario()
        elif opcao == 2: cadastrar_vendedor()
        elif opcao == 3: cadastrar_produto()
        elif opcao == 4: cadastrar_compra()
        elif opcao == 5: atualizar_usuario()
        elif opcao == 6: listar_produtos()
        elif opcao == 7: excluir_compra()
        elif opcao == 0:
            print("Tchau, até mais!")
            break
        else: print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    menu_principal()
