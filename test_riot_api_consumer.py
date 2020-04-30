from riot_api_consumer import *
import os

"""
x
@pytest.fixture()
def retorna_api_key_riot_para_consulta():
    with open('riot_api_key.txt', 'r') as key:
        return key.read()
""" 
  
    
@pytest.fixture()
def retorna_api_key_riot_para_consulta():
    return os.environ.get('RIOT_API_KEY')

    
@pytest.fixture()
def summoner_Ieko():
    """
    Summoner Name: Ieko
    Region: Brazil
    """
    return {
        'summoner_name': 'Ieko',
        'summoner_region': 'br1',
        }


@pytest.fixture()
def summoner_ilha_nublar():
    """
    Summoner Name: Ilha Nubllar
    Region: Brazil
    """
    return {
        'summoner_name': 'Ilha Nublar',
        'summoner_region': 'br1',
        'tft_get_matches_by_summoner': [
            'BR1_1882323432',
            'BR1_1775035230',
            'BR1_1770334549',
            'BR1_1770273342',
            'BR1_1769520122'
        ]
    }
    

@pytest.fixture()
def league_id_list():
    """
    List with League IDs
    """
    return [
        'd55538c0-4f00-4eb6-a8ca-8ffe98517751',
        '2dfb0f02-ef1c-4552-ab16-9193748646f5',
        '881301bb-d573-4e3a-87cf-db652f33bc91',
    ]


def test_init_session(retorna_api_key_riot_para_consulta, summoner_ilha_nublar):
    """
    Testing init session
    Summoner Name: lha Nublar profile.
    """
    api_key = retorna_api_key_riot_para_consulta
    ilha_nublar = summoner_ilha_nublar
    api = new_api(api_key, ilha_nublar['summoner_region'],
                            ilha_nublar['summoner_name']) 
    assert api.api_session['id'] == '5AtW4neaL009Zy-jUjHLbal7PcsGqQvSpB26-S_hfTTi'
    
    
def test_get_summoner_profile(retorna_api_key_riot_para_consulta, summoner_ilha_nublar):
    """
    Testing the consume of /tft/summoner/v1/summoners/by-account/{encryptedAccountId}
    Summoner Name: Ilha Nublar
    """
    api_key = retorna_api_key_riot_para_consulta
    ilha_nublar = summoner_ilha_nublar
    api = new_api(api_key, ilha_nublar['summoner_region'], 
                           ilha_nublar['summoner_name'])
    tft = api.TFT.get_summoner_profile()
    assert tft['id'] =='5AtW4neaL009Zy-jUjHLbal7PcsGqQvSpB26-S_hfTTi'
    
    
def test_get_matches_by_summoner(retorna_api_key_riot_para_consulta, summoner_ilha_nublar):
    """
    Testing the consume of /tft/match/v1/matches/by-puuid/{puuid}/ids
    Summoner Name: Ilha Nublar
    """
    api_key = retorna_api_key_riot_para_consulta
    ilha_nublar = summoner_ilha_nublar
    api = new_api(api_key, ilha_nublar['summoner_region'],
                           ilha_nublar['summoner_name'])
    tft = api.TFT.get_matches_by_summoner()
    for match in ilha_nublar['tft_get_matches_by_summoner']:
        assert match in tft
        
    
def test_get_match_by_match_id_metadata_participants(retorna_api_key_riot_para_consulta, summoner_ilha_nublar):
    """
    Testing the consume of /tft/match/v1/matches/{matchId}
    Summoner Name: Ilha Nublar
    """
    api_key = retorna_api_key_riot_para_consulta
    ilha_nublar = summoner_ilha_nublar
    api = new_api(api_key, ilha_nublar['summoner_region'],
                           ilha_nublar['summoner_name'])
    tft = api.TFT.get_match_by_match_id(ilha_nublar['tft_get_matches_by_summoner'][0])
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
    
    
def test_get_match_by_match_id_info_game_datetime(retorna_api_key_riot_para_consulta, summoner_ilha_nublar):
    """
    Testing the consume of /tft/match/v1/matches/{matchId}
    Summoner Name: Ilha Nublar
    """
    api_key = retorna_api_key_riot_para_consulta
    ilha_nublar = summoner_ilha_nublar
    api = new_api(api_key, ilha_nublar['summoner_region'],
                           ilha_nublar['summoner_name'])
    tft = api.TFT.get_match_by_match_id(ilha_nublar['tft_get_matches_by_summoner'][0])
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
    
    
def test_get_player_ranked_status(retorna_api_key_riot_para_consulta, summoner_Ieko):
    """
    Testing the consume of /tft/league/v1/entries/by-summoner/{encryptedSummonerId}
    Summoner Name: Ieko
    Region: Brazil
    """
    api_key = retorna_api_key_riot_para_consulta
    leko = summoner_Ieko
    api = new_api(api_key, leko['summoner_region'],
                        leko['summoner_name'])
    tft = api.TFT.get_player_ranked_status()
    assert tft[0]['queueType'] == 'RANKED_TFT'
    assert tft[0]['summonerId'] == 'bbYwQtET_GWwodvvxU3i5DEEXsdF3ujtDWfmMTldpfKG3g'
    

def test_get_leagues_by_ranking(retorna_api_key_riot_para_consulta):
    """
    Testing the consume of /tft/league/v1/entries/{tier}/{division}
    In this case, you need inform tier:
        DIAMOND, PLATINUM, GOLD, SILVER, BRONZE or IRON
    and division:
        I, II, III, IV
    """
    api_key = retorna_api_key_riot_para_consulta
    api = new_api(api_key)
    tft = api.TFT.get_leagues_by_ranking('DIAMOND', 'I')
    assert tft[0]['queueType'] == 'RANKED_TFT'
    assert tft[0]['tier'] == 'DIAMOND'
    assert tft[0]['rank'] == 'I'
    

def test_get_league_details_by_league_id(retorna_api_key_riot_para_consulta, league_id_list):
    """
    Testing the consume of /tft/league/v1/leagues/{leagueId}
    """
    api_key = retorna_api_key_riot_para_consulta
    api = new_api(api_key)
    league_list = league_id_list
    for league_id in league_list:
        tft = api.TFT.get_league_details_by_league_id(league_id)
        assert tft['leagueId'] == league_id