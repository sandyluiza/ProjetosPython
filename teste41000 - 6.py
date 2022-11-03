def calcula_total_leds(altura,largura):
    altura = altura + 1
    largura = largura + 1
    quantidade = altura * largura
    print(quantidade)
    return quantidade

if __name__ == '__main__':
    altura = 2
    largura = 3
    calcula_total_leds(altura,largura)
