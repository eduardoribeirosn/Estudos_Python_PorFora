import geopandas as pdg
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon

gdf = pdg.read_file("./dados.geojson")

print(gdf)
print(gdf.columns)

gdf.set_crs(epsg=4326, inplace=True)

# Definir cores
cores = {
    "casa": "pink",
    "mercado": "gray"
}

gdf["cor"] = gdf["tipo"].map(cores)

gdf.plot(color=gdf["cor"])
plt.show()