#trabalhando com função

def is_leap(year):
    leap = False

    resto_div_4 = year % 4
    resto_div_100 = year % 100
    resto_div_400 = year % 400

    if resto_div_4 == 0:
        leap = True

        if resto_div_100 == 0:
            leap = False

            if resto_div_400 == 0:
                leap = True

    else:
        leap = False

    return leap


year = int(input('Informe o ano '))
print(is_leap(year))