import math
def calcula_porcentagem_sorteio(assinante,minutos_assistidos):
    chance_cada = []
    chance_cada_1 = []
    minutos_assistidos_1 = []
    for z in minutos_assistidos:
        z = z/60
        z = math.ceil(z)
        minutos_assistidos_1.append(z)

    for i in range(len(assinante)):
        if assinante[i] == True:
            chance_cada.append(minutos_assistidos_1[i]*2)
        else:
            chance_cada.append(minutos_assistidos_1[i])
    for i in chance_cada:
        soma = sum(chance_cada)
        x = i/soma*100
        chance_cada_1.append(round(x))

    print(chance_cada_1)
    return chance_cada_1


if __name__ == '__main__':
    assinante = [True, False]
    minutos_assistidos = [60, 120]
    calcula_porcentagem_sorteio(assinante, minutos_assistidos)
