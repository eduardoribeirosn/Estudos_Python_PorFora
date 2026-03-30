import osmnx as ox
import networkx as nx

local = "Pinheiros, São Paulo, Brazil"

G = ox.graph_from_place(local, network_type="drive")

# ox.plot_graph(G)
# OR OU
# fig, ax = ox.plot_graph(
#     grafo,
#     node_size=15,
#     node_color='red',
#     edge_color='white',
#     bgcolor='black'
# )

origem = (-23.559436, -46.684727)
destino = (-23.565715, -46.686808)

orig_node = ox.nearest_nodes(G, origem[1], origem[0])
dest_node = ox.nearest_nodes(G, destino[1], destino[0])

rota = nx.shortest_path(G, orig_node, dest_node, weight="length")

ox.plot_graph_route(G, rota)