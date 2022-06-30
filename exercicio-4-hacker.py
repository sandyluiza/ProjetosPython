if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lista_de_array = list(arr)

    #eliminando duplicidades
    lista_de_array = set(lista_de_array)
    lista_de_array = list(lista_de_array)

    #eliminando o numero maior pra deixar o segundo maior
    lista_de_array.remove(max(lista_de_array))

    #imprimindo o segundo maior
    print(max(lista_de_array))