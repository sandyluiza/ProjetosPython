#Aula 3 - notas
#Primeira forma de fazer - piozinha para o usuário
# a=float(input('Digite a primeira nota '))
# b=float(input('Digite a segunda nota '))
# c=float(input('Digite a terceira nota '))
# d=float(input('Digite a quarta nota '))
#
# if a>=0 and a<=10 and b>=0 and b<=10 and c>=0 and c<=10 and d>=0 and d<=10:
#     media=(a+b+c+d)/4
#     print('A média é {}.'.format(media))
# else:
#     print('Foi informada alguma nota errada.')

#Segunda forma de fazer - melhor para o usuário
a=float(input('Digite a primeira nota '))
if a<0 or a>10:
    a=float(input('A nota informada está errada. Digite a primeira nota '))
b=float(input('Digite a segunda nota '))
if b<0 or b>10:
    b=float(input('A nota informada está errada. Digite a segunda nota '))
c=float(input('Digite a terceira nota '))
if c<0 or c>10:
    c=float(input('A nota informada está errada. Digite a terceira nota '))
d=float(input('Digite a quarta nota '))
if d<0 or d>10:
    d=float(input('A nota informada está errada. Digite a quarta nota '))

media=(a+b+c+d)/4
print('A média é {}.'.format(media))

#Esse algoritmo possui um erro, pois se o usuário digitar duas vezes seguidas a nota errada, ele aceitará a segunda nota
#o algoritmo que elimina esse erro está no arquivo "aula4-2python"