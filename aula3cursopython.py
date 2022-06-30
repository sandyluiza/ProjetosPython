#Segundo programa em Python
print('Segundo Programa')

#Primeira forma de fazer o programa
a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo número: '))
c=int(input('Digite o terceiro número: '))

if a>b and a>c: #o 'and' faz o papel do '&'
    print('O maior número é {}.'.format(a))
elif b>a and b>c:
    print('O maior número é {b}.'.format(b=b)) #outra forma de fazer o print
else:
    print('O maior número é '+str(c)+'.')

print('Fim do programa')

# #Segunda forma de fazer o programa
# a = int(input('Digite o primeiro número: '))
# b = int(input('Digite o segundo número: '))
#
# if a > b:
#     print('O maior número é '+str(a))
# else:
#     print('O maior número é '+str(b))
#
# print('Fim do programa')
