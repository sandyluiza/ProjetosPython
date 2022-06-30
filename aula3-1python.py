#Aula 3 programa 2 - par e impar

#Se o número é par
# a=int(input('Digite o número '))
#
# resto=a%2
#
# if resto==0:
#     print('O número {} é par'.format(a))
# else:
#     print('O número {} é ímpar'.format(a))

# #Se um dos números é par usando or
# a=int(input('Digite o primeiro número '))
# b=int(input('Digite o segundo número '))
#
# resto_a=a%2
# resto_b=b%2
#
# if resto_a==0 or resto_b==0:
#     print('Foi digitado ao menos um número par')
# else:
#     print('Nenhum número digitado é par')

#Fazendo um argumento com or not
a=int(input('Digite o primeiro número '))
b=int(input('Digite o segundo número '))

resto_a=a%2
resto_b=b%2

if resto_a==0 or not resto_b==0:  #quando se usa o or not, o segundo argumento fica o contrário, se é verdadeiro fica falso
    print('Foi digitado ao menos um número par')
else:
    print('Nenhum número digitado é par')
