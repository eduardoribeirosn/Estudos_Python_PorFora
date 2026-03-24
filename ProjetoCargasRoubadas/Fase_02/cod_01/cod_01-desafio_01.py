# Coloquei 3 roubos no mesmo lugar (Lugar do roubo 1)

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from geopandas.tools import sjoin
from shapely.geometry import Polygon

# Criação dos pontos
roubos = gpd.read_file("./dadosRoubos.geojson")
roubos.set_crs(epsg=4326, inplace=True)
# Transformar o ponto em poligono (transformar em área)
roubos["geometry"] = roubos.buffer(0.001)

# Criação do bairro
dadosBairro01 = {
    "nome": ["Butantã"],
    "tipo": ["bairro"],
    "bairro": [Polygon([
        (-46.740, -23.5750),
        (-46.720, -23.5750),
        (-46.720, -23.5850),
        (-46.740, -23.5850),
    ])]
}
# Transforma o dicionario em DataFrame
dfBairro = pd.DataFrame(dadosBairro01)
# Transforma em um GeoDataFrame
bairros = gpd.GeoDataFrame(dfBairro, geometry=dadosBairro01["bairro"], crs="EPSG:4326")

# Realiza o sjoin para juntar os 2 GeoDataFrame
gdf = sjoin(roubos, bairros, how="left", predicate="within")

# Mostrar na Tela
ax = bairros.plot(color="none", edgecolor="red")

gdf.plot(ax=ax, color="blue", alpha=0.3)
plt.show()

# print(gdf)
print(gdf.groupby("bairro").size())