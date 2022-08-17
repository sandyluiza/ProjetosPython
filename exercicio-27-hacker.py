# Trabalhando com coordenadas
# O módulo cmath do Python fornece acesso às funções matemáticas para números complexos.
# Phase retorna a fase do número complexo(também conhecido como argumento de z).
# ABS retorna o módulo (valor absoluto) do número complexo.
from cmath import phase

def conversao (self):
    print(abs(self))
    print(phase(self))

if __name__ == '__main__':
    z = complex(input())
    conversao(z)