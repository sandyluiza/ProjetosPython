#para criar o arquivo e escrever.
def escrever_texto(texto):
    arquivo=open ('teste.txt', 'w') #essa parte quer dizer que ele vai criar ou abrir o documento "teste.txt" e
    #adicionar o texto que eu escrever entre parênteses no outro arquivo
    #caso deseje criar ou abrir um arquivo em outro endereço, basta escrever o endereço conforme abaixo:
    # arquivo = open('C:/Users/Sandy/Documents/ADS/Projetos em Python/teste.txt', 'w')
    #outra forma de escrever essa parte de cima é:
    # endereco='C:/Users/Sandy/Documents/ADS/Projetos em Python/teste.txt'
    # arquivo = open(endereco, 'w')
    arquivo.write(texto)
    arquivo.close()

#adiciona texto ao arquivo que já existe
#se não existe ele cria
def adicionar_texto(nome_arquivo, texto):
    arquivo=open (nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_texto(nome_do_arquivo):
    #esse nome do arquivo vai ser o nome que vai ser escrito no parêntese lá no main pra executar, por isso que pode
    #ser qualquer nome
    arquivo=open(nome_do_arquivo,'r')
    texto=arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    # pass
    arquivo=open(nome_arquivo,'r')
    aluno_nota=arquivo.read()
    # print(aluno_nota)
    aluno_nota=aluno_nota.split('\n') #o split transforma o arquivo em uma lista.
    #dentro do parêntese do split coloca o que ele vai usar para dividir as listas
    #coloquei o \n para separar por enter
    # print(aluno_nota)
    lista_media=[]
    for x in aluno_nota:
        # aluno=x[0] #quando eu coloco só o x e a posição sem o nome da lista, ele puxa apenas o caractere da posição
        # de cada item
        #se eu escrever o nome da lista com a posição, que ele vai imprimir o item todo
        # aluno1=aluno_nota[0]
        # print(aluno)
        # print(aluno1)
        lista_notas = x.split(',')
        aluno=lista_notas[0]
        # print(lista_notas)
        print(aluno)
        lista_notas.pop(0)
        print(lista_notas)
        # aluno = x[13] #fazendo dessa forma, ele pega letra por letra de cada item. Por exemplo se tiver 10, ele pega
        #apenas o 1 ou apenas o 0.
        # print(aluno)
        media = lambda notas: sum([int(i) for i in notas])/4
        print(media(lista_notas)) #acima a fórmula pode ser usada por qualquer lista, por isso tem que especificar
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

#para copiar um arquivo para outro diretório
def copia_arquivo(nome_arquivo):
    import shutil         #shutil é uma biblioteca do python
    shutil.copy(nome_arquivo, 'C:/Users/Sandy/Documents/ADS/Projetos em Python')

#como mover um arquivo
def move_arquivo(nome_arquivo):
    import shutil #pode colocar o import aqui ou no início do código, pois caso coloque no início, qualquer def pode usar
    shutil.move(nome_arquivo,'C:/Users/Sandy/Documents/ADS/Projetos em Python')

if __name__ == '__main__':
    move_arquivo('notas.txt')
    # copia_arquivo('notas.txt')
    # lista_media=media_notas('notas.txt')
    # print (lista_media)
    # media_notas('notas.txt')
    # escrever_texto('Aprendendo escrever e puxar metodos\n')
    # aluno = 'Cesar,9,8,6,10\n'
    # adicionar_texto('notas.txt', aluno)
    # ler_texto('teste.txt')