#Aula 4 - Python - Extruturas de repetição

# #Essa extrutura imprime os números começando no zero até o <100, ou seja, 99
# for x in range(100):
#     print(x)

# for x in range(10, 20): #Essa extrutura imprime o x no intervalo >=10 a <20
#     print(x)

#Determinar se um número é primo
a=int(input('Digite o número '))
div=0
for x in range (1, a+1):
    resto = a%x
    # print(x, resto) #outra forma de usar o print
    if resto == 0:
        # div=div+1 #pode usar também div+=1 que é como o div++ do C
        div+=1
if div==2:
    print('O número {} é primo.'.format(a))
else:
    print('O número {} não é primo.'.format(a))