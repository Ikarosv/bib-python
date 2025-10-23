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
    {'nome':'The Wicther - O último Desejo','status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'}, 
    {'nome':'The Witcher - A Espada do Destino', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'}, 
    {'nome':'The Witcher - O Sangue dos Elfos', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'}, 
    {'nome':'The Wicther - Tempo de Desprezo', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'}, 
    {'nome':'The Witcher - Batismo de Fogo', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'}, 
    {'nome':'The Witcher - A Torre da Andorinha', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'}, 
    {'nome':'The Wicther - A Senhora do Lago', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome':'The Witcher - Tempo de Tempestade', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome':'Introduction to Algorithms', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Educacional'},
    {'nome':'Cyberpunk 2077 - Nenhum Acaso', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome':'Memórias Póstumas de Brás Cubas', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Romance'},
    {'nome':'Vidas Secas', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Romance'},
    {'nome':'Don Quixote', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Romance'},
    {'nome':'A Revolução dos Bichos', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Alegoria Política'},
    {'nome':'Sapiens - Uma Breve História da Humanidade', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Antropologia'},
    {'nome':'Duna', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Romance'},
    {'nome':'O Hobbit', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome':'As Crônicas de Nárnia', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome':'O Senhor dos Anéis', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome':'Neuromancer', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Romance'},
    {'nome':'O Silmarillion', 'status': 'Disponivel', 'categoria': 'Fantasia'},
    {'nome':'Contos Inacabados e Os Filhos de Húrin', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome':'Coraline', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome':'O Oceano no Fim do Caminho', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Romance'},
    {'nome':'Stardust', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Romance'},
    {'nome':'Elementos da Matemática - Rufino', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Educacional'},
    {'nome':'Aprendendo a Aprender', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Educacional'},
    {'nome':'A história Sem Fim', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Romance'},
    {'nome':'Circe', 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Romance'},
    {'nome': "O Pêndulo de Foucault", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Romance'},
    {'nome': "Admirável Mundo Novo", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Romance'},
    {'nome': "1984", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Alegoria Política'},
    {'nome': "O Pequeno Príncipe", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome': "Um Estudo em Vermelho", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Romance'},
    {'nome': "O Signo dos Quatro", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Romance'},
    {'nome': "As Aventuras de Sherlock Holmes", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome': "Memórias de Sherlock Holmes", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome': "O Cão dos Baskerville", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Romance'},
    {'nome': "A Volta de Sherlock Holmes", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome': "O Vale do Medo", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Terror'},
    {'nome': "Os Últimos Casos de Sherlock Holmes", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome': "A Metamorfose", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Romance'},
    {'nome': "Os Miseráveis", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Romance'},
    {'nome': "Moby Dick", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Romance'},
    {'nome': "Histórias Extraordinárias", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Terror'},
    {'nome': "As Viagens de Gulliver", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Romance'},
    {'nome': "A Cor Que Caiu do Céu", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome': "Harry Potter e a Pedra Filosofal", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome': "Harry Potter e a Câmara Secreta", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome': "Harry Potter e o Prisioneiro de Azkaban", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome': "Harry Potter e o Cálice de Fogo", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome': "Harry Potter e a Ordem da Fênix", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome': "Harry Potter e o Enigma do Príncipe", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome': "Harry Potter e as Relíquias da Morte", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome': "Livro das Mil e Uma Noites", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome': "As Aventuras de Alice no País das Maravilhas", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Fantasia'},
    {'nome': "Estrangeiro", 'status': Status.DISPONIVEL.name.lower(), 'categoria': 'Romance'}]
    for item in estoque_seed:
        item['id'] = str(uuid.uuid4())
        if 'categoria' not in item:
            item['categoria'] = ''
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