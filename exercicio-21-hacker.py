
# 1 palavra
# duas pessoas fazendo substrings a partir da palavra
# Stuart - palavras começando com consoante
# Kevin - começando com vogais
# Um jogador ganha +1pontos para cada ocorrência da substring na string.
# Determinar o vencedor do jogo e a pontuação
# sempre do inicio para o fim da palavra, não pode formar palavra do fim para o inicio
def minion_game(string):
    todas_as_strings_possiveis = []
    f = len(string)
    for x in range(f+1):
        d = string[x:]  # OK
        for y in range(f+1):
            e = d[:f-y]   #  ok
            todas_as_strings_possiveis.append(e)
        # g = string[x:f-x]
        # h = string[f-x:x+1]
        # for y in range(f+1):
        #     h = string[x:f-y]
        #     i = string[y:x+1]
        # g = string[x:f-x]
        # print(g)
          #OK
        todas_as_strings_possiveis.append(d)  #ok
        # todas_as_strings_possiveis.append(g)
        # todas_as_strings_possiveis.append(h)
        # todas_as_strings_possiveis.append(i)
    # print(todas_as_strings_possiveis)

    todas_as_strings_possiveis = set(todas_as_strings_possiveis)
    todas_as_strings_possiveis = list(todas_as_strings_possiveis)
    # i_seg_strin = len(todas_as_strings_possiveis)
    # print(todas_as_strings_possiveis)

    # for

    # a = len(string)
    # contagem_palavras = 0
    # x = 0
    lista_palavras_conso = []
    lista_palabras_vogais = []
    for y in todas_as_strings_possiveis:
        if y == '':
            pass
        elif y.startswith('A' or 'E' or 'I' or 'O' or 'U'):
            # pontos do Kevin - contar e imprimir
            # print(string)
            lista_palabras_vogais.append(y)
        else:
            # string = string[1:]
            # c = string.startswith('A' or 'E' or 'I' or 'O' or 'U')
            # while c == True:
            #     x = x+1
            #     string = string[x:]
            #     if string == '':
            #         break
            # print(string)
            lista_palavras_conso.append(y)
            # pontos do Stuart - contar e imprimir
    # print('kevin')
    # print(lista_palabras_vogais)
    # print('stuart')
    # print(lista_palavras_conso)

    # Quantidade Kevin
    cont_k = 0
    i = 0
    for sub_string in lista_palabras_vogais:
        quant_carac = len(string)
        for i in range(quant_carac):
            if string[i:].startswith(sub_string):
                cont_k = cont_k + 1
    # print('kevin')
    # print(cont_k)

    # Quantidade Stuart
    cont_s = 0
    i = 0
    for sub_string in lista_palavras_conso:
        quant_carac = len(string)
        for i in range(quant_carac):
            if string[i:].startswith(sub_string):
                cont_s = cont_s + 1
    # print('stuart')
    # print(cont_s)

    if cont_k > cont_s:
        print('Kevin {}'.format(cont_k))
    elif cont_s > cont_k:
        print('Stuart {}'.format(cont_s))
    else:
        print('Draw')

    # for _ in range(a):
        #     # determinar se começa com consoante ou vogal
        #
        #
        #     palavras =
        #     contagem_palavras = contagem_palavras+1
        #     print(palavras)
        #     print(contagem_palavras)

if __name__ == '__main__':
    s = input()
    minion_game(s)