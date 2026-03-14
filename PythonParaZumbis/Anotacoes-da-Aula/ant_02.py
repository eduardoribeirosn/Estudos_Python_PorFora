# Para importar métodos específicos
from random import randint, sample

# ARQUIVOS
# Para abrir um arquivo - Exemplo
f = open(r'c:/Users/fmsa/x.txt', 'w') # Esse r no começo da string é para deixá-la crua. deixar a / sem efeito.

# Para escrever algo - a variável tem que estar como 'w'
f.write(f'txt')
f.close()

# Para ler algo
f2 = open(r'c:/Users/fmsa/x.txt')
for linha in f2.readlines():
    print (linha.strip()) # strip para tirar os \n
f2.close()

# Caso coloque um nome/caminho que não exista, irá dar erro 2

# Mesma coisa que o anterior só que em uma linha
with open(r'c:/Users/fmasa/x.txt') as f3:
    print(f.read())

# Com "with" não precisa dar .close

# string.punctuation pega todos os caracteres especiais.    