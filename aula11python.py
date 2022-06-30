#trabalhando com exceções
#o try permite que o sistema rode um erro, ao invés de dar erro e com isso ele seja tratado, como o caso abaixo
#Primeiro erro
try:
    divisao = 10/0
except ZeroDivisionError:   #esse zerodivisionerror é específico da divisão de um número por zero
    print('Não é possível realizar uma divisão por 0.')

#Segundo erro
lista = [1,10]
arquivo = open ('teste.txt', 'r')
try:
    texto = arquivo.read()
    numero=lista[3]
    print('Fechando arquivo')
    arquivo.close()
# except:     #colocando apenas o except, qualquer erro que tiver, ele vai tratar dessa forma.
#     print('Erro desconhecido')
except IndexError:    #especifico de lista quando o numero é superior
    print('Erro ao acessar um índice inválido da lista')

#Terceiro erro
try:
    x=1
except BaseException as ex:
    print('erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre mais exceção')

#tudo que está no finally, dando erro ou não vai ser executado
finally:
    print('Sempre executa')
    arquivo.close()