from pprint import pprint

import requests

def get_most_intelligent_superhero():
    url = "https://www.superheroapi.com/api.php/2619421814940190/search/"
    superheros = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]

    for hero in superheros:
        hero_response = requests.get(url + hero['name'])
        hero['intelligence'] = int(hero_response.json()['results'][0]['powerstats']['intelligence'])

    # pprint((superheros))
    most_intelligent_hero = sorted(superheros, key=lambda hero: -hero['intelligence'])[0]['name']
    print(f'Самый умный супергерой - {most_intelligent_hero}')


if __name__ == '__main__':
    get_most_intelligent_superhero()


