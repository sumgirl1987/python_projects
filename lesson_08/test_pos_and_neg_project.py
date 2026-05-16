import requests

base_url = 'https://yougile.com/api-v2'
key = ''

# Глобальная переменная для хранения ID
saved_project_id = None


def test_create_project_positive():
    global saved_project_id

    headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json'
    }
    new_company = {
        'title': 'Калейдоскоп',
        'users': {'7cf99a30-6c7a-4436-8d43-75999bd10988': 'worker'}
    }
    response = requests.post(
        f'{base_url}/projects', json=new_company, headers=headers)

    assert response.status_code == 201
    saved_project_id = response.json()['id']
    print(f"✅ Создан проект с ID: {saved_project_id}")


def test_update_project_positive():
    headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json'
    }
    data_body = {
        'title': 'Радуга',
        'users': {'7cf99a30-6c7a-4436-8d43-75999bd10988': 'worker'}
    }
    response = requests.put(f'{base_url}/projects/{saved_project_id}',
                            json=data_body, headers=headers)
    assert response.status_code == 200
    print(f"✅ Проект {saved_project_id} успешно обновлен на 'Радуга'")


def test_get_project_by_id_positive():
    headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json'
    }
    response = requests.get(
        f'{base_url}/projects/{saved_project_id}', headers=headers)

    assert response.status_code == 200, (
        f"GET: ожидался 200, получен {response.status_code}"
    )
    print("✅ Позитивный тест пройден: GET_BY_ID работает")


def test_create_company_negative_without_auth():
    """❌ Негативный тест: создание проекта без авторизации"""
    new_company = {
        'title': 'Калейдоскоп_1',
        'users': {
            '7cf99a30-6c7a-4436-8d43-75999bd10988': 'worker',
        }
    }
    # Отправляем запрос БЕЗ заголовка Authorization
    response = requests.post(f'{base_url}/projects', json=new_company)

    # Проверяем, что вернулась ошибка 401
    assert response.status_code == 401, \
        f"Ожидался 401, получен {response.status_code}"
    error_data = response.json()
    print(f"Ожидаемая ошибка: {error_data}")
    print("✅ Негативный тест пройден: API вернул 401 без авторизации")


def test_update_company_negative_invalid_project_id():
    """❌ Негативный тест: несуществующий ID проекта"""
    invalid_id = '66666666-5555-4444-3333-222222222222'
    headers = {
        'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}
    data_body = {
        'title': 'Радуга_1',
        'users': {
            '7cf99a30-6c7a-4436-8d43-75999bd10988': 'worker',
        }
    }
    response = requests.put(f'{base_url}/projects/{invalid_id}',
                            json=data_body, headers=headers)

    # Проверяем, что вернулась ошибка 404
    assert response.status_code == 404, \
        f"Ожидался 404, получен {response.status_code}"
    error_data = response.json()
    print(f"Ожидаемая ошибка: {error_data}")
    print("✅ Негативный тест пройден: API вернул 404. Неверный ID")


def test_get_project_by_id_negative_wrong_method():
    """❌ Негативный тест: PUT не должен работать для получения проекта"""
    headers = {'Authorization': f'Bearer {key}'}
    response = requests.put(
        f'{base_url}/projects/{saved_project_id}', headers=headers)

    # Ожидаем ошибку, но API возвращает 200 - это БАГ!
    expected_status = 405
    actual_status = response.status_code

    print(f"PUT запрос вернул: {actual_status}")
    print(f"Ответ: {response.json()}")

    assert actual_status == expected_status, (
        f"❌ БАГ API! PUT запрос на /projects/{saved_project_id}\n"
        f"Должен вернуть {expected_status} (Method Not Allowed),\n"
        f"но вернул {actual_status} (OK)\n"
        f"Ответ: {response.json()}"
    )
