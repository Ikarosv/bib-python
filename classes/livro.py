import uuid
from classes.usuario import Usuario
from enums.status import Status
from dbs.seed import arquivo_estoque, estoque
import json
import datetime

class Livro():
    id: str
    nome: str
    status: Status
    categoria: str
    alugadoPor: str | None
    alugadoDia: datetime.datetime | None
    devolverDia: datetime.datetime | None
    
    def __init__(self, nome: str, categoria: str, status: Status = Status.DISPONIVEL):
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.status = status
        self.categoria = categoria
        self.alugadoPor = None
        self.alugadoDia = None
        self.devolverDia = None
    
    def registrar():
        nome = input('Digite o nome do livro: ')
        categoria = input('Digite a categoria do livro: ')
        novo_livro = Livro(nome, categoria, Status.DISPONIVEL.name.lower())
        
        estoque.append(novo_livro.__dict__)
        with open(arquivo_estoque, 'w', encoding='utf-8') as f:
            json.dump(estoque, f, ensure_ascii=False, indent=2)
            f.close()
        
        print(f'Livro {novo_livro.nome} registrado com sucesso!')
    
    def excluir():
        nome = input('Digite o nome do livro: ')
        livro = next(filter(lambda l: l['nome'] == nome, estoque), None)
        if livro:
            estoque.remove(livro)
            with open(arquivo_estoque, 'w', encoding='utf-8') as f:
                json.dump(estoque, f, ensure_ascii=False, indent=2)
                f.close()
            print(f'Livro {livro["nome"]} excluído com sucesso!')
        else:
            print(f'Livro {nome} não encontrado!')
    
    def alugar(usuario: Usuario):
        nome = input('Digite o nome do livro que deseja alugar: ')
        livro = next(filter(lambda l: l['nome'].lower() == nome.lower() and l['status'] == Status.DISPONIVEL.name.lower(), estoque), None)
        if livro:
            Livro.atualizar_status(Status.ALUGADO, usuario.id, nome)
            usuario.addLivro(nome)
            print(f'Livro {livro["nome"]} alugado com sucesso por {usuario.nome}!')
        else:
            print(f'Livro {nome} não disponível para aluguel!')
    
    def devolver(usuario: Usuario):
        nome = input('Digite o nome do livro que deseja devolver: ')
        livro = next(filter(lambda l: l['nome'].lower() == nome.lower() and l['alugadoPor'] == usuario.id, estoque), None)
        if livro:
            Livro.atualizar_status(Status.DISPONIVEL, None, nome)
            usuario.removeLivro(nome)
            print(f'Livro {livro["nome"]} devolvido com sucesso por {usuario.nome}!')
        else:
            print(f'Livro {nome} não encontrado entre os alugados por {usuario.nome}!')
    
    def renovar(usuario: Usuario):
        nome = input('Digite o nome do livro que deseja renovar: ')
        livro = next(filter(lambda l: l['nome'].lower() == nome.lower() and l['alugadoPor'] == usuario.id, estoque), None)
        if livro:
            if datetime.datetime.now() > datetime.datetime.fromisoformat(livro['devolverDia']):
                print(f'O prazo para renovação do livro {livro["nome"]} já expirou. Por favor, devolva o livro primeiro.')
            else:
                livro['devolverDia'] = (datetime.datetime.fromisoformat(livro['devolverDia']) + datetime.timedelta(days=7)).isoformat()
                with open(arquivo_estoque, 'w', encoding='utf-8') as f:
                    json.dump(estoque, f, ensure_ascii=False, indent=2)
                    f.close()
                print(f'Prazo para renovação do livro {livro["nome"]} atualizado com sucesso!')

    
    def listar_disponiveis():
        livros_disponiveis = list(filter(lambda l: l['status'].lower() == Status.DISPONIVEL.name.lower(), estoque))
        if livros_disponiveis:
            print('-' * 30)
            print('Livros disponíveis para aluguel:')
            print('=' * 30)
            for livro in livros_disponiveis:
                print(f'- {livro["nome"]} (Categoria: {livro["categoria"]})')
            print('-' * 30)
        else:
            print('Nenhum livro disponível para aluguel.')
    
    def listar_alugados_por_usuario(usuario: Usuario):
        livros_alugados = list(filter(lambda l: l['alugadoPor'] == usuario.id, estoque))
        if livros_alugados:
            print(f'Livros alugados por {usuario.nome}:')
            for livro in livros_alugados:
                print(f'- {livro["nome"]} (Categoria: {livro["categoria"]})')
        else:
            print(f'Nenhum livro alugado por {usuario.nome}.')
    
    def atualizar_status(status: Status, usuario: str | None, nome_livro: str):
        livro = next(filter(lambda l: l['nome'].lower() == nome_livro.lower(), estoque), None)
        if livro:
            livro['status'] = status.name.lower()
            if status == Status.ALUGADO:
                livro['alugadoPor'] = usuario
                livro['alugadoDia'] = datetime.datetime.now().isoformat()
                # 7 dias para devolver
                livro['devolverDia'] = (datetime.datetime.now() + datetime.timedelta(days=7)).isoformat()
            else:
                livro['alugadoPor'] = None
                livro['alugadoDia'] = None
                livro['devolverDia'] = None
            with open(arquivo_estoque, 'w', encoding='utf-8') as f:
                json.dump(estoque, f, ensure_ascii=False, indent=2)
                f.close()
        else:
            print(f'Livro {nome_livro} não encontrado!')
    
    def categorias_disponiveis():
        categorias = set(l['categoria'] for l in estoque if l['status'] == Status.DISPONIVEL.name.lower() and l['categoria'])
        return categorias
    
    def listar_por_categoria():
        categorias = Livro.categorias_disponiveis()
        if not categorias:
            print('Nenhuma categoria disponível.')
            return
        print('Categorias disponíveis:')
        for categoria in categorias:
            print(f'- {categoria}')
        print('-' * 30)
        categoria = input('Digite a categoria que deseja listar: ')
        livros_categoria = list(filter(lambda l: l['categoria'].lower() == categoria.lower(), estoque))
        if livros_categoria:
            print(f'Livros na categoria {categoria}:')
            for livro in livros_categoria:
                status = 'Disponível' if livro['status'].lower() == Status.DISPONIVEL.name.lower() else 'Alugado'
                print(f'- {livro["nome"]} (Status: {status})')
        else:
            print(f'Nenhum livro encontrado na categoria {categoria}.')