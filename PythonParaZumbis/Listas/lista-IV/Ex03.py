import random

listaA = random.sample(range(100), 10)
listaB = random.sample(range(100), 10)

novaLista = []
for i in range(len(listaA)):
    novaLista.append(listaA[i])
    novaLista.append(listaB[i])

print(f"Lista A: {listaA}\n"
      f"Lista B: {listaB}\n"
      f"Nova Lista: {novaLista}")