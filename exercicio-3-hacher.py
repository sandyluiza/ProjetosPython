x = int(input())
y = int(input())
z = int(input())
n = int(input())

a=0
b=0
c=0
lista1 = []

for a in range(0, x+1):
    lista = [a, b, c]
    for b in range(0, y+1):
        lista = [a, b, c]
        for c in range(0, z+1):
            lista = [a, b, c]
            soma=sum(lista)
            if soma != n:
                lista1.append(lista)
print(lista1)