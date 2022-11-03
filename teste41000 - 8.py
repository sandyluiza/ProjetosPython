def menor_string_maior(name):
    cont = 0
    name1 = list(name)
    tam = len(name1) - 1
    name3 = []
    result = ''
    for x in range(tam):
        for j in range(tam):
            if name1[tam - x] > name1[tam - j - 1]:
                aux = name1[tam - x]
                name1[tam - x] = name1[tam - j - 1]
                name1[tam - 1 - j] = aux
                cont = cont + 1
                name2 = ''.join(name1)

                name3.append(name2)
    name3 = sorted(name3)
    print(name3)
    if cont == 0:
        result = 'sem resposta'
    else:
        result = name3[0]

    return result


if __name__ == '__main__':
    name = 'Qualiifed'
    menor_string_maior(name)
