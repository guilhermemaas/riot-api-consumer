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
    
    def get_summoner_profile(self) -> dict:
        URL = f'{self.base_URL}/summoner/{self.api_version}/summoners/{self.summoner_id}?api_key={self.api_key}'
        response = requests.get(URL)
        return response.json()
    
    def get_matches_by_summoner(self) -> list:
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
    
    def get_leagues_by_ranking(self, tier: str, division: str):
        URL = f'{self.base_URL}/league/{self.api_version}/entries/{tier}/{division}?api_key={self.api_key}'
        response = requests.get(URL)
        return response.json()
    
    def get_league_details_by_league_id(self, league_id:str):
        URL = f'{self.base_URL}/league/{self.api_version}/leagues/{league_id}?api_key={self.api_key}'
        response = requests.get(URL)
        return response.json()
    
    
def new_api(api_key: str, summoner_region='br1', summoner_name='Ilha Nublar'):
    return ConsumerApiRiot(api_key, summoner_region, summoner_name)