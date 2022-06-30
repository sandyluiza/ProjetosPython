#isso é um método porque não retorna nada
class Televisao:
    def __init__(self):
        self.ligada=False
        self.canal=5
    def power(self):
        if self.ligada:
            self.ligada=False
        else:
            self.ligada=True
    def aumenta_canal(self):
        if self.ligada:
            self.canal +=1
    def diminui_canal(self):
        if self.ligada:
            self.canal -=1

if __name__ == '__main__': #esse comando quer dizer "só execute o que está dentro do main se o arquivo for executado por
    #ele mesmo. Caso seja importado o arquivo aula7_televisaopython, não execute essa parte
    #para importar basta abrir o console, digitar import "nome do arquivo"
    #exemplo import aula7_televisaopython
    televisao=Televisao()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    print('Canal: {}'.format(televisao.canal))
    televisao.power()
    televisao.aumenta_canal() #colocar duas vezes quer dizer aumentar duas vezes (dois canais), por isso que a resposta dá 7
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))

    #outra forma de fazer é usar:
    #dessa forma, você puxa apenas o método que precisa dentro do projeto
    # from aula7_televisaopython import Televisao
    #televisao.Televisao()
    #televisao.ligada
    #televisao.power()
    #televisao.ligada
