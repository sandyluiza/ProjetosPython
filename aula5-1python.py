#Aula sobre tupla
#a diferença entre lista e tupla é que a lista pode ser mutável e a tupla não pode ser mudada
#na prática, basta escrever os itens em parênteses ao invés de colchetes
primeira_tupla=(1,3,4,7)
print(primeira_tupla)
# print(primeira_tupla[3])

# primeira_tupla[0]=11 #não adiciona o valor porque a tupla não é editável, se fixou o valor não dá para adicionar

# # quando se deseja saber a quantidade de elementos em uma tupla ou lista
# print(len(primeira_tupla))

# #converte lista para tupla
# lista_animal=['cachorro', 'gato', 'coelho', 'papagaio', 'arara']
# print(lista_animal)
# tupla_animal=tuple(lista_animal)
# print(type(tupla_animal))
# print(tupla_animal)

#converte tupla em lista
tupla_em_lista=list(primeira_tupla)
print(tupla_em_lista)
print(type(tupla_em_lista))
#com a tupla se tornando lista, é possível alterar valores
tupla_em_lista[1]=27
print(tupla_em_lista)