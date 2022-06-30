#como trabalhar com lambda
# contador_letras=lambda lista: [len(x) for x in lista]
#
# lista_animais = ['cachorro','gato','papagaio']
# print(contador_letras(lista_animais))
#
# # o lambda torna as funções anônimas e com isso o código fica mais elegante pois só tem uma linha,não precisa ficar
#dando enter
#
# soma=lambda a,b:a+b
# print(soma(5,10))
#
# subtracao=lambda a,b:b-a
# print(subtracao(5,10))

calculadora={
    'soma': lambda a,b:a+b,
    'subtracao': lambda a,b:a-b,
    'divisao': lambda a,b:a/b,
    'multiplicacao': lambda a,b:a*b,
}

soma=calculadora['soma']
subtracao=calculadora['subtracao']
divisao=calculadora['divisao']
multiplicacao=calculadora['multiplicacao']
print(soma(10,2))
print(subtracao(10,2))
print(divisao(10,2))
print(multiplicacao(10,2))