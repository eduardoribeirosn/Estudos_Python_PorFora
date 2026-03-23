# Desafio - Trocando os nomes

import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib.pyplot as plt

# dados simples
dados = {
    "nome": ["Casa", "Empresa", "Roubo"],
    "lat": [-23.55, -23.56, -23.60],
    "lon": [-46.63, -46.64, -46.60]
}

# 1. cria dataframe normal
df = pd.DataFrame(dados)

# 2. cria geometria
geometry = [Point(lon, lat) for lon, lat in zip(df["lat"], df["lon"])]

# 3. cria geoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=geometry)

# 4. Definir CRS - Padrão
gdf.set_crs(epsg=4326, inplace=True)

print(gdf)

gdf.plot()
plt.show()