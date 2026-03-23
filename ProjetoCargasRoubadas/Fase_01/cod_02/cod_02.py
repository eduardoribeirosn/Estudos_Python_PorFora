# Código para plotar LINHAS

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString

dados = {
    "Nome": ["Rota até o Marlene"],
    "Tipo": ["Trajeto"],
    "lat": [[-23.55, -23.56, -23.57]],
    "lon": [[-46.63, -46.64, -46.65]]
}

# 1.
df = pd.DataFrame(dados)

# 2. - LineString
arrayCoords = []
for item in zip(df["lon"][0], df["lat"][0]):
    arrayCoords.append(item)
linha = LineString(arrayCoords)

# 3.
gdf = gpd.GeoDataFrame(df, geometry=[linha])

# 4.
gdf.set_crs(epsg=4326, inplace=True)

# ....
gdf.plot()
plt.show()