import random

lista = []

for i in range(100):
    lista.append(i + 1)

listaGerados = random.sample(lista, 20)

listaPar = []
listaImpar = []

for i in range(len(listaGerados)):
    if (listaGerados[i] % 2 == 0):
        listaPar.append(listaGerados[i])
    else:
        listaImpar.append(listaGerados[i])

print(f"Lista: {listaGerados}\n"
      f"Pares: {listaPar}\n"
      f"Impares: {listaImpar}")