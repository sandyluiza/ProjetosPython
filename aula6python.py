# Aprendendo Dicionário
# o conjunto usa a chave
# conjunto = {1,2,5,3}
# print(type(conjunto))

# #ele não imprime duplicidade. Então:
# conjunto = {1,2,5,3,2,1,4,5}
# print(conjunto)
#
# #adicionando elemento
# conjunto.add(6)
# print(conjunto)
#
# print(sum(conjunto))
#
# print(max(conjunto))
#
# print(min(conjunto))
#
# #para remover usa o discard e não o remove
# conjunto.discard(2)
# print(conjunto)

# #para unir dois conjuntos não consegue pela soma, precisa usar o union
# conjunto_1={5,6,7,8,9}
# conjunto_soma=conjunto.union(conjunto_1)
# print(conjunto_soma)

# #para fazer a interseção entre 2 conjuntos
# conjunto_intersecao=conjunto.intersection(conjunto_1)
# print(conjunto_intersecao)

#para imprimir os elementos que tem em um conjunto e não tem no outro
# #vai imprimir os elementos que existem no conjunto e não tem no conjunto1
# conjunto_diferenca=conjunto.difference(conjunto_1)
# print(conjunto_diferenca)
#
# conjunto_diferenca1=conjunto_1.difference(conjunto)
# print(conjunto_diferenca1)

# # para determinar a diferença simétrica, ou seja, o que tem de diferença dos dois conjuntos juntos
# diferenca_simetrica=conjunto.symmetric_difference(conjunto_1)
# print(diferenca_simetrica)

# #para determinar se um conjunto é subconjunto de outro
# #retorna v ou f
# conjunto_2={1,2,3}
# subconjunto_ou_nao=conjunto_2.issubset(conjunto)
# print(subconjunto_ou_nao)
#
# #para fazer o contrário do caso anterior, ou seja, determinar se um conjunto é superconjunto de outro
# superconjunto_ou_nao=conjunto.issuperset(conjunto_2)
# print(superconjunto_ou_nao)

# #converter conjunto para lista
# lista=list(conjunto)
# print(lista)
#
# #converter lista para tupla
# tupla=tuple(lista)
# print(tupla)
#
# #converter tupla para conjunto
# conjunto_1=set(tupla)
# print(conjunto_1)

#tirar a duplicidade de uma lista
lista=[1,2,3,4,1,2,3,2,2,3]
print(lista)
conjunto=set(lista)
print(conjunto)
lista=list(conjunto)
print(lista)


