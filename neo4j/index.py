from neo4j import GraphDatabase, basic_auth

class Neo4jConnection:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=basic_auth(user, password))

    def close(self):
        self._driver.close()

    def execute_query(self, query, params=None):
        with self._driver.session(database="neo4j") as session:
            result = session.run(query, params)
            return result


uri = "neo4j+s://8d6c4351.databases.neo4j.io"
user = "neo4j"
password = "22ttZiKIwGGOccOjbyg2nBZlWt5iKp789NXJ4GFj0tc"
conn = Neo4jConnection(uri, user, password)

class HandlerVendedor:
    @staticmethod
    def insert():
        query = """
        CREATE (vendedor:Vendedor {nome: $nome, cpf_cnpj: $cpf_cnpj, telefone: $telefone, email: $email,
                                    cep: $cep, numero_casa: $numero_casa, rua: $rua, bairro: $bairro,
                                    cidade: $cidade, estado: $estado})
        RETURN vendedor
        """
        print("### Informações pessoais ###")
        nome = input("Nome do vendedor: ")
        cpf_cnpj = input("CPF ou CNPJ: ")
        print("### Informações para contato ###")
        telefone = input("Telefone: ")
        email = input("Email: ")
        cep = input("CEP: ")
        numero_casa = input("Numero da casa: ")
        rua = input("Rua: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        params = {
            "nome": nome,
            "cpf_cnpj": cpf_cnpj,
            "telefone": telefone,
            "email": email,
            "cep": cep,
            "numero_casa": numero_casa,
            "rua": rua,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado
        }
        result = conn.execute_query(query, params)
        return result.single()

    @staticmethod
    def findAll():
        query = """
        MATCH (vendedor:Vendedor)
        RETURN vendedor
        """
        result = conn.execute_query(query)
        return result


class HandlerCliente:
    @staticmethod
    def insert():
        query = """
        CREATE (cliente:Cliente {nome: $nome, cpf: $cpf, data_nascimento: $data_nascimento, 
        telefone: $telefone, email: $email, cep: $cep, numero_casa: $numero_casa, rua: $rua,
        bairro: $bairro, cidade: $cidade, estado: $estado, favoritos: []})
        RETURN cliente
        """
        print("### Informações pessoais ###")
        nome = input("Nome do cliente: ")
        data_nascimento = input("Data de nascimento no formato DD/MM/AAAA: ")
        cpf = input("CPF: ")
        print("### Informações para contato ###")
        telefone = input("Telefone: ")
        email = input("Email: ")
        cep = input("CEP: ")
        numero_casa = input("Numero da casa: ")
        rua = input("Rua: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        params = {
            "nome": nome,
            "cpf": cpf,
            "data_nascimento": data_nascimento,
            "telefone": telefone,
            "email": email,
            "cep": cep,
            "numero_casa": numero_casa,
            "rua": rua,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado
        }
        result = conn.execute_query(query, params)
        return result.single()

    @staticmethod
    def findAll():
        query = """
        MATCH (cliente:Cliente)
        RETURN cliente
        """
        result = conn.execute_query(query)
        return result


class HandleProduto:
    @staticmethod
    def insert():
        nome = input("Nome do produto: ")
        descricao = input("Descricao do produto: ")
        preco = float(input("Preco do produto: "))
        query = """
        CREATE (produto:Produto {nome: $nome, descricao: $descricao, preco: $preco)
        RETURN produto
        """
        params = {
            "nome": nome,
            "descricao": descricao,
            "preco": preco
        }
        result = conn.execute_query(query, params)
        return result.single()

    @staticmethod
    def findAll():
        query = """
        MATCH (produto:Produto)
        RETURN produto
        """
        result = conn.execute_query(query)
        return result


class HandleCompra:
    @staticmethod
    def selectCliente(self, id_cliente):
        query = """
        MATCH (cliente:Cliente {id: $id_cliente})
        RETURN cliente
        """
        params = {"id_cliente": id_cliente}
        result = conn.execute_query(query, params)
        return result.single()

    @staticmethod
    def selectProduto(self, id_produto):
        query = """
        MATCH (produto:Produto {id: $id_produto})
        RETURN produto
        """
        params = {"id_produto": id_produto}
        result = conn.execute_query(query, params)
        return result.single()

    @staticmethod
    def insert():
        query = """
        MATCH (cliente:Cliente {id: $id_cliente})
        MATCH (produto:Produto {id: $id_produto})
        CREATE (compra:Compra {
            id_cliente: $id_cliente,
            id_produto: $id_produto,
            quantidade: $quantidade,
            valor_total: $valor_total,
            data: date()
        })
        MERGE (cliente)-[:REALIZOU_COMPRA]->(compra)
        MERGE (produto)-[:FOI_COMPRADO_EM]->(compra)
        RETURN compra
        """
        id_cliente = input("Informe o ID do cliente: ")
        cliente = HandleCompra.selectCliente(id_cliente)
        if not cliente:
            print(f"Cliente com ID {id_cliente} não encontrado.")
            return None
        
        id_produto = input("Informe o ID do produto: ")
        produto = HandleCompra.selectProduto(id_produto)
        if not produto:
            print(f"Produto com ID {id_produto} não encontrado.")
            return None
        else:
            quantidade = int(input("Informe a quantidade do produto: "))
            valor_total = produto["preco"]*quantidade
        params = {
            "id_cliente": id_cliente,
            "id_produto": id_produto,
            "quantidade": quantidade,
            "valor_total": valor_total
        }
        result = conn.execute_query(query, params)
        return result.single()

    @staticmethod
    def findAll():
        query = """
        MATCH (compra:Compra)
        RETURN compra
        """
        result = conn.execute_query(query)
        return result


def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Vendedor")
        print("3 - Cadastrar Produto")
        print("4 - Cadastrar Compra")
        print("5 - Listar Clientes")
        print("6 - Listar Vendedores")
        print("7 - Listar Produtos")
        print("8 - Listar Compras")
        print("0 - Sair")
        opcao = int(input("Selecione a opção desejada: "))
        if opcao == 1: HandlerCliente.insert() 
        elif opcao == 2: HandlerVendedor.insert()
        elif opcao == 3: HandleProduto.insert()
        elif opcao == 4: HandleCompra.insert()
        elif opcao == 5: HandlerCliente.findAll()
        elif opcao == 6: HandlerVendedor.findAll()
        elif opcao == 7: HandleProduto.findAll()
        elif opcao == 8: HandleCompra.findAll()
        elif opcao == 0:
            print("Tchau, até mais!")
            break
        else: print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    menu_principal()
