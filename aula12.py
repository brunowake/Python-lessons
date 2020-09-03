import requests
def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.json())
    dados_cep = response.json()
    print(dados_cep['logradouro'])

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))

    return response.json()

def retorna_response(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    retorna_dados_cep('22041001')
    dados_pokemon = retorna_dados_pokemon('pikachu')
    print(dados_pokemon['sprites']['front_shiny'])

    print(retorna_response('https://google.com'))