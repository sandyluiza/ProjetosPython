def calcula_top_ocorrencias_de_queries(texto,queries,k):
    dicio = {}
    quant_carac = len(texto)
    result = []
    result_1 = []

    for j in range(len(queries)):
        cont = 0
        for i in range(quant_carac):
            if texto[i:].startswith(queries[j]):
                cont = cont + 1
        dicio[queries[j]] = cont

    for i in sorted(dicio, key=dicio.get, reverse=True):
        result.append(i)

    for i in range(k):
        result_1.append(result[i])

    print(result_1)

    return result_1


if __name__ == '__main__':
    texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
    queries = ["a", "em", "i", "el"]
    k = 2
    calcula_top_ocorrencias_de_queries(texto,queries,k)
