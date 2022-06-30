# montei a lista
lista_com_todos = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    lista = [name,score]
    lista_com_todos.append(lista)
print(lista_com_todos)

# ordenei
lista1 = sorted(lista_com_todos, key = lambda item: item[1] )
print(lista1)

# peguei apenas os segundos maiores
quantidade_elemen_list1 = int(len(lista1))
print(quantidade_elemen_list1)
elemento_seg_menor = []

y=1

for x and y in range(quantidade_elemen_list1):
    for y in range(quantidade_elemen_list1):
        if lista1[x][1] < lista1[y][1]:
            elemento_seg_menor.append(lista1[y])
print(elemento_seg_menor)

quantidade_elemen_list2 = int(len(elemento_seg_menor))
print(quantidade_elemen_list2)

# elemento_seg_ter=[]
# for x in range(quantidade_elemen_list2):
#     for y in range(quantidade_elemen_list2):
#         if elemento_seg_menor[y][1] > elemento_seg_menor[x][1]:
#             elemento_seg_ter.remove(elemento_seg_menor[y])
#         print(elemento_seg_ter)



# if elemento_seg_menor[x][1] == lista1[x+1][1]:
#     elemento_seg_menor.append(lista1[x+1])
# else:
#     elemento_seg_menor = elemento_seg_menor


# # colocar em ordem alfabetica pelo nome
# elemento_seg_menor.sort()
#
# # imprimir os nomes
# quantidade_elemen_list = int(len(elemento_seg_menor))
# if quantidade_elemen_list>1:
#     for y in range (quantidade_elemen_list):
#         print(elemento_seg_menor[y][0])
# else:
#     print(elemento_seg_menor)
