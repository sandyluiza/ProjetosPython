# # Usando defaultdict
# # A ferramenta defaultdict é um contêiner na classe collections do Python. É semelhante ao contêiner de dicionário usual
# # ( dict ), mas a única diferença é que um defaultdict terá um valor padrão se essa chave ainda não tiver sido definida
# from collections import defaultdict
#
# def determ_posic_defaultdict(comp_grupo_a, comp_grupo_b):
#     defaultdic = defaultdict(list)
#     indice = 0
#     posicao_a = {}
#     # posicao_a = []
#     # posicao_b = []
#     for _ in range(comp_grupo_a):
#         defaultdic['a'].append(input())
#     for _ in range(comp_grupo_b):
#         defaultdic['b'].append(input())
#
#     # for i in defaultdic.items():
#     #     print(i)
#
#     for i in defaultdic['a']:
#         indice = indice + 1
#         posicao_a.setdefault(i,[])
#         posicao_a[i].append(indice)
#     print(posicao_a)
#
#     for i in posicao_a.values():
#         print(*i)
#
#     if 'c' in defaultdic['b']:
#         print(-1)
#
#     # o asterisco tira os colchetes e virgulas
#         # if i == 'a':
#         #     posicao_a.append(indice)
#         # if i == 'b':
#         #     posicao_b.append(indice)
#     # for i in range(comp_grupo_a):
#     #     if 'uma' in defaultdic['a']:
#     #         posicao_a.append(i)
#     #
#     #     if 'b' in defaultdic['a']:
#     #         posicao_b.append(i)
#
#     # print(posicao_a)
#     # print(posicao_b)
#
#
#
# if __name__ == '__main__':
#     comp_grupo_a, comp_grupo_b = map(int, input().split())
#     determ_posic_defaultdict(comp_grupo_a, comp_grupo_b)
# #
# n,m=map(int,input().split())
# d={}
# for i in range(n):
#     w=input()
#     d.setdefault(w,[])
#     print(d)
#     d[w].append(i+1)
# for i in range(m):
#     w=input()
#     print(*d[w]) if w in d else print(-1)

from collections import defaultdict


def determ_posic_defaultdict(comp_grupo_a, comp_grupo_b):
    defaultdic = defaultdict(list)
    indice = 0
    posicao = {}
    for _ in range(comp_grupo_a):
        defaultdic['a'].append(input())
    for _ in range(comp_grupo_b):
        defaultdic['b'].append((input()))
    for i in defaultdic['a']:
        indice = indice + 1
        posicao.setdefault(i, [])
        posicao[i].append(indice)
        # print(posicao)
    for i in posicao.values():
        if comp_grupo_a == 1:
            pass
        else:
            print(*i)

    for i in defaultdic['b']:
        for j in i:
            if 'c' in j:
                print(-1)
                return

if __name__ == '__main__':
    comp_grupo_a, comp_grupo_b = map(int, input().split())
    determ_posic_defaultdict(comp_grupo_a, comp_grupo_b)

