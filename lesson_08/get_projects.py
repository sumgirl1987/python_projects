import requests

base_url = 'https://yougile.com/api-v2/'
key = ''


def get_project_by_id_positive():
    headers = {'Authorization': f'Bearer {key}'}
    response = requests.get(f'{base_url}projects', headers=headers)

    print(f"Статус: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print(f"Тип ответа: {type(data)}")

        # Проверяем структуру ответа
        if isinstance(data, dict) and 'content' in data:
            projects = data['content']
        elif isinstance(data, list):
            projects = data
        else:
            print("Неизвестная структура:", data.keys() if isinstance(data, dict) else "список?")
            projects = []

        print(f"\nНайдено проектов: {len(projects)}")
        print("-" * 40)

        for project in projects:
            print(f"ID: {project.get('id')}")
            print(f"Название: {project.get('title')}")
            print(f"Удален: {project.get('deleted', False)}")
            print("-" * 40)
    else:
        print(f"Ошибка: {response.status_code}")
        print(response.json())


# 👇 ВЫЗЫВАЕМ ФУНКЦИЮ
get_project_by_id_positive()
