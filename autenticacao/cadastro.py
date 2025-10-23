from enums.cargos import Cargos
from classes.usuario import Usuario

class Cadastro:
    def __init__(self):
        self.nome = input("Digite seu nome: ")
        self.senha = input("Digite sua senha: ")
        self.confirmar_senha = input("Confirme sua senha: ")
        if self.senha != self.confirmar_senha:
            print("As senhas não coincidem. Tente novamente.")
            return
        self.cargo = Cargos.CLIENTE.name.lower()
        self.usuario = Usuario().cadastrar(self.nome, self.senha, self.cargo)
        print(f'Usuário {self.usuario.nome} cadastrado com sucesso!')

if __name__ == '__main__':
    Cadastro()