#exerciio for
n=int(input('Entre com o numero '))
saida = str(1)

for a in range(1, n):
    a += 1
    b = str(a)
    saida = saida + b
print(saida)