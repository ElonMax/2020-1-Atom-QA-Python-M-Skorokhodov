"""
Файл с фикстурами
"""
import pytest


@pytest.fixture()
def def_list():
    """
    :return: list of numbers
    """
    print('generating list')
    yield [3, 2, 2]
    print('generating done')


@pytest.fixture()
def def_set():
    """
    :return: set of char
    """
    print('generating set')
    yield {'a', 'b', 'c'}
    print('generating done')


@pytest.fixture()
def give_salary():
    """
    :return: dict of salary
    """
    print('give salary')
    yield {'Sasha': 100, 'Maksim': 1000}
    print('salary is given')


@pytest.fixture()
def get_sentence():
    """
    :return: some sentence
    """
    print('get text')
    yield 'London is the capital of Great Britain'
    print('get done')


@pytest.fixture()
def upload_number():
    """
    :return: some number
    """
    print('loading number')
    yield 215478542
    print('successful load')
