def retorna_menor_e_maior_valor_de_vendas(tickets):
    maior = 19
    menor = 501
    for x in tickets:
        for y in x:
            if y > maior:
                maior = y
            if ((y < menor) and (y > 0)):
                menor = y

    mai_men = [maior, menor]
    print(mai_men)


if __name__ == '__main__':
    tickets = [[200,100],[300], [0], [300]]
    retorna_menor_e_maior_valor_de_vendas(tickets)
