"""
Файл для тестирования типа int
"""
import random


from math import sqrt


import pytest


class TestIntMethods:
    def test_real_part(self):
        """
        Проверка действительной части комплексного числа
        """
        number1 = 5 + 4j
        assert number1.real == 5

    def test_image_part(self):
        """
        Проверяет, что мнимая часть положительна
        """
        number2 = -10 + 15j
        assert number2.imag > 0

    def test_bit_length(self):
        """
        Проверяет возникновение ошибки при определенной битовой длине числа
        """
        number3 = random.randint(0, 127)
        with pytest.raises(AssertionError):
            assert number3.bit_length() > 7


def test_with_fixture_int(upload_number):
    """
    Проверка на четность
    :param upload_number:
    """
    print(upload_number)
    assert upload_number % 2 == 0


@pytest.mark.parametrize('cube', [i**3 for i in range(-5, 0)])
def test_negative_root(cube):
    """
    Обработка отрицательных квадратных корней
    :param cube: list of cube negative numbers
    """
    with pytest.raises(ValueError):
        assert sqrt(cube)
