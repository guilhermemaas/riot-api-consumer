import pytest
import requests

"""
1 - Quero consultar o um Invocador afim de buscar seus dados no modo de jogo TFT.
"""

class ConsumerApiRiot:
    def __init__(self, api_key: str, region_id: str, invocador_name='xyz'):
        self.api_key = api_key
        self.region_id = region_id
        self.invocador_name = invocador_name
        
    def tft_consultar_invocador_por_nome(self):
        URL = 'https://'+self.region_id+'.api.riotgames.com/tft/summoner/v1/summoners/by-name/'+self.invocador_name+'?api_key='+self.api_key
        response = requests.get(URL)
        return response.json()

nova_consulta = ConsumerApiRiot('RGAPI-5daaaf89-04a4-4cb6-a4d3-ead57eb6ad69', 'br1', 'Ieko')
response_consulta = nova_consulta.tft_consultar_invocador_por_nome()
print(type(response_consulta))
for key, value in response_consulta.items():
    print(key, value)

@pytest.fixture()
def retorna_api_key_riot_para_consulta() -> str:
    with open('riot_api_key.txt', 'r') as key:
        return key.read()

    
@pytest.fixture()
def retorna_infos_invovacador_testes() -> str:
    """Perfil do Leko"""
    return {
        'invocador_id': 1640, 
        'invocador_name': 'Ieko', 
        'region_id': 'br1'
        }

invocador_infos = {}
invocador_infos = retorna_infos_invovacador_testes()
print(invocador_infos)
def gera_consumidor_api_riot(retorna_api_key_riot_para_consulta, retorna_infos_invovacador_testes):
    return ConsumerApi(retorna_api_key_riot_para_consulta)


def test_retornar_informacoes_summoner_tft_por_nome(retorna_api_key_riot_para_consulta: str, nome_invocador: str):
    pass