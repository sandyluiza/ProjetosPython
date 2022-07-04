def count_substring(string, sub_string):
    cont = 0
    i = 0
    quant_carac = len(string)
    for i in range(quant_carac):
        if string[i:].startswith(sub_string):   #startswith () é utilizado para verificar se a string é especificado
        # sub-string no início, se ele retorna True, caso contrário, False.
            cont = cont + 1
    #     a = string.count(sub_string)    #conta se tem substring dentro de uma string
    return cont


if __name__ == '__main__':
    string = input().strip()   # o .strip() é para separa o que foi digitado na primeira linha, da segunda
    sub_string = input().strip()
    # print(string)
    # print(sub_string)

    count = count_substring(string, sub_string)
    print(count)