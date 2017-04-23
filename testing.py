import requests

APIKey = 'RGAPI-E0199471-1836-467C-B66C-940F0A647BC0'

def requestSummonerData(summonerName):
    URL = "https://na.api.riotgames.com/api/lol/na/v1.4/summoner/by-name/" + summonerName + "?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()

def requestRankedData(ID):
    URL = "https://na.api.riotgames.com/api/lol/na/v2.5/league/by-summoner/" + ID + "/entry?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()

def requestSummonerStats(ID):
    URL = "https://na.api.riotgames.com/api/lol/na/v1.3/stats/by-summoner/" + ID + "/summary?season=SEASON2017&api_key=" + APIKey
    response = requests.get(URL)
    return response.json()


def requestMasteryData(ID):
    URL = "https://na1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/" + ID + "?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()

def requestChampionName():
    URL = "https://na1.api.riotgames.com/lol/static-data/v3/champions?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()
