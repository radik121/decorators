import requests
from Decorators.logger import log_decorator


@log_decorator('PycharmProjects/logs', 'log.txt')
def most_intelligence_hero(hero_list):
    intelligence_hero = 0
    most_intelligence = None
    for i in hero_list:
        url = "https://superheroapi.com/api/2619421814940190/search/" + i
        responce = requests.get(url)
        result = responce.json()['results']
        if int(result[0]['powerstats']['intelligence']) > intelligence_hero:
            intelligence_hero = int(result[0]['powerstats']['intelligence'])
            most_intelligence = result[0]['name']
    return most_intelligence


if __name__ == '__main__':
    most_intelligence_hero(['Hulk', 'Captain America', 'Thanos'])
