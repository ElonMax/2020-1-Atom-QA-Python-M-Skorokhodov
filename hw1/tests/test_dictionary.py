"""
Файл для тестирования типа dict
"""
import random


import pytest


class TestDictMethods:
    def test_values(self):
        """
        Проверка на наличие значений у ключей
        """
        dict_work = {'miner': '2000$', 'policeman': '2500$', 'doctor': '5000$'}
        assert dict_work.values() != []

    def test_keys(self):
        """
        Проверка на содержание определенных ключей
        """
        dict_names = {'Smith': 'Jhon', 'Black': 'David', 'Snow': 'Rick'}
        assert 'Smith' and 'Black' in dict_names.keys()

    def test_clear(self):
        """
        Проверка метода clear
        """
        dict_num = {1: 'a', 2: 'b', 3: 'c'}
        dict_num.clear()
        assert dict_num == {}


def test_with_fixture_dict(give_salary):
    """
    Проверка, что значения словаря удовлетворяют условиям
    :param give_salary: dict with names and salary, keys: 'Sasha', 'Maksim'
    """
    print(give_salary)
    assert give_salary['Maksim'] > 999


@pytest.mark.parametrize('iter_keys', list(range(10)))
def test_type(iter_keys):
    """
    Проверка ошибки AssertionError
    :param iter_keys: list of int from 0 to 9
    """
    dicts = {i: random.randint(0, 10) for i in range(10)}
    with pytest.raises(AssertionError):
        assert dicts[iter_keys] < 0
