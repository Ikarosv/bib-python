from pathlib import Path
from enums.status import Status
from enums.cargos import Cargos
import uuid
import json

arquivo_estoque = Path(__file__).with_name('estoque.json')
arquivo_usuarios = Path(__file__).with_name('usuarios.json')

# Se ainda não existir o JSON, cria a partir dos dados atuais
if not arquivo_estoque.exists():
    estoque_seed = [
    {'nome':'The Wicther - O último Desejo','status': Status.DISPONIVEL.name.lower()}, 
    {'nome':'The Witcher - A Espada do Destino', 'status': Status.DISPONIVEL.name.lower()}, 
    {'nome':'The Witcher - O Sangue dos Elfos', 'status': Status.DISPONIVEL.name.lower()}, 
    {'nome':'The Wicther - Tempo de Desprezo', 'status': Status.DISPONIVEL.name.lower()}, 
    {'nome':'The Witcher - Batismo de Fogo', 'status': Status.DISPONIVEL.name.lower()}, 
    {'nome':'The Witcher - A Torre da Andorinha', 'status': Status.DISPONIVEL.name.lower()}, 
    {'nome':'The Wicther - A Senhora do Lago', 'status': Status.DISPONIVEL.name.lower()},
    {'nome':'The Witcher - Tempo de Tempestade', 'status': Status.DISPONIVEL.name.lower()},
    {'nome':'Introduction to Algorithms', 'status': Status.DISPONIVEL.name.lower()},
    {'nome':'Cyberpunk 2077 - Nenhum Acaso', 'status': Status.DISPONIVEL.name.lower()},
    {'nome':'Memórias Póstumas de Brás Cubas', 'status': Status.DISPONIVEL.name.lower()},
    {'nome':'Vidas Secas', 'status': Status.DISPONIVEL.name.lower()},
    {'nome':'Don Quixote', 'status': Status.DISPONIVEL.name.lower()},
    {'nome':'A Revolução dos Bichos', 'status': Status.DISPONIVEL.name.lower()},
    {'nome':'Sapiens - Uma Breve História da Humanidade', 'status': Status.DISPONIVEL.name.lower()},
    {'nome':'Duna', 'status': Status.DISPONIVEL.name.lower()},
    {'nome':'O Hobbit', 'status': Status.DISPONIVEL.name.lower()},
    {'nome':'As Crônicas de Nárnia', 'status': Status.DISPONIVEL.name.lower()},
    {'nome':'O Senhor dos Anéis', 'status': Status.DISPONIVEL.name.lower()},
    {'nome':'Neuromancer', 'status': Status.DISPONIVEL.name.lower()},
    {'nome':'O Silmarillion', 'status': 'Disponivel'},
    {'nome':'Contos Inacabados e Os Filhos de Húrin', 'status': Status.DISPONIVEL.name.lower()},
    {'nome':'Coraline', 'status': Status.DISPONIVEL.name.lower()},
    {'nome':'O Oceano no Fim do Caminho', 'status': Status.DISPONIVEL.name.lower()},
    {'nome':'Stardust', 'status': Status.DISPONIVEL.name.lower()},
    {'nome':'Elementos da Matemática - Rufino', 'status': Status.DISPONIVEL.name.lower()},
    {'nome':'Aprendendo a Aprender', 'status': Status.DISPONIVEL.name.lower()},
    {'nome':'A história Sem Fim', 'status': Status.DISPONIVEL.name.lower()},
    {'nome':'Circe', 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "O Pêndulo de Foucault", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "Admirável Mundo Novo", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "1984", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "O Pequeno Príncipe", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "Um Estudo em Vermelho", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "O Signo dos Quatro", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "As Aventuras de Sherlock Holmes", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "Memórias de Sherlock Holmes", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "O Cão dos Baskerville", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "A Volta de Sherlock Holmes", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "O Vale do Medo", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "Os Últimos Casos de Sherlock Holmes", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "A Metamorfose", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "Os Miseráveis", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "Moby Dick", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "Histórias Extraordinárias", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "As Viagens de Gulliver", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "A Cor Que Caiu do Céu", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "Harry Potter e a Pedra Filosofal", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "Harry Potter e a Câmara Secreta", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "Harry Potter e o Prisioneiro de Azkaban", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "Harry Potter e o Cálice de Fogo", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "Harry Potter e a Ordem da Fênix", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "Harry Potter e o Enigma do Príncipe", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "Harry Potter e as Relíquias da Morte", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "Livro das Mil e Uma Noites", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "As Aventuras de Alice no País das Maravilhas", 'status': Status.DISPONIVEL.name.lower()},
    {'nome': "Estrangeiro", 'status': Status.DISPONIVEL.name.lower()}]
    for item in estoque_seed:
        item['id'] = str(uuid.uuid4())
        item['categoria'] = None
        item['alugadoPor'] = None
        item['alugadoDia'] = None
        item['devolverDia'] = None
        
    with arquivo_estoque.open('w', encoding='utf-8') as f:
        json.dump(estoque_seed, f, ensure_ascii=False, indent=2)

# Carrega do JSON
with arquivo_estoque.open('r', encoding='utf-8') as f:
    estoque = json.load(f)

# Cria o JSON se não existir
if not arquivo_usuarios.exists():
    usuarios_seed = [
        {
            'id': str(uuid.uuid4()),
            'nome': 'Gabriel',
            'senha': 'admin123',
            'cargo': Cargos.ADMIN.name.lower(),
            'livrosAlugados': []
        },
        {
            'id': str(uuid.uuid4()),
            'nome': 'Cliente',
            'senha': 'cliente123',
            'cargo': Cargos.CLIENTE.name.lower(),
            'livrosAlugados': []
        }
    ]
    with arquivo_usuarios.open('w', encoding='utf-8') as f:
        json.dump(usuarios_seed, f, ensure_ascii=False, indent=2)

# Carrega e migra (caso já exista)
with arquivo_usuarios.open('r', encoding='utf-8') as f:
    usuarios = json.load(f)
