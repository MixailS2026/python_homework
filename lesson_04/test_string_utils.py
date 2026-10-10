import pytest
from string_utils import StringUtils


string_utils = StringUtils()

# --- Позитивные тесты ---

# Обычная строка, первая буква становится заглавной.


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Удаление пробелов в начале
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("   hello world", "hello world"),
    ("   python", "python"),
])
def test_trim_spaces_at_start(input_str, expected):
    assert string_utils.trim(input_str) == expected


# Cимвол найден в строке
@pytest.mark.positive
@pytest.mark.parametrize(
    "string, symbol",
    [
        ("SkyPro", "S"),
        ("Hello World", "W"),
        ("Python", "t"),
    ],
)
def test_contains_true(string, symbol):
    assert string_utils.contains(string, symbol) is True

# --- Негативные тесты ---


# Числа как строка, Пустая строка, Пробел
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Cимвол не найден, должен вернуть False
@pytest.mark.negative
@pytest.mark.parametrize(
    "string, symbol",
    [
        ("SkyPro", "U"),
        ("Hello World", "A"),
        ("Python", "w"),
    ],
)
def test_contains_false(string, symbol):
    assert string_utils.contains(string, symbol) is False


# поиск пустой строки
@pytest.mark.negative
def test_contains_empty_symbol():
    assert string_utils.contains("abc", "") is True
