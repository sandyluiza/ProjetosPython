class Error(Exception):
    pass
class InputError(Error):
    def __init__(self,message):
        self.message=message

def tentando_fazer_def():
    while True:
        try:
            x=int(input('Entre com uma nota de 0 a 10: '))
            print(x)
            if x>10 or x<0:
                raise InputError ('Nota não pode estar fora do intervalo 0 a 10')
            break
        except ValueError:
            print('Valor inválido. Deve-se digitar apenas números')
        except InputError as ex:
            print(ex)

if __name__ == '__main__':
    tentando_fazer_def()