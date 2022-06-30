#separar uma string em uma lista e juntar uma lista em string
def split_and_join(line):
    resultado = line.split(' ') #essa parte é para separa a string em uma lista
    # print (resultado)
    resultado = '-'.join(resultado)  #essa parte é para juntar a lista em uma string separada por '-'
    # print(resultado)
    return resultado

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)