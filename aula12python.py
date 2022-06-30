import requests
#acessar funções no requests

def retorna_dados_cep(cep):
    response=requests.get('https://viacep.com.br/ws/{}/json'.format(cep))
    print(response.status_code)
    #vai aparecer 200 que quer dizer que foi com sucesso
    print(response.text)
    print(type(response.text))
    print(response.json())
    print(type(response.json())) #está em formato de dicionário
    dados_cep=response.json()
    print(dados_cep['logradouro'])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response=requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon=response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    # retorna_dados_cep('42701350')]
    # dados_pokemon=retorna_dados_pokemon('pikachu')
    # print(dados_pokemon['sprites']['front_shiny']) #da pra fazer programa falando pra pessoa informar o nome do pokemon
    # # e abre a imagem
    # print(dados_pokemon['sprites']['front_default'])
    response = retorna_response('https://www.instagram.com/p/CJUoz6wpzNWd3oD8aDrBx5I5Y8L7edDt2C3iUg0/')
    print(response)