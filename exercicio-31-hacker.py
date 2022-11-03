import calendar
# print (calendar.TextCalendar(firstweekday=6).formatyear(2015))
# Sobre o firstweekday, é o índice para o calendário começar com algum dia na semana.
# Por exemplo "eu quero que a coluna do calendario comece na terça ao invés de no domingo"
# daí altera o número.
# Para começar no domingo, o indice precisa ser 6

mes, dia, ano = map(int, input().split())
# calendar.weekday(year, month, day)¶
name = (calendar.weekday(ano, mes, dia))
if name == 0:
    print('MONDAY')
elif name == 1:
    print('TUESDAY')
elif name == 2:
    print('WEDNESDAY')
elif name == 3:
    print('THURSDAY')
elif name == 4:
    print('FRIDAY')
elif name == 5:
    print('SATURDAY')
elif name == 6:
    print('SUNDAY')