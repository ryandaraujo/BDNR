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

def CaseUsuario(mydb):
    execucao = True
    while execucao:
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
        match escolha:
            case '0':
                return
            case '1':
                CadastroCliente.CadastrarUsuario(mydb)
            case '2':
                BuscarUsuario.PegarUsuarios(mydb)
            case '3':
                BuscarUsuario.UsuariobyID(mydb)
            case '4':
                DeletarUsuario.DeletarUsuarioID(mydb)
            case '5':
                AtualizacaoUsuario.AtualizarUsuarioID(mydb)
            case '6':
                Favoritos.ListaDesejos(mydb)


def CaseProduto(mydb):
    execucao = True
    while execucao:
        print('''Opções\n
    0 - Voltar\n
    1 - Cadastrar produto\n
    3 - buscar Produto por ID\n
    4 - Atualizar Produto por ID\n
    5 - Deletar Produto\n''')
        escolha = input('escolha Uma Opção:')
        match escolha:
            case '0':
                break
            case '1':
                CadastroProduto.CadastrarProduto(mydb)
            case '3':
                BuscarProdutos.ProdutosbyID(mydb)
            case '4':
                AtualizarProdutoByID.AtualizarProdutoID(mydb)
            case '5':
                DeletarProdutoID.DeletarProdutoID(mydb)
                


def CaseCompra(mydb):
    execucao = True
    while execucao:
        print('''Escolha Uma Opções\n
    0 - Voltar\n
    1 - Comprar produto\n
    2 - Buscar todas compras\n
    3 - Buscar compra por id\n''')
        escolha = input('escolha Uma Opção: ')
        match escolha:
            case '0':
                return
            case '1':
                ComprarProduto.Compra(mydb)
            case '2':
                BuscaCompra.PegarCompras(mydb)
            case '3':
                BuscaCompra.ComprasbyID(mydb)

def CaseVendedor(mydb):
    execucao = True
    while execucao:
        print('''Opções\n
    0 - Voltar\n
    1 - Cadastrar vendedor\n
    2 - Listar vendedores\n
    3 - Deletar vendedor \n
    4 - Atualizar vendedor\n''')
        escolha = input('escolha Uma Opção: ')
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