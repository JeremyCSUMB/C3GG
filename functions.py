import requests
from key import APIKey
def requestSummonerData(summonerName):
    URL = "https://na.api.riotgames.com/api/lol/na/v1.4/summoner/by-name/" + summonerName + "?api_key=" + APIKey
    # print URL
    response = requests.get(URL)
    return response.json()

def requestRankedData(ID):
    URL = "https://na.api.riotgames.com/api/lol/na/v2.5/league/by-summoner/" + ID + "/entry?api_key=" + APIKey
    # print URL
    response = requests.get(URL)
    return response.json()


def requestSummonerStats(ID):
    URL = "https://na.api.riotgames.com/api/lol/na/v1.3/stats/by-summoner/" + ID + "/summary?season=SEASON2017&api_key=" + APIKey
    response = requests.get(URL)
    print URL
    return response.json()


def requestMasteryData(ID):
    URL = "https://na1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/" + ID + "?api_key=" + APIKey
    # print URL
    response = requests.get(URL)
    return response.json()

def requestChampionName():
    URL = "https://na1.api.riotgames.com/lol/static-data/v3/champions?api_key=" + APIKey
    # print URL
    response = requests.get(URL)
    return response.json()

def main():
    summonerName = (str)(raw_input('Type your Summoner Name here and DO NOT INCLUDE ANY SPACES: '))
    responseJSON  = requestSummonerData(summonerName)

    ID = responseJSON[summonerName]['id']
    ID = str(ID)
    print ID

    responseJSON2 = requestRankedData(ID)
    print responseJSON2[ID][0]['tier'], responseJSON2[ID][0]['entries'][0]['division']
    print "League Points:", responseJSON2[ID][0]['entries'][0]['leaguePoints']

    responseMASTERY = requestMasteryData(ID)
    for i in range(0,3):
        print "Champion ID #" + str(i + 1) + ":", responseMASTERY[i]['championId']
        print "Champion Level:", responseMASTERY[i]['championLevel']
    responseCHAMP = requestChampionName()
    print "Name:", responseCHAMP['data']['MonkeyKing']['name'] # This is just a name test! Doesn't mean anything!
if __name__ == "__main__":
    main()
