# Para importar uma biblioteca
import random

# -----

# Para saber o que tem dentro da biblioteca
dir(random)

# Para saber o que um método faz
help(random.radint)

# Para sortiar algo de dentro de uma lista
lista = ['nome1', 'nome2', 'nome3']
random.choice(lista)

# Para misturar uma lista
random.shuffle(lista)

# Para gerar algo aleatório mais de uma vez
# (lista de itens, quantidade de vezes gerada
random.sample(lista, 3)
