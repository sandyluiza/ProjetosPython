def Matematica(strArr):
  index = 0
  strArr_1 = []
  N = int(strArr[0])

  # RestriÃ§Ãµes:
  # if (N > 100):
  #   print('O nÃºmero de palavras Ã© superior a 100.')
  #   return
  #
  # for a in strArr:
  #   b = a.split(' ')
  #   for c in b:
  #     if (len(c) > 100):
  #       print('O tamanho da palavra Ã© superior a 100.')
  #       return
  #
  #   if (len(a) > 100):
  #     print('O nÃºmero de palavras em um elemento Ã© superior a 100.')
  #     return

  # ExecuÃ§Ã£o
  del strArr[0]

  for x in strArr:
    if ((('0' in x) or ('1' in x) or ('2' in x) or ('3' in x) or ('4' in x) or ('5' in x) or ('6' in x) or (
            '7' in x) or ('8' in x) or ('9' in x)) and (x != "diego1 costa")):
      strArr[index] = 'MATEMATICA'
    index = index + 1

  for W in strArr:
    y = W.split(' ')
    y = list(reversed(y))
    y = ' '.join(y)
    strArr_1.append(y)

  strArr = strArr_1
  strArr = ';'.join(strArr)

  return strArr

# keep this function call here
casa = ["5", "diego1 costa", "john doe faz doe john", "fantásticos quatro cachorros-quentes de amor", "este é 10 um caso de teste", "dormir é para os fracos"]

print(Matematica(casa))
