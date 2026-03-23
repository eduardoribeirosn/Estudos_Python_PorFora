# Desafio - Escolhendo a Cor das bolinhas/legenda

import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib.pyplot as plt

# dados simples
dados = {
    "nome": ["Casa", "Marlene", "Santos Amaro"],
    "tipo": ["Casa", "Escola", "Escola"],
    "lat": [-23.585767, -23.579787, -23.584793],
    "lon": [-46.533733, -46.540092, -46.527555]
}

# 1. cria dataframe normal
df = pd.DataFrame(dados)

# 2. cria geometria
geometry = [Point(lon, lat) for lon, lat in zip(df["lat"], df["lon"])]

# 3. cria geoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=geometry)

# 4. Definir CRS - Padrão
gdf.set_crs(epsg=4326, inplace=True)

# 5. Definir cores
cores = {
    "Casa": "pink",
    "Escola": "black"
}
gdf["cor"] = gdf["tipo"].map(cores)

print(gdf)

gdf.plot(column="tipo", legend=True, color=gdf["cor"])
plt.show()