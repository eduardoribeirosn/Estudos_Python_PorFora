import psycopg2

conn = psycopg2.connect(
    dbname="base_roubos",
    user="postgres",
    password="Stusrt#9125",
    host="localhost",
    port="5432",
)

cursor = conn.cursor()

# Pegar as coordenadas de todas as linhas.
cursor.execute("SELECT longitude, latitude FROM roubos ORDER BY id")
list_coordenadas = cursor.fetchall()

for i, coordenadas_atual in enumerate(list_coordenadas):
    if list_coordenadas[i][0] == None or list_coordenadas[i][1] == None or list_coordenadas[i][0] == "NULL" or list_coordenadas[i][1] == "NULL":
        print("Campos nulos.")
    else:
        print(coordenadas_atual)
        cursor.execute(f"UPDATE roubos SET geometria = ST_SetSRID(St_MakePoint(%s, %s), 4326) WHERE id = %s", (float(coordenadas_atual[0].replace(",", ".")), float(coordenadas_atual[1].replace(",", ".")), (i + 1)))

conn.commit()


# cursor.execute("UPDATE roubos SET geometria = ST_SetSRID(St_MakePoint(-46.63, -23.55), 4326) WHERE id = 3")
#
# conn.commit()