# Trabalhando com dicionarios
informacoes_de_pessoas = {
    "Sandy Luiza": "SanLuiza",
    "Rafael Augusto": "Rafinha",
    "Luke Oliveira": "Lukinho",
    "Leia Oliveira": "Leia"
}
# print(type(informacoes_de_pessoas))
# print(informacoes_de_pessoas)

# Para pegar alguma resposta do dicionario:
# print(informacoes_de_pessoas["Rafael Augusto"])

# Para adicionar item:
informacoes_de_pessoas["Alvo Oliveira"] = "Alvinho"
# print(informacoes_de_pessoas)

# Para pegar os nomes das chaves:
# nomes_das_pessoas = []
# for nome_da_pessoa in informacoes_de_pessoas:
#     nomes_das_pessoas.append(nome_da_pessoa)
# print(nomes_das_pessoas)
#OU
# nomes_das_pessoas = dict.keys(informacoes_de_pessoas)
# print(type(nomes_das_pessoas))
# print(nomes_das_pessoas)
# nomes_das_pessoas = list(nomes_das_pessoas)
# print(nomes_das_pessoas)
# #OU
# nomes_das_pessoas = informacoes_de_pessoas.keys()
# print(nomes_das_pessoas)

# Para pegar apenas os valores:
# print(dict.values(informacoes_de_pessoas))
# OU
# apelidos = []
# for nomes_das_pessoas in informacoes_de_pessoas:
#     apelido = informacoes_de_pessoas[nomes_das_pessoas]
#     apelidos.append(apelido)
# print(apelidos)
# OU
# apelidos = informacoes_de_pessoas.values()
# print(apelidos)

# Para retirar um item do dicionario:
# informacoes_de_pessoas.pop("Sandy Luiza")
print(informacoes_de_pessoas)

# Verificar se existe um dado no dicionario:
# if "Sandy Luiza" in informacoes_de_pessoas:
#     print('Existe')
# else:
#     print('Não existe')