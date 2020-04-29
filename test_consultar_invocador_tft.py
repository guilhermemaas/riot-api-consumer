import pytest
import requests

"""
1) Quero consultar o um Invocador afim de buscar seus dados no modo de jogo TFT.
2) Quero consultar as informacoes de liga ranqueada por jogador no TFT.
"""    

class ConsumerApiRiot:
    def __init__(self, api_key: str, summoner_region: str, summoner_name='Ilha Nublar'):
        self.api_key = api_key
        self.summoner_region = summoner_region
        self.summoner_name = summoner_name
        
        def __init_session():
            URL = f'https://{self.summoner_region}.api.riotgames.com/tft/summoner/v1/summoners/by-name/{self.summoner_name}?api_key={self.api_key}'
            response = requests.get(URL)
            return response.json()
        
        self.api_session = __init_session()
        self.TFT = TftApi(self.summoner_region, 
                          self.api_session['id'], 
                          self.api_key,
                          self.api_session['puuid']) 
        
            
class TftApi:
    def __init__(self, summoner_region:str, summoner_id: str, api_key: str, puuid: str):
        self.summoner_region = summoner_region
        self.summoner_id = summoner_id
        self.api_key = api_key
        self.puuid = puuid
        self.api_version = 'v1'
        self.baseURL = f'https://{self.summoner_region}.api.riotgames.com/tft'
        self.baseURLtft_match = f'https://americas.api.riotgames.com/tft'
    
    def summoner_profile(self):
        URL = f'{self.baseURL}/summoner/{self.api_version}/summoners/{self.summoner_id}?api_key={self.api_key}'
        response = requests.get(URL)
        return response.json()
    
    def last_matches(self):
        count_matches = 20
        URL = f'{self.baseURLtft_match}/match/{self.api_version}/matches/by-puuid/{self.puuid}/ids?count={count_matches}&api_key={self.api_key}'
        response = requests.get(URL)
        return response.json()
    

def api_riot_factory(api_key: str, summoner_region: str, summoner_name: str):
    return ConsumerApiRiot(api_key, summoner_region, summoner_name)


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


@pytest.fixture()
def example_summoner_ilha_nublar() -> str:
    """
    Summoner Name: Ilha Nubllar
    Region: Brazil
    """
    return {
        'summoner_name': 'Ilha Nublar',
        'summoner_region': 'br1',
        'tft_last_matches': [
            'BR1_1882323432',
            'BR1_1775035230',
            'BR1_1770334549',
            'BR1_1770273342',
            'BR1_1769520122'
        ]
    }


def test_init_session(retorna_api_key_riot_para_consulta, example_summoner_ilha_nublar):
    """
    Testing init session
    Summoner Name: lha Nublar profile.
    """
    api_key = retorna_api_key_riot_para_consulta
    ilha_nublar = example_summoner_ilha_nublar
    api = api_riot_factory(api_key, ilha_nublar['summoner_region'],
                            ilha_nublar['summoner_name']) 
    assert api.api_session['id'] == '5AtW4neaL009Zy-jUjHLbal7PcsGqQvSpB26-S_hfTTi'
    
    
def test_tft_summoner_profile_by_id(retorna_api_key_riot_para_consulta, example_summoner_ilha_nublar):
    """
    Testing the consume of /tft/summoner/v1/summoners/by-account/{encryptedAccountId}
    Summoner Name: Ilha Nublar
    """
    api_key = retorna_api_key_riot_para_consulta
    ilha_nublar = example_summoner_ilha_nublar
    api = api_riot_factory(api_key, ilha_nublar['summoner_region'], 
                           ilha_nublar['summoner_name'])
    tft = api.TFT.summoner_profile()
    assert tft['id'] =='5AtW4neaL009Zy-jUjHLbal7PcsGqQvSpB26-S_hfTTi'
    
    
def test_tft_matches_by_puuid(retorna_api_key_riot_para_consulta, example_summoner_ilha_nublar):
    """
    Testing the consume of /tft/match/v1/matches/by-puuid/{puuid}/ids
    Summoner Name: Ilha Nublar
    """
    api_key = retorna_api_key_riot_para_consulta
    ilha_nublar = example_summoner_ilha_nublar
    api = api_riot_factory(api_key, ilha_nublar['summoner_region'],
                           ilha_nublar['summoner_name'])
    tft = api.TFT.last_matches()
    for match in ilha_nublar['tft_last_matches']:
        assert match in tft