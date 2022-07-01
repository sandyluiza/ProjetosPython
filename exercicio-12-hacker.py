# como inserir item a uma string
# def mutate_string(string, position, character):
#     string = list(string)
#     # print(string)
#     # print(type(position))
#     # print(type(character))
#     string.insert(position, character)
#     # print(string)
#     resultado = ''.join(string)
#     # print(resultado)
#     return resultado
#
# if __name__ == '__main__':
#     s = input()
#     # print(type(s))
#     i, c = input().split()   #como dividir a entrada em variáveis quando são recebidas na mesma linha
#     # print(i)
#     # print(c)
#     # print(i,c)    #como imprimir variaveis juntas
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

# como substituir item de uma string
def mutate_string(string, position, character):
    string = list(string)
    # print(string)
    # print(type(position))
    # print(type(character))
    string[position] = character
    # print(string)
    resultado = ''.join(string)
    # print(resultado)
    return resultado

if __name__ == '__main__':
    s = input()
    # print(type(s))
    i, c = input().split()   #como dividir a entrada em variáveis quando são recebidas na mesma linha
    # print(i)
    # print(c)
    # print(i,c)    #como imprimir variaveis juntas
    s_new = mutate_string(s, int(i), c)
    print(s_new)