import requests

base_url = 'https://yougile.com/api-v2'
key = 'zequ8LDdJ6u5QV6+IvnYxMgH1KnPbOKI4LuXQCDgl7pz-dGXUVmzQYI9WZCSTqzK'
user_id = '7cf99a30-6c7a-4436-8d43-75999bd10988'

# Список ID проектов для удаления
project_ids = [
    '2f969637-4de2-4064-bd2b-4e4e321181c5',
    '0fd080dc-d14e-4781-8f8e-1a12090045aa',
    '3e0801dc-fdb8-4b42-8609-5e5050007e7d'
    # Добавьте сюда все ID, которые нужно удалить
]


def test_update_company_positive():
    """Позитивный тест: успешное обновление (удаление) нескольких проектов"""
    headers = {'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}
    data_body = {
        'deleted': True,
        'users': {user_id: 'worker'}
    }

    for project_id in project_ids:
        response = requests.put(f'{base_url}/projects/{project_id}',
                                json=data_body, headers=headers)

        if response.status_code == 200:
            print(f"✅ Проект {project_id} успешно удален")
        else:
            print(f"❌ Ошибка при удалении {project_id}: {response.status_code}")
            print(f"   Ответ: {response.json()}")

        assert response.status_code == 200, f"Ошибка при удалении {project_id}"
