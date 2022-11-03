def menor_string_maior(name):
    cont = 0
    name1 = list(name)
    name3 = []
    tam = len(name1) - 1
    for x in range(tam):
        if name1[tam - x] > name1[tam - x - 1]:
            aux = name1[tam - x]
            name1[tam - x] = name1[tam - x - 1]
            name1[tam - 1 - x] = aux
            cont = cont + 1
            name2 = ''.join(name1)
            if (name2 > name):
                name3.append(name2)
    name3 = sorted(name3)

    if cont == 0:
        result = 'sem resposta'
    else:
        result = name3[0]

    while (result > name) and (result <= name3[0]):
        result1 = list(result)
        for x in range(tam):
            if result1[tam - x] > result1[tam - x - 1]:
                aux = result1[tam - x]
                result1[tam - x] = result1[tam - x - 1]
                result1[tam - 1 - x] = aux
                cont = cont + 1
                result = ''.join(result1)

    print(name3)
    return result


if __name__ == '__main__':
    name = 'Qualified'
    menor_string_maior(name)
