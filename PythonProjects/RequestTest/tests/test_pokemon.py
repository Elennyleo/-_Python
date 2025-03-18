import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e7418f594959361cb4b4f989f892e749'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '34261'

#проверка статус кода
def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200     


#проверка имени
def test_trainer_name():
    response_get_name = requests.get(url = f'{URL}/me', headers=HEADER)
    assert response_get_name.json()["data"][0]["trainer_name"] == "Leonardo"