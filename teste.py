# lista_teste=['cachorro', 'gato', 'cavalo']
# numero=int(len(lista_teste))
# lista1=[]
#
# for x in range(numero):
#     contador = len(lista_teste[x])
#     lista1.append(contador)
#
# print(lista1)

lista=[[4,7,8],[4,5,10],[4,8,9]]
# item1= lambda item:item[1]
# print(item1(lista))

lista1=sorted(lista,key=lambda item:item[2])
print(lista1)
# soma=lambda a,b:a+b
# print(soma(5,10))


