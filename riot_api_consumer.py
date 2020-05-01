import pytest
import requests


"""
For understand more about Riot Api access this link:
https://developer.riotgames.com/
For now, the focus is simplify the use of endpoints of this categories:
TFT-LEAGUE-V1
TFT-MATCH-V1
TFT-SUMMONER-V1
For details about the use, visit the github page:
https://github.com/guilhermemaas/riot-api-consumer
"""    


class ConsumerRiotApi:
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
        """
        You can get the profile information of a summoner.
        """
        URL = f'{self.base_URL}/summoner/{self.api_version}/summoners/{self.summoner_id}?api_key={self.api_key}'
        response = requests.get(URL)
        return response.json()
    
    def get_matches_by_summoner(self, count_matches) -> list:
        """
        You can get the code of lastest matches of a summoner
        """
        URL = f'{self.base_URL_tft}/match/{self.api_version}/matches/by-puuid/{self.puuid}/ids?count={count_matches}&api_key={self.api_key}'
        response = requests.get(URL)
        return response.json()
    
    def get_match_by_match_id(self, match: str) -> list:
        """
        You can get the details of match, by code match 
        """
        URL = f'{self.base_URL_tft}/match/{self.api_version}/matches/{match}?api_key={self.api_key}'
        response = requests.get(URL)
        return response.json()
    
    def get_challenger_league(self) -> list:
        """
        You can get the list of all challengers players  
        """
        URL = f'{self.base_URL}/league/{self.api_version}/challenger?api_key={self.api_key}'
        response = requests.get(URL)
        return response.json()
    
    def get_grandmaster_league(self) -> list:
        """
        You can get the list of all grandmaster players  
        """
        URL = f'{self.base_URL}/league/{self.api_version}/grandmaster?api_key={self.api_key}'
        response = requests.get(URL)
        return response.json()

    def get_master_league(self) -> list:
        """
        You can get the list of all master players
        """
        URL = f'{self.base_URL}/league/{self.api_version}/master?api_key={self.api_key}'
        response = requests.get(URL)
        return response.json()
    
    def get_player_ranked_status(self) -> dict:
        """
        You can get the details about ranking status of a player
        """
        URL = f'{self.base_URL}/league/{self.api_version}/entries/by-summoner/{self.summoner_id}?api_key={self.api_key}'
        response = requests.get(URL)
        return response.json()
    
    def get_leagues_by_ranking(self, tier: str, division: str) -> list:
        """
        You can get a list of leagues, filtred by tir and tier and division
        Example: tire='DIAMOND', division'I'
        """
        URL = f'{self.base_URL}/league/{self.api_version}/entries/{tier}/{division}?api_key={self.api_key}'
        response = requests.get(URL)
        return response.json()
    
    def get_league_details_by_league_id(self, league_id:str) -> dict:
        """
        You can get details about a specific league
        """
        URL = f'{self.base_URL}/league/{self.api_version}/leagues/{league_id}?api_key={self.api_key}'
        response = requests.get(URL)
        return response.json()
    
    
def new_api(api_key: str, summoner_region='br1', summoner_name='Ilha Nublar'):
    """
    After import this module, you need call this function
    then you gona can call the methods of class TFTApi
    """
    return ConsumerRiotApi(api_key, summoner_region, summoner_name)
