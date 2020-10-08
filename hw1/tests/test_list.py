"""
Файл для тестирования типа list
"""
import random


import pytest


class TestListSimple:
    def test_index(self):
        """
        Проверяет совпадение элемента списка с заданным числом
        """
        numbers = [0, 1, 2, 3]
        assert numbers[1] == 1

    def test_match(self):
        """
        Проверяет, что список из случайных чисел не превышает заданных пределов
        """
        set_length = 3
        random_list = [random.randint(0, 100) for i in range(set_length)]
        sample_list = [101 for i in range(set_length)]
        assert random_list < sample_list


def test_exception():
    """
    Проверяет возникновение ошибки при суммировании элементов списка с разными типами
    """
    number_list = [1, 2, 3]
    name_list = ['Pasha', 'Sasha', 'Masha']
    with pytest.raises(TypeError):
        assert number_list[0] + name_list[0]


def test_with_fixture_list(def_list):
    """
    Проверяет работу метода count
    :param def_list: fixture, return list
    """
    print(def_list)
    assert def_list.count(2) == 2


@pytest.mark.parametrize('num', list(range(5)))
def test_find_number(num):
    """
    Проверяет наличие числа из num в заданном списке
    :param num: integer from 0 to 5
    """
    assert num in [0, 1, 2, 3, 4]
