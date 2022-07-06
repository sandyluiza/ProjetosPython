# Desenhar um tapete
# N = número natural ímpar - colunas
# M = 3 x N - largura
# WELCOME escrito no centro
# caracteres | . -
# Entrada = N M

# Lendo as entradas
N, M = input().split(' ')
N = int(N)
M = int(M)
O = 'WELCOME'
P = '|'
Q = '.'
R = '-'
S = len(O)
T = int((M-S)/2)   #largura para o nome
# print(T)
# print(N)
# print(type(N))
# print(M)
# print(type(M))
U = Q+P+Q

# Fazendo a parte dos pontinhos e tracinhos
for i in range(2, int(N+1), 2):
    X = U*(i-1) # parte dos pontinhos
    Z = len(X)  # parte dos tracinhos
    Y = int((M-Z)/2)    # parte dos tracinhos
    print((R*Y)+X.center(0)+(R*Y))

# Fazendo o meio do tapete
# for i in range(M):
print((R*T)+O+(R*T))

# Fazendo a parte dos pontinho debaixo
v = int(N-1)
for i in range(1, int(N+1), 2):
    W = U*(v-i) #parte dos pontinhos
    A = len(W)  #parte dos tracinhos
    B = int((M-A)/2)  #parte dos tracinhos
    if W == '':
        break
    print((R*B)+W.center(0)+(R*B))

