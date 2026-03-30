import osmnx as ox
import os
import networkx as nx
# import geopandas as gpd
# from geopandas.tools import sjoin
# from shapely.geometry import Point
import psycopg2

# Conecta com o Banco de Dados
conn = psycopg2.connect(
    dbname="base_roubos",
    user="postgres",
    password="Stusrt#9125",
    host="localhost",
    port="5432",
)

cursor = conn.cursor()

# ------------------------------

# CARREGAR Local

ox.settings.use_cache = True
ox.settings.log_console = True
ox.settings.timeout = 300
# ox.settings.overpass_settings = "https://overpass.kumi.systems/api/interpreter"

# Nome do arquivo onde vamos "salvar o jogo"
arquivo_grafo = "grafo_test-zdu_01.graphml"

# Verifica se o arquivo já existe na mesma pasta do seu projeto no PyCharm
if not os.path.exists(arquivo_grafo):
    print("Baixando o mapa de 'Test-zdu_01' (Isso vai demorar um pouco)...")
    # Baixa da internet
    # north = -23.506629
    # south = -23.520323
    # east = -46.554999
    # west = -46.569210
    # G = ox.graph_from_bbox((north, south, east, west), network_type="drive")
    # G = ox.graph_from_place(", Brazil", network_type="drive")
    centro = (-23.512, -46.562)

    G = ox.graph_from_point(
        centro,
        dist=800,
        network_type="drive"
    )

    print("Salvando o mapa no disco rígido...")
    # Salva o grafo no seu computador
    ox.save_graphml(G, filepath=arquivo_grafo)
    print("Mapa salvo com sucesso!")

else:
    print("Mapa já encontrado no PC! Carregando do disco...")
    # Carrega o arquivo local (Muito mais rápido!)
    G = ox.load_graphml(filepath=arquivo_grafo)
    print("Mapa carregado instantaneamente!")

# Imprime o tamanho real do monstro que você baixou
print(f"Total de cruzamentos (Nós): {len(G.nodes)}")
print(f"Total de ruas (Arestas): {len(G.edges)}")

print()
print()
# -----------------------------------------------------

# RANGE (-46.562273, -23.508672)
# RANGE (-46.561758, -23.567501)
# RANGE (-46.666471, -23.559638)
# RANGE (-46.679174, -23.502221)

origem = (-23.520226, -46.568158)
destino = (-23.505964, -46.555841)

orig_node = ox.nearest_nodes(G, origem[1], origem[0])
dest_node = ox.nearest_nodes(G, destino[1], destino[0])

rotaCurta = nx.shortest_path(G, orig_node, dest_node, weight="length")

coords = [(G.nodes[node]["y"], G.nodes[node]["x"]) for node in rotaCurta]

print(coords[:10])

# ox.plot_graph_route(G, rotaCurta)

# COISAS PARA O PRÓXIMO DIA.. NÃO GERAR O MAPA E SIM SÓ A ROTA...