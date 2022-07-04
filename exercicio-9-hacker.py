#alterando uma string de letras maiusculas para minusculas e vice versa
def swap_case(s):
    # b = ''
    # # quant_carac = len(s)
    # for x in s:
    #     maiusculo = x.isupper() #falar se tem letra maiuscula
    #     minusculo = x.islower() #falar se tem letra minuscula
    #     if maiusculo == True:
    #         x = x.lower() #converter para minuscula
    #         # print('maiusculo')
    #         # print(x)
    #     elif minusculo == True:
    #         x = x.upper() #converter para maiuscula
    #         # print(x)
    #         # print('minusculo')
    #     b = b+x
    b = s.swapcase()
    return (b)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)