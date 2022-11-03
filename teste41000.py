def ultima_parada(combustivel, consumo, postos_de_gasolina):
    distancia = combustivel * consumo
    postos_de_gasolina = sorted(postos_de_gasolina)
    i = 0

    if distancia < postos_de_gasolina[0]:
        b = -1
        return b
    else:
        while ((distancia >= postos_de_gasolina[i]) and (i < len(postos_de_gasolina))):
            if i == (len(postos_de_gasolina) - 1):
                return postos_de_gasolina[i]
            i = i + 1
        return postos_de_gasolina[i - 1]






if __name__ == '__main__':
    combustivel = 2
    consumo = 8
    postos_de_gasolina = [18]
    a = ultima_parada(combustivel, consumo, postos_de_gasolina)
    print(a)