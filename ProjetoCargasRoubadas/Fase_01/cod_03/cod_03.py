# Código para plotar POLÍGONOS

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon

dados = {
    "Nome": ["Região com Perigo Leve"],
    "Tipo": ["Perigo-Leve"],
    "lat": [[-23.55, -23.55, -23.56, -23.56]],
    "lon": [[-46.63, -46.64, -46.64, -46.63]]
}

# 1.
df = pd.DataFrame(dados)

# 2. - LineString
arrayCoords = []
for item in zip(df["lon"][0], df["lat"][0]):
    arrayCoords.append(item)
linha = Polygon(arrayCoords)

# 3.
gdf = gpd.GeoDataFrame(df, geometry=[linha])

# 4.
gdf.set_crs(epsg=4326, inplace=True)

# ....
gdf.plot()
plt.show()