# # if __name__ == '__main__':
# d = {'A': 1, 'B': 2, 'C': 3}
# # d['A'] = d['A'] + 100
# for i in d.keys():
#     # print(i)
#     d[i] = d[i] + 3
# print(d)
# # #     # total = sum(d[x] for x in d)
# #
# #     print(d['A'])
# my_list=[5,10,7,5,6,8,5,15]
#
# my_list = [9 if value == 5 else value for value in my_list]
#
# print(my_list)
#
# if __name__ == '__main__':
#     a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    # a = [0 if x % 2 == 1 else x for x in a]
# print(d)  # imprime [0, 2, 0, 4, 0, 6, 0, 8, 0]

#
# mochila= {'tochas': 2, 'cristais de rubi': 0, 'cristais de esmeralda': 2}
# mochila.update(tochas=1)
# print(mochila)

# import random
#
# x = 0
# while x != 10:
#     x = random.randint(1, 10)
#     # prin(x)
# print(x)


# x = random.randint(1,52)
#
# print(x)
#
# x = random.randrange(1,52)
#
# print(x)

# inventory = {'nome': 'SandyLuiza',
#  'moedas': 6600,
#  'objetos': ['espada de madeira', 'armadura de pano', 'escudo de bronze'],
#  'bolso': '',
#  'mochila': {'tochas': 2, 'cristais de rubi': 0}}
#
# inventory['bolso'] = dict(inventory['bolso'])
# inventory['bolso']['sacola'] = 'pederneira'
# print(dict(inventory['bolso']))
# print(type(inventory['bolso']))
# inventory['bolso'] = dict({'sacola':'pederneira'})
# # print(type(inventory['bolso']))
# # (map(dict, inventory['bolso'])).update(sacola = 'pederneira')
# #
# # #TERMINE SEU CÓDIGO AQUI
#
# print(inventory)
# for i in inventory['mochila'].keys():
#   inventory['mochila'][i] = inventory['mochila'][i] + 3
#
# print(inventory)

# inventory['e-mail'] = 'sandyluimo@hotmail.com'
# print(inventory)

n, m = list(map(int, input().split()))

grp_a = [input() for _ in range(n)]
grp_b = [input() for _ in range(m)]

dct = defaultdict(set)

[dct[elem].add(indx + 1) for indx, elem in enumerate(grp_a) if elem in grp_b]
[dct[string].add(-1) for string in grp_b if string not in grp_a]

for string in grp_b:
  for value in sorted(dct[string]):
      print(value, end=' ')
  print()

