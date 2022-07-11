import string
letras = list(string.ascii_lowercase)
letra = []
tracinho = '-'
juntos = []
com_tracinho = []

def print_rangoli(size):
    # tamanho_da_linha = (size*2)-1 + (size*2)-2
    a = ''
    for x in range(1, size+1):
        h = size-x
        # g = x-2
        # v = len(letra)
        # print(v)
        # if v == 0:
        a = a+tracinho+letras[h]
        # print(a)
        # b = len(a)
        # c = int((tamanho_da_linha-b)/2)
        # d = (tracinho*(c-1))+a+c*tracinho
        # d = a+c*tracinho
        # d = a+tracinho
        letra.append(a)
        # else:
        #     print(letra[g])
        #     a = a + tracinho + letras[h]
            # letra.append(a)
    # print(letra)
    for x in range(2, size+2):
        h = size-x
        # print(h)
        u = letra[h]
        # print(u)
        if h < 0:
            u = ''
        u = u.split('-')
        u.reverse()
        u = '-'.join(u)
        u = tracinho+u
        # print(u)
        w = letra[size-x+1]
        z = w+u
        juntos.append(z)
    # print(juntos)
    a = juntos[0]
    # print(a)
    a = a[1:]
    # print(a)
    t = len(a) - 1
    a = a[:t]
    # print(a)
    juntos[0] = a
    # print(juntos)
    r = len(juntos[0])
    s = len(juntos)
    for m in range(s):
        i = len(juntos[m])
        j = int((r-i)/2)
        e = juntos[m]
        l = (tracinho*j)+e+(tracinho*j)
        com_tracinho.append(l)
    # print(com_tracinho)
    for q in range(1, size):
        decrecente = size - q
        print(com_tracinho[decrecente])
    for o in range(size):
        print(com_tracinho[o])

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)