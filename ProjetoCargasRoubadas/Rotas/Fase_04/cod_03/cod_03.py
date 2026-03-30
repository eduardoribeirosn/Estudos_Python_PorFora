import osmnx as ox
import networkx as nx
import geopandas as gpd
from shapely.geometry import Point

cidade = "São Paulo, Brazil"

G = ox.graph_from_place(cidade, network_type="drive")

fix, ax = ox.plot_graph(
    G,
    figsize=(30, 30),
    dpi=300,
    node_size=0,
    edge_linewidth=0.2,
    edge_color="white",
    bgcolor="black"
)

# fig.save("sao_paulo_alta_resolucao.png", dpi=300, bbox_inches="tight")