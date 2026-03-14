qtd = 0
for i in range(18644, 33088):
    if ('2' in str(i) and not('7' in str(i))):
       qtd += 1

print(qtd)