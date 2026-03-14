import random

listaGerados = random.sample(range(100), 10)

maiorN = listaGerados[0]
menorN = listaGerados[1]

for i in range(len(listaGerados)):
    if listaGerados[i] > maiorN:
        maiorN = listaGerados[i]
    elif listaGerados[i] < menorN:
        menorN = listaGerados[i]

print(f"Lista = {listaGerados}\n"
      f"Maior: {maiorN}\n"
      f"Menor: {menorN}")
