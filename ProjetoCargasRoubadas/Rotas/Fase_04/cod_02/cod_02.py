import osmnx as ox
import networkx as nx
import geopandas as gpd
from geopandas.tools import sjoin
from scipy.stats import alpha
from shapely.geometry import Point

local = "Pinheiros, São Paulo, Brazil"

G = ox.graph_from_place(local, network_type="drive")

origem = (-23.559436, -46.684727)
destino = (-23.565715, -46.686808)

orig_node = ox.nearest_nodes(G, origem[1], origem[0])
dest_node = ox.nearest_nodes(G, destino[1], destino[0])

# MODIFICAR PESOS NA ROTA
# Quebrar grafo em nodes e edges
nodes, edges = ox.graph_to_gdfs(G)

# Criação dos roubos ficticios
dados = {
    "roubos": [5, 10, 2],
    "geometry": [
        Point(-46.686518, -23.560533),
        Point(-46.683890, -23.563905),
        Point(-46.685177, -23.562145)
    ]
}

# Transformando roubos em GeoDataFrame
roubos = gpd.GeoDataFrame(dados, crs="EPSG:4326")

# Transformando os pontos de roubo em buffer (área)
roubos = roubos.to_crs(epsg=3857)
edges = edges.to_crs(epsg=3857)
roubos["buffer"] = roubos.buffer(300)

# Inserir quais ruas passam por risco
edges["risco"] = edges.intersects(roubos["buffer"].union_all())

# Colocar pesos nas ruas que tem perigo
edges["peso"] = edges["length"]
edges.loc[edges["risco"] == True, "peso"] *= 5

# Voltar CRS
edges = edges.to_crs(epsg=4326)
roubos = roubos.to_crs(epsg=4326)

# Criar grafo atualizado
G = ox.graph_from_gdfs(nodes, edges)

edges[edges["risco"]].to_crs(4326).plot()

# Criar rotas baseadas em perigo e tempo
rotaSegura = nx.shortest_path(G, orig_node, dest_node, weight="peso")
rotaCurta = nx.shortest_path(G, orig_node, dest_node, weight="length")

# Mostrar Mapa + area de roubo
tGDF = sjoin(roubos, edges, how="left", predicate="within")
ax = edges.plot()
roubos.plot(ax=ax, alpha=0.3)
# edges.plot()

ox.plot_graph_route(G, rotaCurta)
ox.plot_graph_route(G, rotaSegura)

print(edges["risco"].value_counts())