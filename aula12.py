import requests
from requests.models import Response

def retornaDadosCEP(cep):

    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.text)
    dadosCEP = response.json()

    print(dadosCEP['logradouro'])
    print(dadosCEP['complemento'])
    return dadosCEP

def retornaDadosPoke(poke):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(poke))
    dadosPoke = response.json()
    return dadosPoke

def retornaResponse(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    response = retornaResponse('https://www.sonda.com/en/')
    print(response)
    # retornaDadosCEP("09852820")
    # dadosPoke = retornaDadosPoke("pikachu")
    # print(dadosPoke['sprites']['front_shiny'])