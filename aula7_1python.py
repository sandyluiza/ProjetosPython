class Calculadora:
    # def __init__(self):
    #     pass #é para não ficar vazio, na prática ele não faz nada
    # #ou pode retirar o init pois os valores foram adicionados em cada equação
    def soma(self, a, b):
        return a+b
    def subtracao(self, a, b):
        return a-b
    def multiplicacao(self, a, b):
        return a*b
    def divisao(self, a, b):
        return a/b

if __name__ == '__main__': #o if name main serve pra que quando for importar esse método em outro programa, não puxe
    #tudo, com o if name main, puxa apenas o que você quer.
    #se deixar sem o if name main, independente do que você quiser puxar no outro programa, vai puxar tudo que tem nesse
    calculadora=Calculadora() #essa parte se chama estanciar
    print(calculadora.soma(5,2))
    print(calculadora.subtracao(3,1))
    print(calculadora.multiplicacao(100,3))
    print(calculadora.divisao(20,4))