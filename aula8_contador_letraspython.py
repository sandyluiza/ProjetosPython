#criação de método que conta letras
def contador_letras(lista):
    contador=[]
    for x in lista:
        quantidade=len(x) #o len determina a quantidade de itens dentro da lista
        contador.append(quantidade)
    return contador

def teste():
    return ('teste')

if __name__ == '__main__':
    lista=['cachorro', 'gato']
    print(contador_letras(lista))


