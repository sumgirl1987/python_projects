import pytest
from string_utils import StringUtils


@pytest.mark.positive
@pytest.mark.parametrize(
    'input,expected',
    [
        ('good bye', 'Good bye'),
        ('good bye, Alice', 'Good bye, alice'),
        ('bye', 'Bye'),
    ]
)
def test_pos_capitalize_strings(input, expected):
    print('\n')
    result = StringUtils().capitalize(input)
    print(f"Тестирую: '{input}'")
    print(f"Получил: '{result}'")
    print(f"Ожидал: '{expected}'")
    if result == expected:
        print("✅ Тест пройден!")
    else:
        print("❌ Исправь ошибку!!!")

    assert result == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    'input,expected',
    [
        ('.', '.'),                              # один символ (точка)
        ('123', '123'),                          # только цифры
        ('good bye\nAlice', 'Good bye\nalice'),  # переход на следующую строку
    ]
)
def test_neg_capitalize_strings(input, expected):
    print('\n')
    result = StringUtils().capitalize(input)
    print(f"Тестирую: '{input}'")
    print(f"Получил: '{result}'")
    print(f"Ожидал: '{expected}'")

    if result == expected:
        print("✅ Тест пройден!")
    else:
        print("❌ Исправь ошибку!!!")

    assert result == expected


@pytest.mark.positive
@pytest.mark.parametrize(
    'input,expected',
    [
        (' Good bye', 'Good bye'),
        ('  Good bye, Alice', 'Good bye, Alice'),
        (' Bye', 'Bye'),
    ]
)
def test_pos_trim_strings(input, expected):
    print('\n')
    result = StringUtils().trim(input)
    print(f"Тестирую: '{input}'")
    print(f"Получил: '{result}'")
    print(f"Ожидал: '{expected}'")
    if result == expected:
        print("✅ Тест пройден!")
    else:
        print("❌ Исправь ошибку!!!")

    assert result == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    'input,expected',
    [
        ('[]', '[]'),               # пустой список
        ('   ', ''),                # 3 пробела
        (' ', ''),                  # 1 пробел
    ]
)
def test_neg_trim_strings(input, expected):
    print('\n')
    result = StringUtils().trim(input)
    print(f"Тестирую: '{input}'")
    print(f"Получил: '{result}'")
    print(f"Ожидал: '{expected}'")
    if result == expected:
        print("✅ Тест пройден!")
    else:
        print("❌ Исправь ошибку!!!")

    assert result == expected


@pytest.mark.positive
@pytest.mark.parametrize(
    'input_string, input_symbol, expected',
    [
        ('Good bye', 'G', True),
        ('Good bye, Alice', ', Alice', True),
        ('Bye', 'e', True),
    ]
)
def test_pos_contains_symbols(input_string, input_symbol, expected):
    print('\n')
    result = StringUtils().contains(input_string, input_symbol)
    print(f"Тестирую: '{input_string}, символ '{input_symbol}'")
    print(f"Получил: '{result}'")
    print(f"Ожидал: '{expected}'")
    if result == expected:
        print("✅ Тест пройден!")
    else:
        print("❌ Исправь ошибку!!!")

    assert result == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    'input_string, input_symbol, expected',
    [
        ('Good bye', 'g', False),
        ('Good bye, Alice', '.', False),
        ('Bye', 'o', False),
    ]
)
def test_neg_contains_symbols(input_string, input_symbol, expected):
    print('\n')
    result = StringUtils().contains(input_string, input_symbol)
    print(f"Тестирую: '{input_string}, символ '{input_symbol}'")
    print(f"Получил: '{result}'")
    print(f"Ожидал: '{expected}'")
    if result == expected:
        print("✅ Тест пройден!")
    else:
        print("❌ Исправь ошибку!!!")

    assert result == expected


@pytest.mark.positive
@pytest.mark.parametrize(
    'input_string, input_symbol, expected',
    [
        ('Good bye', 'Good ', 'bye'),
        ('Good bye, Alice', ', Alice', 'Good bye'),
        ('Bye', 'e', 'By'),
    ]
)
def test_pos_delete_symbols(input_string, input_symbol, expected):
    print('\n')
    result = StringUtils().delete_symbol(input_string, input_symbol)
    print(f"Тестирую: '{input_string}, символ '{input_symbol}'")
    print(f"Получил: '{result}'")
    print(f"Ожидал: '{expected}'")
    if result == expected:
        print("✅ Тест пройден!")
    else:
        print("❌ Исправь ошибку!!!")

    assert result == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    'input_string, input_symbol, expected',
    [
        ('Good bye', 'g', 'Good bye'),
        ('', 'a', ''),
        ('Bye', '', 'Bye'),
    ]
)
def test_neg_delete_symbols(input_string, input_symbol, expected):
    print('\n')
    result = StringUtils().delete_symbol(input_string, input_symbol)
    print(f"Тестирую: '{input_string}, символ '{input_symbol}'")
    print(f"Получил: '{result}'")
    print(f"Ожидал: '{expected}'")
    if result == expected:
        print("✅ Тест пройден!")
    else:
        print("❌ Исправь ошибку!!!")

    assert result == expected
