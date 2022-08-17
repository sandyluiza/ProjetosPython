from collections import Counter   # o Counter conta a quantidade de elementos dentro do dicionario

# X = numero de sapatos
# os tamanhos dos X sapatos que tem (alguns estão repetidos porque tem dois pares da numeração)
# N = numero de clientes
# os sapatos pedidos pelos N clientes organizados pela numeração e o preço
# retornar a soma dos preços dos sapatos

Quant_pares = int(input())
Taman_sapat = input().split()
Quant_client = int(input())
Sapat_pedidos = []
for _ in range(Quant_client):
    Sapat_pedido = input().split()
    Sapat_pedidos.append(Sapat_pedido)
# print(Taman_sapat)
# print(Sapat_pedidos)

Soma_valores = 0
for x in Sapat_pedidos:
    print(x)
    print(x[0])
    if x[0] in Taman_sapat:
        Soma_valores = Soma_valores + int(x[1])
        print(Soma_valores)
        Taman_sapat.remove(x[0])
        print(Taman_sapat)
print(Soma_valores)
