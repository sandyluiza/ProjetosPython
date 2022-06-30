#formei a lista com os dados
lista_com_todos = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    lista= [name,score]
    lista_com_todos.append(lista)
print(lista_com_todos)

lista1=sorted(lista_com_todos,key=lambda item:item[1]) #utilizamos a função lambda para indicar ao python que queremos
# ordenar pelo segundo item, que será o valor (item[1])
#sempre que precisar ordenar pelo segundo item de uma lista dentro de uma lista, montar exatamente como o modelo acima
print(lista1)

quantidade_elemen_list1=int(len(lista1))

if quantidade_elemen_list1>1:
    if lista1[0][1]==lista1[1][1]==lista1[2][1]:
        lista1.remove(lista1[0])
        lista1.remove(lista1[0])
        lista1.remove(lista1[0])
        quantidade_elemen_list1 = int(len(lista1))

    if quantidade_elemen_list1 > 1:
        if lista1[0][1] == lista1[1][1]:
            lista1.remove(lista1[0])
            lista1.remove(lista1[0])
        else:
            lista1.remove(lista1[0])
else:
    lista1.remove(lista1[0])
print(lista1)

quantidade_elemen_list=int(len(lista1))
print(quantidade_elemen_list)

resposta_em_ordem_alfab=[]

if quantidade_elemen_list>1:
    if lista1[0][1]==lista1[1][1]:
        resposta_em_ordem_alfab.append(lista1[0][0])
        resposta_em_ordem_alfab.append(lista1[1][0])
    else:
        resposta_em_ordem_alfab.append(lista1[0][0])
else:
    resposta_em_ordem_alfab.append(lista1[0][0])

resposta_em_ordem_alfab.sort()

numero_elementos_resposta=int(len(resposta_em_ordem_alfab))

if numero_elementos_resposta>1:
    print(resposta_em_ordem_alfab[0])
    print(resposta_em_ordem_alfab[1])
else:
    print(resposta_em_ordem_alfab[0])


#
# lista1=[['Rachel', -50.0], ['Mawer', -50.0], ['Sheen', -50.0], ['Shaheen', 51.0]]
# for x in range (3):
#     if lista1[x][1]==lista1[x+1][1]:
#         print (lista1[x+1])