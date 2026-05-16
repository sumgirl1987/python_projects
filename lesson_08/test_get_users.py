import requests
import json


base_url = 'https://yougile.com/api-v2/'
key = 'zequ8LDdJ6u5QV6+IvnYxMgH1KnPbOKI4LuXQCDgl7pz-dGXUVmzQYI9WZCSTqzK'
headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json'
}


def test_get_type_of_response():
    type_response = requests.get(f'{base_url}/users', headers=headers)
    print(type_response.text)  # Посмотреть, что приходит
    data = type_response.json()  # Получаем словарь из JSON
    print(data.keys())
    print(json.dumps(data, indent=2, ensure_ascii=False))


def test_get_users():
    headers = {'Authorization': f'Bearer {key}'}
    response = requests.get(f'{base_url}/users', headers=headers)
    data = response.json()
    users = data['content']

    for user in users:
        print(f"ID: {user['id']}, Email: {user['email']}")
