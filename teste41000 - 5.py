def checa_numero_escondido(numero,numero_oculto):
    cont = 0
    numero = str(numero)
    numero = list(numero)
    numero_oculto = str(numero_oculto)
    numero_oculto = list(numero_oculto)

    for x in range(len(numero_oculto)):
        for y in range(len(numero)):
            z = y+x
            if numero_oculto[x] == numero[z]:
                cont = cont + 1
                break
    tam = len(numero_oculto)
    if cont >= tam:
        return True
    elif cont < tam:
        return False


if __name__ == '__main__':
    numero = 12345
    numero_oculto = 235
    checa_numero_escondido(numero, numero_oculto)
