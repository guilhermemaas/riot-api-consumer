import pytest
import requests

"""
Riot TFT API
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
        self.base_URL = f'https://{self.summoner_region}.api.riotgames.com/tft'
        self.base_URL_tft = f'https://americas.api.riotgames.com/tft'
    
    def summoner_profile(self) -> dict:
        URL = f'{self.base_URL}/summoner/{self.api_version}/summoners/{self.summoner_id}?api_key={self.api_key}'
        response = requests.get(URL)
        return response.json()
    
    def last_matches(self) -> list:
        count_matches = 20
        URL = f'{self.base_URL_tft}/match/{self.api_version}/matches/by-puuid/{self.puuid}/ids?count={count_matches}&api_key={self.api_key}'
        response = requests.get(URL)
        return response.json()
    
    def get_match_by_match_id(self, match: str):
        URL = f'{self.base_URL_tft}/match/{self.api_version}/matches/{match}?api_key={self.api_key}'
        response = requests.get(URL)
        return response.json()
    
    def get_challenger_league(self):
        URL = f'{self.base_URL}/league/{self.api_version}/challenger?api_key={self.api_key}'
        response = requests.get(URL)
        return response.json()
    
    def get_grandmaster_league(self):
        URL = f'{self.base_URL}/league/{self.api_version}/grandmaster?api_key={self.api_key}'
        response = requests.get(URL)
        return response.json()

    def get_master_league(self):
        URL = f'{self.base_URL}/league/{self.api_version}/master?api_key={self.api_key}'
        response = requests.get(URL)
        return response.json()
    
    def get_player_ranked_status(self):
        URL = f'{self.base_URL}/league/{self.api_version}/entries/by-summoner/{self.summoner_id}?api_key={self.api_key}'
        response = requests.get(URL)
        return response.json()
    
    
def new_api(api_key: str, summoner_region='br1', summoner_name='Ilha Nublar'):
    return ConsumerApiRiot(api_key, summoner_region, summoner_name)


@pytest.fixture()
def retorna_api_key_riot_para_consulta():
    with open('riot_api_key.txt', 'r') as key:
        return key.read()

    
@pytest.fixture()
def example_summoner_Ieko():
    """
    Perfil Exemplo example_summoner_Ieko
    Summoner Name: Ieko
    Region: Brazil
    """
    return {
        'summoner_name': 'Ieko',
        'summoner_region': 'br1',
        }


@pytest.fixture()
def example_summoner_ilha_nublar():
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
    api = new_api(api_key, ilha_nublar['summoner_region'],
                            ilha_nublar['summoner_name']) 
    assert api.api_session['id'] == '5AtW4neaL009Zy-jUjHLbal7PcsGqQvSpB26-S_hfTTi'
    
    
def test_tft_summoner_profile_by_id(retorna_api_key_riot_para_consulta, example_summoner_ilha_nublar):
    """
    Testing the consume of /tft/summoner/v1/summoners/by-account/{encryptedAccountId}
    Summoner Name: Ilha Nublar
    """
    api_key = retorna_api_key_riot_para_consulta
    ilha_nublar = example_summoner_ilha_nublar
    api = new_api(api_key, ilha_nublar['summoner_region'], 
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
    api = new_api(api_key, ilha_nublar['summoner_region'],
                           ilha_nublar['summoner_name'])
    tft = api.TFT.last_matches()
    for match in ilha_nublar['tft_last_matches']:
        assert match in tft
        
    
def test_get_match_by_match_id_metadata_participants(retorna_api_key_riot_para_consulta, example_summoner_ilha_nublar):
    """
    Testing the consume of /tft/match/v1/matches/{matchId}
    Summoner Name: Ilha Nublar
    """
    api_key = retorna_api_key_riot_para_consulta
    ilha_nublar = example_summoner_ilha_nublar
    api = new_api(api_key, ilha_nublar['summoner_region'],
                           ilha_nublar['summoner_name'])
    tft = api.TFT.get_match_by_match_id(ilha_nublar['tft_last_matches'][0])
    assert tft['metadata']['participants'] == [
            "nm2JSpP6N6KD1_QLyFeh7a1rsaqiy3AZLrtxYN6DsuHJqVMOo1-webHa41OTEWutfg6Uhi_CuZrJUg",
            "ijuMF8ZATGoIMz9bIYCYRB5TE7zSYsUDB-PP23qcqGRb_2UqafvObTlt3sQeAYlONuXgNXx1sMdYag",
            "2vnp9IKykBQheMSHaLZxi55nxhzUqmHgzB1W9DsZrFvsK2LJaUzGpf2roS3JwM3e_r4QoVHKE_BveA",
            "I7EzrZLIf9hYZQ16kkqqUNhRu2MJcYoohyrxkIHwCIJ0uKUNGbazyACXo4UR5JXkVF6X-Ik0qyoPXA",
            "IcRhE40UO4xEtQCN8SHkMWDhbLnPK7JsbBoaw7XECTWECMthv5EYX-_VkJLuYlxxhQOZPAvb2SY2tA",
            "fi570nWOGW6lJC0NaSWDMgTuXvD5Yl138zbO6FxLA0hhPgkp8LmeHALc-I6gIT4pzRW6Q1eFDHElAg",
            "oGymNs7Q9VpVdankY3Cq25C2r-sCPCM5-DN8drSa-MZ-qonpLlAKk1xIIQ_oy9SSmF9P1oUTPdZVug",
            "lPRGWj6euSdVWOKLMtPFWt4ah8N1SZJCRhRkzrfZmfrqDfllK1lwBQW87iFbc9LbGHtzyw097lMnww"
        ]
    
def test_get_match_by_match_id_info_game_datetime(retorna_api_key_riot_para_consulta, example_summoner_ilha_nublar):
    """
    Testing the consume of /tft/match/v1/matches/{matchId}
    Summoner Name: Ilha Nublar
    """
    api_key = retorna_api_key_riot_para_consulta
    ilha_nublar = example_summoner_ilha_nublar
    api = new_api(api_key, ilha_nublar['summoner_region'],
                           ilha_nublar['summoner_name'])
    tft = api.TFT.get_match_by_match_id(ilha_nublar['tft_last_matches'][0])
    assert tft['info']['game_datetime'] == 1584585338593
    

def test_get_challenger_league(retorna_api_key_riot_para_consulta):
    """
    Testing the consume of /tft/league/v1/challenger
    """
    api_key = retorna_api_key_riot_para_consulta
    api = new_api(api_key)
    tft = api.TFT.get_challenger_league()
    assert tft['tier'] == 'CHALLENGER'
    assert tft['queue'] == 'RANKED_TFT'
    

def test_get_grandmaster_league(retorna_api_key_riot_para_consulta):
    """
    Testing the consume of /tft/league/v1/grandmaster
    """
    api_key = retorna_api_key_riot_para_consulta
    api = new_api(api_key)
    tft = api.TFT.get_grandmaster_league()
    assert tft['tier'] == 'GRANDMASTER'
    assert tft['queue'] == 'RANKED_TFT'
    

def test_get_master_league(retorna_api_key_riot_para_consulta):
    """
    Testing the consume of /tft/league/v1/master
    """
    api_key = retorna_api_key_riot_para_consulta
    api = new_api(api_key)
    tft = api.TFT.get_master_league()
    assert tft['tier'] == 'MASTER'
    assert tft['queue'] == 'RANKED_TFT'
    
    
def test_get_player_ranked_status(retorna_api_key_riot_para_consulta, example_summoner_Ieko):
    """
    Testing the consumo of /tft/league/v1/entries/by-summoner/{encryptedSummonerId}
    Summoner Name: Ieko
    Region: Brazil
    """
    api_key = retorna_api_key_riot_para_consulta
    leko = example_summoner_Ieko
    api = new_api(api_key, leko['summoner_region'],
                        leko['summoner_name'])
    tft = api.TFT.get_player_ranked_status()
    assert tft[0]['queueType'] == 'RANKED_TFT'
    assert tft[0]['summonerId'] == 'bbYwQtET_GWwodvvxU3i5DEEXsdF3ujtDWfmMTldpfKG3g'