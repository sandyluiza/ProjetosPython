# Detalhes
# Maximinizar o Retorno Financeiro
# Alocando recursos
# Orçamento específico

# def Melhor_opcao_invest (self):
#     opcao_1 =

from itertools import permutations


# if __name__ == '__main__':

# Lendo as variáveis
Capital_para_invest = float(input())
Quant_opcoes_invest = int(input())
Opcoes_investimentos = []
for _ in range(Quant_opcoes_invest):
    Opcao_custo_retorno = input().split()
    Opcoes_investimentos.append(Opcao_custo_retorno)
print(Opcoes_investimentos)

# Somando até atingir o Capital
valor_gasto = 0
investimentos_somados = []
lucro_gerado = 0
permutacao = list(permutations(Opcoes_investimentos))
# print(permutacao)
# print(type(permutacao))
lucro_gerado_ultimo = 0
valor_gasto_ultimo = 0
investimentos_somados_ultimo = []

for x in permutacao:
    for y in x:
        print(y)
        valor_gasto = valor_gasto + int(y[1])
        if valor_gasto <= Capital_para_invest:
            investimentos_somados.append(y[0])
            lucro_gerado = lucro_gerado + int(y[2])
        else:
            valor_gasto = valor_gasto - int(y[1])
    print(lucro_gerado, valor_gasto, investimentos_somados)

    if lucro_gerado_ultimo > lucro_gerado:
        lucro_gerado = 0
        valor_gasto = 0
        investimentos_somados = []
    else:
        lucro_gerado_ultimo = lucro_gerado
        valor_gasto_ultimo = valor_gasto
        investimentos_somados_ultimo = investimentos_somados
        lucro_gerado = 0
        valor_gasto = 0
        investimentos_somados = []



    #
    #
print(valor_gasto_ultimo, investimentos_somados_ultimo, lucro_gerado_ultimo)

    # if lucro_gerado_ultimo <= lucro_gerado:
        #     lucro_gerado_ultimo = lucro_gerado
        #     valor_gasto_ultimo = valor_gasto
        #     investimentos_somados_ultimo = investimentos_somados


# print(lucro_gerado, valor_gasto, investimentos_somados)

