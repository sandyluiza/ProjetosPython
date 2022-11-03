def escolhe_taxi(tf1,vqr1,tf2,vqr2):
    cont = 0
    tf1 = float(tf1)
    vqr1 = float(vqr1)
    tf2 = float(tf2)
    vqr2 = float(vqr2)

    if (tf1 > tf2) and (vqr1 > vqr2):
        result = 'Empresa 2'
    elif (tf1 < tf2) and (vqr1 < vqr2):
        result = 'Empresa 1'
    elif (tf1 == tf2) and (vqr1 == vqr2):
        result = 'Tanto faz'
    else:
        soma1 = tf1 + vqr1
        soma2 = tf2 + vqr2
        if (soma1 > soma2) and (vqr1 > vqr2):
            result = 'Empresa 2'
        elif (soma1 < soma2) and (vqr1 < vqr2):
            result = 'Empresa 1'
        elif ((soma1 > soma2) and (vqr1 < vqr2)):
            while (soma1 > soma2):
                soma1 = tf1 + vqr1 * cont
                soma2 = tf2 + vqr2 * cont
                cont = cont + 0.001
            cont = cont - 0.001
            cont1 = cont * 100
            cont1 = int(cont1)
            cont1 = str(cont1)
            cont1 = list(cont1)
            ultimo = int(cont1[len(cont1) - 1])

            if (ultimo < 2):
                result = 'Empresa 2 quando a distância < {:.1f}, Tanto faz quando a distância = {:.1f}, Empresa 1 quando a distância > {:.1f}'.format(
                    cont, cont, cont)
            else:
                result = 'Empresa 2 quando a distância < {:.2f}, Tanto faz quando a distância = {:.2f}, Empresa 1 quando a distância > {:.2f}'.format(
                    cont, cont, cont)

        elif ((soma1 < soma2) and (vqr1 > vqr2)):
            while (soma1 < soma2):
                soma1 = tf1 + vqr1 * cont
                soma2 = tf2 + vqr2 * cont
                cont = cont + 0.001
            cont = cont - 0.001
            cont1 = cont * 100
            cont1 = int(cont1)
            cont1 = str(cont1)
            cont1 = list(cont1)
            ultimo = int(cont1[len(cont1) - 1])
            print(cont)
            if (ultimo < 2):
                result = 'Empresa 1 quando a distância < {:.1f}, Tanto faz quando a distância = {:.1f}, Empresa 2 quando a distância > {:.1f}'.format(
                    cont, cont, cont)
            else:
                result = 'Empresa 1 quando a distância < {:.2f}, Tanto faz quando a distância = {:.2f}, Empresa 2 quando a distância > {:.2f}'.format(
                    cont, cont, cont)
    print(result)
    print(ultimo)
    return result

if __name__ == '__main__':
    tf1 = 2.50
    vqr1 = 1.00
    tf2 = 5.00
    vqr2 = 0.75
    escolhe_taxi(tf1,vqr1,tf2,vqr2)
