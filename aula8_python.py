#importando método/função de outro arquivo
# from aula7_televisaopython import Televisao
# televisao=Televisao()
# print(televisao.ligada)
# televisao.power()
# print(televisao.ligada)
#
# from aula7_1python import Calculadora
# calculadora=Calculadora()
# print(calculadora.soma(5,10))

#outra forma de fazer é deixar os froms dentro do if name main e os comandos fora:
from aula7_televisaopython import Televisao
from aula7_1python import Calculadora
from aula8_contador_letraspython import contador_letras, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora()
    print(calculadora.soma(5, 10))

    lista = ['gato', 'cachorro','papagaio']
    total_letras = contador_letras(lista)
    print(total_letras)

    teste=teste()
    print(teste)

#1 eu crio o def ou a classe dentro de 1 arquivo
#2 importo o arquivo e método
#3 eu estancio
#4 eu executo

#fazer sempre os módulos separados e ter um arquivo só que junta todos eles