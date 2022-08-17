# usando ferramento itertools.permutations(iterable[, r])
from itertools import permutations
# lista = ['1', '2', '3']
# print(list(permutations(lista)))
# print(list(permutations(['1', '2', '3'])))
# print(list(permutations(['1', '2', '3'], 2)))
# print(list(permutations('abc', 3)))

def String_e_caractere(s, n):
    lista_item_junto = []
    permutacao = list(permutations(s,int(n)))
    # permutacao = permutacao.sort()
    # print(permutacao)
    for x in permutacao:
    #     # print(type(x))
    #     # print(x)
        item_junto = ''.join(x)
        lista_item_junto.append(item_junto)
    lista_item_junto.sort()
    # print(lista_item_junto)
    for y in lista_item_junto:
        print(y)
    # print(s)
    # print(n)



if __name__ == '__main__':
    String, numero_caract = input().split()
    String_e_caractere(String, numero_caract)