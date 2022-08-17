# Produto de plano cartesiano
from itertools import product  # para usar o product e multiplicar planos cartesianos
import sys  # para puxar o sys.stdout.write e imprimir lado a lado

A, B = input().split(), input().split()

for x in range(len(A)):
    A[x] = int(A[x])

for x in range(len(B)):
    B[x] = int(B[x])

produto = list(product(A,B))
for x in produto:
    x = str(x)+' '
    sys.stdout.write(x)  # imprime lado a lado
