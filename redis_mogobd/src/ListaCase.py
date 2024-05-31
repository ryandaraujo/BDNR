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
import Usuario.ListaDesejo as Desejo
import Compra.FindQuery as BuscaCompra
import Compra.deletar as DeletarCompra
import banco.setUsuario as redis

def CaseUsuario(mydb):
    execucao = True
    while execucao:
        print('''Opções\n
    0 - Voltar\n
    1 - Cadastrar usuário\n
    2 - Visualizar usuários\n
    3 - Usuario por ID\n
    4 - Deletar usuário \n
    5 - Atualizar usuário\n
    6 - favoritar Produto\n
        ''')
        escolha = input('escolha Uma Opção:')
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
                Desejo.ListaDesejos(mydb)


def CaseProduto(mydb):
    execucao = True
    while execucao:
        print('''Opções\n
    0 - Voltar\n
    1 - CadastrarProduto\n
    2 - Pegar Produtos\n
    3 - buscar Produto por ID\n
    4 - Atualizar Produto por ID\n
    5 - Deletar Produto\n''')
        escolha = input('escolha Uma Opção:')
        match escolha:
            case '0':
                break
            case '1':
                CadastroProduto.CadastrarProduto(mydb)
            case '2':
                BuscarProdutos.PegarProdutos(mydb)
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
    1 - ComprarProduto\n
    2 - Deletar Compra\n
    3 - buscar todas Compras\n
    4 - buscar Compra por id\n''')
        escolha = input('escolha Uma Opção:')
        match escolha:
            case '0':
                return
            case '1':
                ComprarProduto.Compra(mydb)
            case '2':
                DeletarCompra.DeletarCompraID(mydb)
            case '3':
                BuscaCompra.PegarCompras(mydb)
            case '4':
                BuscaCompra.ComprasbyID(mydb)
def Caseredis(mydb,conR):
    execucao = True
    while execucao:
        print('''Opções\n
    0 - Voltar\n
    1 - SetUsuario Redis\n
    2 - Verificar Conta\n
    3 - DetUsuario Redis\n
    4 - ListUsuario Redis\n
    5 - Cadastro Lista de desejos Redis\n''')
        escolha = input('escolha Uma Opção: ')
        match escolha:
            case '0':
                return
            case '1':
                redis.SetUsuarios(mydb,conR)
            case '2':
                redis.SetToken(mydb,conR)
            case '3':
                redis.deletaRedis(conR)
            case '4':
                redis.getUsuariosRedis(conR)   
            case '5':
                redis.setListaFavoritos(mydb,conR)