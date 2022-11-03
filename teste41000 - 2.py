def calcula_numero_da_senha(senha):
    result = []
    result_1 = []
    for y in range(len(senha)):
        cont_0 = 0
        cont_1 = 0
        for x in senha:
            if x[y] == '0':
                cont_0 = cont_0 + 1
            elif x[y] == '1':
                cont_1 = cont_1 + 1
        if cont_0 > cont_1:
            result.append(0)
        elif cont_0 <= cont_1:
            result.append(1)
    for i in result:
        i = str(i)
        result_1.append(i)
    result_1 = ''.join(result_1)
    result_2 = int(result_1, 2)
    print(result_2)


if __name__ == '__main__':
    senha = ["0110100000","1001011111","1110001010","0111010101","0011100110","1010011001","1101100100","1011010100","1001100111","1000011000"]
    calcula_numero_da_senha(senha)
