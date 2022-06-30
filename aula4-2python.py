# #Usando a extrutura de repetição while
# a=0
# while a<10:
#     print(a)
#     a+=1

#Forma correta de fazer esse algoritmo
a=float(input('Digite a primeira nota '))
while a<0 or a>10:
    a=float(input('A nota informada está errada. Digite a primeira nota '))
b=float(input('Digite a segunda nota '))
while b<0 or b>10:
    b=float(input('A nota informada está errada. Digite a segunda nota '))
c=float(input('Digite a terceira nota '))
while c<0 or c>10:
    c=float(input('A nota informada está errada. Digite a terceira nota '))
d=float(input('Digite a quarta nota '))
while d<0 or d>10:
    d=float(input('A nota informada está errada. Digite a quarta nota '))

media=(a+b+c+d)/4
print('A média é {}'.format(media))
