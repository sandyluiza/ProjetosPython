# def insert (i,e):
#     lista.insert(i, e)
# def print ():
#     print(lista)
# def remove (e):
#     lista.remove(e)
# def append (e):
#     lista.append(e)
# def sort ():
#     lista.sort()
# def pop():
#     lista.pop()
# def reverse():
#     lista.reverse()
#
def ultimo():
    lista = []
    N = int(input())
    print(N)
    for _ in range(N):
# input('{} {} {}'.format(str(metodo),int(x),int(y)))
        a = input()
        print(a)
        b = a.split(' ')
        print(b)
        # c = '{}()'.format(b[0])
        # print(c)
        # return(c)
        if b[0] == 'insert':
            f=int(b[1])
            g=int(b[2])
            print (b[1])
            print (b[2])
            lista.insert(f, g)
        elif b[0] == 'print':
            print(lista)
        elif b[0] == 'remove':
            lista.remove(int(b[1]))
        elif b[0] == 'append':
            lista.append(int(b[1]))
        elif b[0] == 'sort':
            lista.sort()
        elif b[0] == 'pop':
            lista.pop()
        elif b[0] == 'reverse':
            lista.reverse()


# metodo = str(a)
# x=int(b)
# y=int(c)
# metodo(x,y)

if __name__ == '__main__':
    d = ultimo()
    # print (d)
