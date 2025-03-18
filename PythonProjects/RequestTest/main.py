import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e7418f594959361cb4b4f989f892e749'
HEADER ={'Content-Type': 'application/json', 'trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "e.s.leonova@mrdoors.ru",
    "password": "Deniz2024"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бублик",
    "photo_id": 1
}


body_change = {
    "pokemon_id": "266854",
    "name": "Котик",
    "photo_id": 2
}


body_catch = {
    "pokemon_id": "266854"
}


'''response = requests.post(url =f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)
print(response.status_code)'''


'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json=body_confirmation) 
print(response_confirmation.text)
print(response_confirmation.status_code)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json=body_create)
print(response_create.text)
print(response_create.status_code)'''


'''message = response_create.json()['message']
print(message)'''

'''response_сhange = requests.put(url = f'{URL}/pokemons', headers = HEADER, json=body_change)
print(response_сhange.text)
print(response_сhange.status_code)
'''

response_сatch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json=body_change)
print(response_сatch.text)
print(response_сatch.status_code)
