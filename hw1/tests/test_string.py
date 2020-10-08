"""
Файл для тестирования типа string
"""
import pytest


class TestStrMethods:
    def test_upper(self):
        """
        Проверка метода upper
        """
        text1 = 'hello, world!'
        assert text1.upper() == 'HELLO, WORLD!'

    def test_number(self):
        """
        Проверка является ли строка числом
        """
        number = '777'
        assert number.isdigit()

    def test_strip(self):
        """
        Проверка работы strip
        """
        text2 = ' test '
        assert text2.strip(' ') == 'test'


def test_with_fixture_string(get_sentence):
    """
    Проверяет, что строка не удовлетворяет заданной длине
    :param get_sentence: return some sentence
    """
    print(get_sentence)
    with pytest.raises(AssertionError):
        assert len(get_sentence) == 50


@pytest.mark.parametrize('words', ['My', 'name', 'is', 'Maksim'])
def test_match(words):
    """
    Проверяет наличие определенных слов в строке
    :param words: list of string
    """
    assert words in 'My name is Maksim! I am from Russia.'
