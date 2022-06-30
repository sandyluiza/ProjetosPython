#utilizando data e hora
#para usar data em python precisa importar o date do datetime
from datetime import date, time, datetime, timedelta
#date é para trabalhar apenas com data
#time é para trabalhar apenas com hora
#datetime é para trabalhar com data e hora juntas
#timedelta é para fazer contas usando hora e data


def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual)
    print(type(data_atual))
    print(data_atual.strftime('%d/%m/%Y')) #essa função strftime transforma o dado em string no formato que colocar entre
    #parêntese
    #o y minusculo pega apenas 2 digitos do ano, com o Y maiusculo pega os 4
    print(type(data_atual))
    #se converter a data para usar nome, ela se torna uma string e com isso não dá para fazer algumas ações como calculo
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(data_atual_str)
    print((type(data_atual_str)))

def trabalhando_com_time():
    # pass    #usa-se o pass quando ainda vai adicionar as informações, mas se quer executar pra ver se foi tudo bem até
    #agora
    horario = time(hour=5, minute=18, second=30)
    print(horario)
    print(type(horario))
    # return (horario)
    horario_str=(horario.strftime('%Hh %Mm %Ss')) #mudando o formato
    print(type(horario_str))

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    data_atual_str= (data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual_str)
    # print(type(data_atual_str))
    data_atual_1 = (data_atual.strftime(('%c')))
    print(data_atual_1)
    print(data_atual.day)
    print(data_atual.month)
    print(data_atual.year)
    print(data_atual.hour)
    print(data_atual.minute)
    print(data_atual.second)
    print(data_atual.weekday())
    tupla=('Segunda','Terca','Quarta','Quinta','Sexta','Sabado','Domingo')
    print(tupla[data_atual.weekday()])   #mesmo sendo tupla, quando coloca posição precisa estar entre colchetes
    data_criada=datetime(2018, 12, 27, 16, 20, 30)
    print(data_criada)
    data_criada_1 = data_criada.strftime('%d/%m/%Y %H:%M:%S')
    print(data_criada_1)
    data_string = '05/07/2021 12:22:30'
    print(type(data_string))
    data_string_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S') #para converter uma texto em data.
    #o verdinho quer dizer o formato que a data em string está para que o programa achei o que é dia, mes e ano e hora
    print(data_string_convertida)
    print(type(data_string_convertida))
    #fazendo operações matemáticas com data e hora
    nova_data= data_string_convertida - timedelta(days=365, hours=2, minutes=15)
    print(nova_data)

if __name__ == '__main__':
    # trabalhando_com_date()
    # print(trabalhando_com_time())
    # trabalhando_com_time()
    trabalhando_com_datetime()