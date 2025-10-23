from classes.usuario import Usuario

class Login:
    usuario: Usuario
    def __init__(self):
        self.usuario = Usuario()
        nome = input('Digite seu nome de usuário: ')
        senha = input('Digite sua senha: ')

        if self.usuario.autenticar(nome, senha):
            print(f'Bem-vindo, {self.usuario.nome}!')
        else:
            print('Nome de usuário ou senha incorretos.')

if __name__ == '__main__':
    Login()