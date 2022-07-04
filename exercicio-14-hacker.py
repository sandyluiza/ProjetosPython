# vendo caracteristicas de uma string
# if __name__ == '__main__':
#     s = input()

    # # se tem qualquer caractere alfanumerico
    # p = 0
    # for q in s:
    #     if q.isalnum() == True:
    #         p = p + 1
    # if p == 0:
    #     print(False)
    # else:
    #     print(True)
    # # print(s.isalnum())
    #
    # # se tem qualquer caractere alfabetico
    # g = 0
    # for x in s:
    #     if x.isalpha() == True:
    #         g = g+1
    # if g == 0:
    #     print(False)
    # else:
    #     print(True)
    #
    # # se tem qualquer dígito (0-9)
    # w = 0
    # for d in s:
    #     if d.isdigit() == True:
    #         w = w + 1
    # if w > 0:
    #     print(True)
    # else:
    #     print(False)
    #
    # # qualquer caractere minusculo
    # h = 0
    # for y in s:
    #     if y.islower() == True:
    #         h = h+1
    # if h == 0:
    #     print(False)
    # else:
    #     print(True)
    #
    # #qualquer caractere maiusculo
    # n = 0
    # for z in s:
    #     if z.isupper() == True:
    #         n = n + 1
    # if n == 0:
    #     print(False)
    # else:
    #     print(True)
    # # print(s)

# fazendo o código de maneira mais organizada
if __name__ == '__main__':
    s = input()
    p = 0
    g = 0
    w = 0
    h = 0
    n = 0

    for x in s:
        if x.isalnum() == True:
            p = p + 1
        if x.isalpha() == True:
            g = g+1
        if x.isdigit() == True:
            w = w + 1
        if x.islower() == True:
            h = h+1
        if x.isupper() == True:
            n = n + 1

    if p == 0:
        print(False)
    else:
        print(True)

    if g == 0:
        print(False)
    else:
        print(True)

    if w > 0:
        print(True)
    else:
        print(False)

    if h == 0:
        print(False)
    else:
        print(True)

    if n == 0:
        print(False)
    else:
        print(True)