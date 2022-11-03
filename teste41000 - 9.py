def shuffle_musicas(musicas_tocadas):
    lista_music_1 = []

    while len(musicas_tocadas) > 0:
        maior_o = 0
        menor_o = 9999999
        if len(musicas_tocadas) == 1:
            lista_music_1.append(musicas_tocadas[0])
            return lista_music_1
        for x in range(len(musicas_tocadas)):
            if musicas_tocadas[x] > maior_o:
                maior_o = musicas_tocadas[x]
            if musicas_tocadas[x] < menor_o:
                menor_o = musicas_tocadas[x]
        musicas_tocadas.remove(maior_o)
        musicas_tocadas.remove(menor_o)
        lista_music_1.append(maior_o)
        lista_music_1.append(menor_o)

    print(lista_music_1)
    return lista_music_1


if __name__ == '__main__':
    musicas_tocadas = [2, 10, 5, 3]
    shuffle_musicas(musicas_tocadas)
