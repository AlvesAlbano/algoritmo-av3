import pandas as pd
import json
from collections import defaultdict, deque

def carregar_datasets(movies_path, credits_path):
    try:
        movies = pd.read_csv(movies_path)
        credits = pd.read_csv(credits_path)
        return movies, credits
    except FileNotFoundError as e:
        print(f"Erro: {e}")
        return None, None

def construir_grafo(credits):
    grafo = defaultdict(list)
    filmes_atores = defaultdict(list)  # Mapeia filmes para os atores que participaram

    for _, row in credits.iterrows():
        try:
            # Parsear o JSON na coluna 'cast'
            elenco = json.loads(row['cast'])
            filme_id = row['movie_id']
            atores = [ator['name'] for ator in elenco if 'name' in ator]
            
            # Registrar atores no filme
            filmes_atores[filme_id] = atores
            
            # Conectar atores no grafo
            for i in range(len(atores)):
                for j in range(i + 1, len(atores)):
                    grafo[atores[i]].append((atores[j], filme_id))
                    grafo[atores[j]].append((atores[i], filme_id))
        except (json.JSONDecodeError, TypeError):
            continue  # Ignorar linhas com dados malformados
    return grafo, filmes_atores

def encontrar_caminho(grafo, filmes_atores, ator1, ator2):
    if ator1 not in grafo or ator2 not in grafo:
        return None

    visitados = set()
    fila = deque([(ator1, [ator1], [])])  # (Ator atual, Caminho de atores, Caminho de filmes)

    while fila:
        atual, caminho_atores, caminho_filmes = fila.popleft()
        if atual == ator2:
            return caminho_atores, caminho_filmes

        visitados.add(atual)

        for vizinho, filme_id in grafo[atual]:
            if vizinho not in visitados:
                fila.append((vizinho, caminho_atores + [vizinho], caminho_filmes + [filme_id]))
    
    return None

# Caminhos para os datasets
movies_path = 'tmdb_5000_movies.csv'
credits_path = 'tmdb_5000_credits.csv'

# Etapa 1: Carregar datasets
movies, credits = carregar_datasets(movies_path, credits_path)

if movies is not None and credits is not None:
    # Etapa 2: Construir grafo
    grafo_atores, filmes_atores = construir_grafo(credits)

    # Etapa 3: Encontrar o caminho entre dois atores
    ator1 = "Kevin Bacon"
    ator2 = "Leonardo DiCaprio"
    resultado = encontrar_caminho(grafo_atores, filmes_atores, ator1, ator2)

    if resultado:
        caminho_atores, caminho_filmes = resultado
        print(f"Caminho entre {ator1} e {ator2}:")
        for i in range(len(caminho_atores) - 1):
            filme_id = caminho_filmes[i]
            filme_nome = movies[movies['id'] == filme_id]['title'].values[0]
            print(f"{caminho_atores[i]} -> ({filme_nome}) -> {caminho_atores[i + 1]}")
    else:
        print(f"Nenhuma conexão encontrada entre {ator1} e {ator2}.")
else:
    print("Erro ao carregar os datasets. Verifique os caminhos e os arquivos.")
