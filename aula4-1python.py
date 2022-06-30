#Números primos de 0 a 100
# a=0
# for a in range (0, 100):
#     a=a+1
#     div=0
#     for x in range (1, a):
#         resto = a%x
#         # print(x, resto) #outra forma de usar o print
#         if resto == 0:
#             # div=div+1 #pode usar também div+=1 que é como o div++ do C
#             div+=1
#     if div==2:
#         print('O número {} é primo.'.format(a))
#     else:
#         print('O número {} não é primo.'.format(a))

# #Para imprimir apenas os números primos
# print('Os números primos entre 1 e 100 são: ')
# for a in range (0, 100):
#     div=0
#     for x in range (1, a+1):
#         resto = a%x
#         # print(x, resto) #outra forma de usar o print
#         if resto == 0:
#             # div=div+1 #pode usar também div+=1 que é como o div++ do C
#             div+=1
#     if div==2:
#         print(a)

#Para imprimir os numeros primos até o número informado pelo usuário
a=int(input('Informe o número '))
print('Os números primos de 1 até {} são:'.format(a))
for a in range (0, a+1):
    div=0
    for x in range (1, a+1):
        resto = a%x
        # print(x, resto) #outra forma de usar o print
        if resto == 0:
            # div=div+1 #pode usar também div+=1 que é como o div++ do C
            div+=1
    if div==2:
        print(a)
