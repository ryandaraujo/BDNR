import random
from neo4j import GraphDatabase

class App:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def criar_usuario(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._criar_usuario)

    @staticmethod
    def _criar_usuario(tx):
        query = """
        CREATE (u:Usuario {nome: $nome, email: $email, cpf: $cpf, estado: $estado, cidade: $cidade, rua: $rua, numero: $numero})
        """
        usuario = {
            'nome': input("Nome do usuário: "),
            'email': input("Email: "),
            'cpf': input("CPF: "),
            'estado': input("Estado: "),
            'cidade': input("Cidade: "),
            'rua': input("Rua: "),
            'numero': input("Número: ")
        }
        tx.run(query, **usuario)
        print("Usuário criado com sucesso!")

    def criar_vendedor(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._criar_vendedor)

    @staticmethod
    def _criar_vendedor(tx):
        query = """
        CREATE (v:Vendedor {nome: $nome, email: $email, cnpj: $cnpj})
        """
        vendedor = {
            'nome': input("Nome do vendedor: "),
            'email': input("Email: "),
            'cnpj': input("CNPJ: ")
        }
        tx.run(query, **vendedor)
        print("Vendedor criado com sucesso!")

    def criar_produto(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._criar_produto)

    @staticmethod
    def _criar_produto(tx):
        query = """
        MATCH (v:Vendedor {email: $email_vendedor})
        CREATE (p:Produto {nome: $nome, descricao: $descricao, preco: $preco})
        CREATE (v)-[:VENDE]->(p)
        """
        produto = {
            'nome': input("Nome do produto: "),
            'descricao': input("Descrição: "),
            'preco': input("Preço: "),
            'email_vendedor': input("Email do vendedor: ")
        }
        tx.run(query, **produto)
        print("Produto criado com sucesso e relacionamento estabelecido com o vendedor!")

    def realizar_compra(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._realizar_compra)

    @staticmethod
    def _realizar_compra(tx):
        compra_id = str(random.randint(1, 100000))
        compra = {
            'id': compra_id,
            'produto': input("Nome do produto: "),
            'vendedor': input("Email do vendedor: "),
            'usuario': input("Email do usuário: ")
        }

        query = """
        MATCH (u:Usuario {email: $usuario})
        MATCH (v:Vendedor {email: $vendedor})
        MATCH (p:Produto {nome: $produto})
        CREATE (c:Compra {id: $id})
        CREATE (u)-[:REALIZOU]->(c)
        CREATE (v)-[:VENDEU]->(c)
        CREATE (p)-[:INCLUI]->(c)
        """
        
        tx.run(query, **compra)
        print("Compra realizada com sucesso!")

    def procurar_usuarios(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._procurar_usuarios)

    @staticmethod
    def _procurar_usuarios(tx):
        query = "MATCH (u:Usuario) RETURN u"
        result = tx.run(query)
        for row in result:
            print(row)

    def procurar_vendedores(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._procurar_vendedores)

    @staticmethod
    def _procurar_vendedores(tx):
        query = "MATCH (v:Vendedor) RETURN v"
        result = tx.run(query)
        for row in result:
            print(row)

    def procurar_produtos(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._procurar_produtos)

    @staticmethod
    def _procurar_produtos(tx):
        query = "MATCH (p:Produto) RETURN p"
        result = tx.run(query)
        for row in result:
            print(row)

    def procurar_compras(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._procurar_compras)

    @staticmethod
    def _procurar_compras(tx):
        query = "MATCH (c:Compra) RETURN c"
        result = tx.run(query)
        for row in result:
            print(row)


def menu(app):
    while True:
        print("""
        1 - Novo Usuario
        2 - Novo Vendedor
        3 - Novo Produto
        4 - Nova Compra
        5 - Listar todos Usuarios
        6 - Listar todos Vendedores
        7 - Listar todos Produtos
        8 - Listar todas Compras
        0 - Sair
        """)
        escolha = input("Digite a Operação desejada: ")
        if escolha == '1':
            app.criar_usuario()
        elif escolha == '2':
            app.criar_vendedor()
        elif escolha == '3':
            app.criar_produto()
        elif escolha == '4':
            app.realizar_compra()
        elif escolha == '5':
            app.procurar_usuarios()
        elif escolha == '6':
            app.procurar_vendedores()
        elif escolha == '7':
            app.procurar_produtos()
        elif escolha == '8':
            app.procurar_compras()
        elif escolha == '0':
            print("Até a Próxima!")
            app.close()
            break
        else:
            print("Operação não entendida")


if __name__ == "__main__":
    uri = "neo4j+s://0b4d57fa.databases.neo4j.io:7687"
    user = "neo4j"
    password = "7ORJYUD_V3JlwHLlZuo19KJkCAPWNAiDXX4vn6VgyRQ"
    app = App(uri, user, password)
    menu(app)
