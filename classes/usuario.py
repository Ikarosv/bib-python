from enums.cargos import Cargos
from dbs.seed import usuarios, arquivo_usuarios
import uuid
import json

# arquivo_usuarios = Path(__file__).with_name('usuarios.json')

class Usuario():
    id: str
    nome: str
    senha: str
    cargo: str
    livrosAlugados: list[str]
    def __init__(self):
        self.id = ''
        self.nome = ''
        self.senha = ''
        self.cargo = Cargos.CLIENTE
    
    def autenticar(self, nome: str, senha: str) -> bool:
        user = self.getUser(nome)
        if user:
            if user['senha'] == senha:
                self.id = user['id']
                self.nome = user['nome']
                self.cargo = Cargos[user['cargo'].upper()]
                self.livrosAlugados = user['livrosAlugados']
                return True
        return False
    
    def cadastrar(self, nome: str, senha: str, cargo: str):
        self.nome = nome
        self.senha = senha
        self.cargo = cargo
        self.livrosAlugados = []
        self.id = str(uuid.uuid4())
        usuarios.append(self.__dict__)
        with open(arquivo_usuarios, 'w') as f:
            json.dump(usuarios, f, ensure_ascii=False, indent=2)
            f.close()
        
        self.cargo = Cargos[self.cargo.upper()]
        return self

    def addLivro(self, nome_livro: str):
        self.livrosAlugados.append(nome_livro)
        usuario = self.getUser(self.nome)
        if usuario:
            usuario['livrosAlugados'] = self.livrosAlugados
            with open(arquivo_usuarios, 'w', encoding='utf-8') as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=2)
                f.close()

    def removeLivro(self, nome_livro: str):
        if nome_livro in self.livrosAlugados:
            self.livrosAlugados.remove(nome_livro)
            usuario = self.getUser(self.nome)
            if usuario:
                usuario['livrosAlugados'] = self.livrosAlugados
                with open(arquivo_usuarios, 'w', encoding='utf-8') as f:
                    json.dump(usuarios, f, ensure_ascii=False, indent=2)
                    f.close()

    def getUser(self, nome: str):
        return next(filter(lambda u: u['nome'] == nome, usuarios), None)