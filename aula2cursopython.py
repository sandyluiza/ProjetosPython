#Aula de Python
print('Programa em Python\n')

# #Iniciando o programa com variaveis de valores fixos
# a=1
# b=1

# Pedindo variáveis - exemplo 1
# Iniciando o programa com valores digitados, mas não sendo pedidos por uma frase
# a=input()
# b=input()
#apenas digitando dessa forma dá erro, porque o programa lê as variáveis como uma string
#colocando da maneira correta:
# a=int(input())
# b=int(input())
#dessa forma, adicionando o int, o valor já é convertido em inteiro

#Pedindo Variaveis - exemplo 2
# Iniciando o programa com valores digitados pelo usuário sendo pedido por uma frase
# a=input('Digite o primeiro valor ')
# b=input('Digite o segundo valor ')
#apenas digitando dessa forma dá erro, porque o programa lê as variáveis como uma string
#colocando da maneira correta:
a=int(input('Digite o primeiro valor '))
b=int(input('Digite o segundo valor '))

#Operações em Python
soma=a+b
subtracao=a-b
multiplicacao=a*b
divisao=a/b
resto=a%b

# #Formas de Imprimir
# #Parte 1
# print('Parte 1')
# print(soma)
# print(subtracao)
# print(multiplicacao)
# print(divisao)
# print(resto)
#
# #Parte 2
# #print(type(soma)) #esse comando mostra que tipo de variavel é
# #para imprimir junto com texto, precisa transformar a variavel em texto
# #ao escrever texto, pode usar duas aspas ou uma
# print('\nParte 2')
# print('Soma: '+str(soma)) #str mudou a soma de inteiro ou float(no caso da divisão, para string
# print('Subtração: '+str(subtracao))
# print('Multiplicação: '+str(multiplicacao))
# print('Divisao: '+str(divisao))
# print('Resto: '+str(resto))
#
# #Parte 3
# print('\nParte 3')
# print('Soma: {}'.format(soma)) #essa é outra forma de converter o numero para string
# print('Subtração: {}'.format(subtracao))
# print("Multiplicação: {}".format(multiplicacao))
# print('Divisão: {}'.format(divisao))
# print('Resto: {}'.format(resto))
#
# #Parte 4
# #essa é forma de escrever variaveis juntas num mesmo comando
# print('\nParte 4')
# print('Soma: {} \nSubtração: {} \nMultiplicação: {} \nDivisão: {} \nResto: {}'.format(soma, subtracao,
#                                                                                         multiplicacao, divisao,
#                                                                                         resto))
#
# #parte 5
# # escrever dentro pra não perder
# print('\nParte 5')
# print(f'Soma: {soma} \nSubtração: {subtracao} \nMultiplicação: {multiplicacao} \nDivisão: {divisao} \nResto: {resto}'.
#       format(soma=soma, subtracao=subtracao, multiplicacao=multiplicacao, divisao=divisao, resto=resto))
# #essa é a forma de escrever dentro pra não perder
# #não precisa estar em ordem depois do format
#
# #parte 6
# # da mesma forma da parte 5, apenas mudando a ordem depois do format e mostrando que não tem problema
# print('\nParte 6')
# print(f'Soma: {soma} \nSubtração: {subtracao} \nMultiplicação: {multiplicacao} \nDivisão: {divisao} \nResto: {resto}'.
#       format(subtracao=subtracao, soma=soma, resto=resto, divisao=divisao, multiplicacao=multiplicacao))
#
# #parte 7
# # da mesma forma da parte 7, porém mostrando que o nome dentro da chave pode ser qualquer um desde que esteja
# # referenciado depois do formato
# print('\nParte 7')
# print('Soma: {sum} \nSubtração: {sub} \nMultiplicação: {multi} \nDivisão: {div} \nResto: {rest}'.format
#       (sub=subtracao, sum=soma, rest=resto, div=divisao, multi=multiplicacao))
# # posso usar variavel à beça em cima e na hora de imprimir, só dar o nome de outra variavel e colocar que é igual depois
# # do format, tipo como é feito um ponteiro

#parte 8
#outra coisa que dá pra fazer é denominar o comando do print como uma variável e depois imprimir apenas a variável
# print('\nParte 8')
Resultado = ('Soma: {sum} \nSubtração: {sub} \nMultiplicação: {multi} \nDivisão: {div} \nResto: {rest}'.format
      (sub=subtracao, sum=soma, rest=resto, div=divisao, multi=multiplicacao))
print(Resultado)


# print(int(divisao)) #int converte o float para inteiro
# x='1'
# soma2=int(x)+1 #essa linha esta convertendo x que está como string para inteiro, pra depois somar
# print (soma2)

# seleciona várias linhas e clica em "ctrl+/" faz varias linhas ficarem comentadas


