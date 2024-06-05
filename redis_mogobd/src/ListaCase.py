import json

import Produto.deletar as DeletarUsuario
import Usuario.deletar  as DeletarUsuario
import Usuario.update as AtualizacaoUsuario
import Usuario.CadastroCliente as CadastroCliente
import Usuario.FindQuery as BuscarUsuario
import Produto.Cadastro as CadastroProduto
import Produto.FindQuery as BuscarProdutos
import Produto.update as AtualizarProdutoByID
import Produto.deletar as DeletarProdutoID
import Compra.Cadastro as ComprarProduto
import Usuario.ListaFavoritos as Favoritos
import Compra.FindQuery as BuscaCompra
import vendedor as Vendedor

def CaseUsuario(mydb, conR, auth, token):
    mycol = mydb.Cliente
    users = json.dumps(mycol.find())
    conR.set("users-mongo", users)
    while token:
        print('''Opções\n
    0 - Voltar\n
    1 - Cadastrar usuário\n
    2 - Listar usuários\n
    3 - Buscar usuário por ID\n
    4 - Deletar usuário \n
    5 - Atualizar usuário\n
    6 - Favoritar Produto\n
        ''')
        escolha = input('Escolha uma opção: ')
        auth()
        if token is None:
            return
        else:
            match escolha:
                case '0':
                    return
                case '1':
                    CadastroCliente.CadastrarUsuario(mydb)
                case '2':
                    BuscarUsuario.PegarUsuarios(mydb, conR)
                case '3':
                    BuscarUsuario.UsuariobyID(mydb)
                case '4':
                    DeletarUsuario.DeletarUsuarioID(mydb)
                case '5':
                    AtualizacaoUsuario.AtualizarUsuarioID(mydb)
                case '6':
                    Favoritos.ListaDesejos(mydb)


def CaseProduto(mydb, auth, token):
    while token:
        print('''Opções\n
    0 - Voltar\n
    1 - Cadastrar produto\n
    2 - buscar Produto por nome\n
    3 - Atualizar Produto por ID\n
    4 - Deletar Produto\n
    5 - Listar produtos''')
        escolha = input('escolha Uma Opção:')
        auth()
        if token is None:
            return
        else:
            match escolha:
                case '0':
                    break
                case '1':
                    CadastroProduto.CadastrarProduto(mydb)
                case '2':
                    BuscarProdutos.ProdutosNome(mydb)
                case '3':
                    AtualizarProdutoByID.AtualizarProdutoID(mydb)
                case '4':
                    DeletarProdutoID.DeletarProdutoID(mydb)


def CaseCompra(mydb, auth, token):
    while token:
        print('''Escolha Uma Opções\n
    0 - Voltar\n
    1 - Comprar produto\n
    2 - Buscar todas compras\n
    3 - Buscar compra por id\n''')
        escolha = input('escolha Uma Opção: ')
        auth()
        if token is None:
            return
        else:
            match escolha:
                case '0':
                    return
                case '1':
                    ComprarProduto.Compra(mydb)
                case '2':
                    BuscaCompra.PegarCompras(mydb)
                case '3':
                    BuscaCompra.ComprasbyID(mydb)

def CaseVendedor(mydb, auth, token):
    while token:
        print('''Opções\n
    0 - Voltar\n
    1 - Cadastrar vendedor\n
    2 - Listar vendedores\n
    3 - Deletar vendedor \n
    4 - Atualizar vendedor\n''')
        escolha = input('escolha Uma Opção: ')
        auth()
        if token is None:
            return
        else:
            match escolha:
                case '0':
                    return
                case '1':
                    Vendedor.setVendedor(mydb)
                case '2':
                    Vendedor.listVendedor(mydb)
                case '3':
                    Vendedor.deleteVendedor(mydb)   
                case '4':
                    Vendedor.atualizarVendedor(mydb)
