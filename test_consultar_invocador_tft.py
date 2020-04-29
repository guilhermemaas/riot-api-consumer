import pytest
import requests

"""
1) Quero consultar o um Invocador afim de buscar seus dados no modo de jogo TFT.
2) Quero consultar as informacoes de liga ranqueada por jogador no TFT.
"""

"""class ConsumerApiRiot:
    def __init__(self, api_key: str, region_id: str, invocador_name='xyz', invocador_id_incripted='xyz'):
        self.api_key = api_key
        self.region_id = region_id
        self.invocador_name = invocador_name
        self.invocador_id_incripted = invocador_id_incripted
        
    def tft_consultar_invocador_por_nome(self):
        URL = 'https://'+self.region_id+'.api.riotgames.com/tft/summoner/v1/summoners/by-name/'+self.invocador_name+'?api_key='+self.api_key
        response = requests.get(URL)
        return response.json()
    
    def tft_consultar_liga_ranqueada_por_nome(self):
        URL = 'https://'+self.region_id+'.api.riotgames.com/tft/league/v1/entries/by-summoner/'+self.invocador_id_incripted+'?api_key='+self.api_key
        response = requests.get(URL)
        return response.json()
"""    
#nova_consulta = ConsumerApiRiot('RGAPI-5daaaf89-04a4-4cb6-a4d3-ead57eb6ad69', 'br1', 'Ieko')
#response_consulta = nova_consulta.tft_consultar_invocador_por_nome()
#print(type(response_consulta)) 
#for key, value in response_consulta.items():
#    print(key, value)

@pytest.fixture()
def retorna_api_key_riot_para_consulta() -> str:
    with open('riot_api_key.txt', 'r') as key:
        return key.read()

    
@pytest.fixture()
def retorna_infos_invovacador_testes() -> str:
    """Perfil Exemplo Leko"""
    return {
        'invocador_id': 1640, 
        'invocador_id_incripted': 'bbYwQtET_GWwodvvxU3i5DEEXsdF3ujtDWfmMTldpfKG3g',
        'invocador_name': 'Ieko', 
        'region_id': 'br1'
        }


#invocador_infos = {}
#invocador_infos = retorna_infos_invovacador_testes()
#print(invocador_infos)
"""
def gera_consumidor_api_riot(api_key: str, region_id: str, invocador_name: str, invocador_id_incripted: str):
    return ConsumerApiRiot(api_key, region_id, invocador_name, invocador_id_incripted)

def test_retornar_informacoes_summoner_tft_por_nome(retorna_api_key_riot_para_consulta, retorna_infos_invovacador_testes):
    api_key = retorna_api_key_riot_para_consulta
    exemplo_invocador = retorna_infos_invovacador_testes
    nova_consulta = gera_consumidor_api_riot(api_key, exemplo_invocador['region_id'], 
                                             exemplo_invocador['invocador_name'], exemplo_invocador['invocador_id_incripted'])
    response = nova_consulta.tft_consultar_invocador_por_nome()
    
    assert response['id'] == 'bbYwQtET_GWwodvvxU3i5DEEXsdF3ujtDWfmMTldpfKG3g'
    assert response['accountId'] == 'JBX0iKm6A6RLm7dQypws4XhOoX2O-ZHE1fQuI77uNhMPKnE'
    assert response['puuid'] == 'fRCUIJp8iKco_EdZcDE2BU8j5SsGcizXsh2uCFkSgxQrzZrgWhkAyUTyeUk7aQ7aFMkGOOMN6XIsFg'
    assert response['profileIconId'] == 1640
    

def test_retornar_informacoes_de_liga_tft_por_id(retorna_api_key_riot_para_consulta, retorna_infos_invovacador_testes):
    api_key = retorna_api_key_riot_para_consulta
    exemplo_invocador = retorna_infos_invovacador_testes
    nova_consulta = gera_consumidor_api_riot(api_key, exemplo_invocador['region_id'], 
                                             exemplo_invocador['invocador_name'], exemplo_invocador['invocador_id_incripted'])
    #nova_consulta.TFT.consultar_invocador_por_nome()
    response = nova_consulta.tft_consultar_liga_ranqueada_por_nome()
    for invocador in response:
        assert invocador['queueType'] == 'RANKED_TFT'
        assert invocador['summonerId'] == 'bbYwQtET_GWwodvvxU3i5DEEXsdF3ujtDWfmMTldpfKG3g'
"""      
#####################
#####################
#####################
    
class TftApi:
    def __init__(self, summoner_region:str, summoner_id: str, api_key: str):
        self.summoner_region = summoner_region
        self.summoner_id = summoner_id
        self.api_key = api_key
        self.api_version = 'v1'
        self.baseURL = f'https://{self.summoner_region}.api.riotgames.com/tft'
    
    def summoner_profile(self):
        URL = f'{self.baseURL}/summoner/{self.api_version}/summoners/{self.summoner_id}?api_key={self.api_key}'
        #print(f'URL - summoner_profile: {URL}')
        response = requests.get(URL)
        return response.json()
    
      
class ConsumerApiRiot2:
    def __init__(self, api_key: str, summoner_region: str, summoner_name='Ilha Nublar'):
        self.api_key = api_key
        self.summoner_region = summoner_region
        self.summoner_name = summoner_name
        
        def __init_session():
            URL = f'https://{self.summoner_region}.api.riotgames.com/tft/summoner/v1/summoners/by-name/{self.summoner_name}?api_key={self.api_key}'
            response = requests.get(URL)
            return response.json()
        
        self.api_session = __init_session()
        self.TFT = TftApi(self.summoner_region, self.api_session['id'], self.api_key) 


def api_riot_factory(api_key: str, summoner_region: str, summoner_name: str):
    return ConsumerApiRiot2(api_key, summoner_region, summoner_name)


@pytest.fixture()
def example_summoner_ilha_nublar() -> str:
    """Ilha Nublar Profile - Brazil"""
    return {
        'summoner_name': 'Ilha Nublar',
        'summoner_region': 'br1'
    }


def test_init_session(retorna_api_key_riot_para_consulta, example_summoner_ilha_nublar):
    """Testing init session
    Summoner Name: lha Nublar profile."""
    api_key = retorna_api_key_riot_para_consulta
    ilha_nublar = example_summoner_ilha_nublar
    api = api_riot_factory(api_key, ilha_nublar['summoner_region'],
                            ilha_nublar['summoner_name']) 
    assert api.api_session['id'] == '5AtW4neaL009Zy-jUjHLbal7PcsGqQvSpB26-S_hfTTi'
    
def test_summoner_profile_by_id(retorna_api_key_riot_para_consulta, example_summoner_ilha_nublar):
    """Testing the consume of /tft/summoner/v1/summoners/by-account/{encryptedAccountId}
    Summoner Name: Ilha Nublar
    """
    api_key = retorna_api_key_riot_para_consulta
    ilha_nublar = example_summoner_ilha_nublar
    api = api_riot_factory(api_key, ilha_nublar['summoner_region'], 
                           ilha_nublar['summoner_name'])
    tft = api.TFT.summoner_profile()
    assert tft['id'] =='5AtW4neaL009Zy-jUjHLbal7PcsGqQvSpB26-S_hfTTi'