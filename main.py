from classes.usuario import Usuario
from enums.cargos import Cargos
from classes.livro import Livro
from autenticacao.login import Login
from autenticacao.cadastro import Cadastro

usuarioLogin = Usuario()
usuarioLogin.id = "eb18d659-9b01-49a2-b2e6-e2227e50f2b6"
usuarioLogin.nome = "Gabriel"
usuarioLogin.senha = "admin123"
usuarioLogin.cargo = Cargos.CLIENTE
usuarioLogin.livrosAlugados = []

def menu():
    if not usuarioLogin.nome:
        print('1 - Login')
        print('2 - Cadastro')
        print('3 - Fechar o programa')
        escolha =  input('Escolha uma opção: ')
        match escolha:
            case '1':
                return 'login'
            case '2':
                return 'cadastro'
            case '3':
                return 'sair'
            case _:
                raise ValueError('Opção inválida!')

    elif usuarioLogin.cargo == Cargos.ADMIN:
        print('1 - Registrar um livro')
        print('2 - Excluir um livro')
        print('3 - Listar livros disponíveis')
        print('4 - Alugar livro')
        print('5 - Renovar prazo')
        print('6 - Devolver livro')
        print('7 - Sair')
        escolha =  input('Escolha uma opção: ')
        match escolha:
            case '1':
                return 'registrar'
            case '2':
                return 'excluir'
            case '3':
                return 'listar_disponiveis'
            case '4':
                return 'alugar'
            case '5':
                return 'renovar'
            case '6':
                return 'devolver'
            case '7':
                return 'sair'
            case _:
                raise ValueError('Opção inválida!')
    elif usuarioLogin.cargo == Cargos.CLIENTE:
        print('1 - Listar livros disponíveis')
        print('2 - Alugar livro')
        print('3 - Listar livros alugados por mim')
        print('4 - Renovar prazo')
        print('5 - Devolver livro')
        print('6 - Sair')
        escolha =  input('Escolha uma opção: ')
        match escolha:
            case '1':
                return 'listar_disponiveis'
            case '2':
                return 'alugar'
            case '3':
                return 'listar_alugados_por_usuario'
            case '4':
                return 'renovar'
            case '5':
                return 'devolver'
            case '6':
                return 'sair'
            case _:
                raise ValueError('Opção inválida!')
while True:
    try:
        acao = menu()
        
        match acao:
            case 'login':
                login = Login()
                usuarioLogin = login.usuario
            case 'cadastro':
                cadastro = Cadastro()
                usuarioLogin = cadastro.usuario
                pass
            case 'registrar':
                Livro.registrar()
                pass
            case 'excluir':
                Livro.excluir()
                pass
            case 'alugar':
                Livro.alugar(usuarioLogin)
                pass
            case 'listar_disponiveis':
                Livro.listar_disponiveis()
                pass
            case 'listar_alugados_por_usuario':
                Livro.listar_alugados_por_usuario(usuarioLogin)
                pass
            case 'renovar':
                Livro.renovar(usuarioLogin)
                pass
            case 'devolver':
                Livro.devolver(usuarioLogin)
                pass
            case 'sair':
                break
            case _:
                raise ValueError('Opção inválida!')
    except ValueError:
        print('Opção inválida!')