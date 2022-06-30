# por convenção, método é o que não retorna valor e função é o que retona valor
#no python, método se chama definição
#o return não imprime valor
# a determinação dos valores tem que ocorrer fora do def

#essa é uma forma de fazer função e método
# def soma(a,b):
#     return a+b
# def subtracao(a,b):
#     return a-b
# def multiplicacao(a,b):
#     return a*b
# def divisao(a,b):
#     return a/b
# a=10
# b=2
# print(soma(a,b))
# print(soma(3,4))
# print(subtracao(a,b))
# print(subtracao(3,4))
# print(abs(subtracao(a,b)))
# print(abs(subtracao(3,4)))
# print(multiplicacao(a,b))
# print(divisao(a,b))

#segunda forma de fazer as funções e método em áreas diferentes
class Calculadora:
    def __init__(self,num1,num2):
        self.a=num1
        self.b=num2
    def soma(self):
        return self.a+self.b
    def subtracao(self):
        return self.a-self.b
    def multiplicacao(self):
        return self.a*self.b
    def divisao(self):
        return self.a/self.b

calculadora=Calculadora(10,2) #essa parte se chama estanciar
print(calculadora.a)
print(calculadora.b)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())