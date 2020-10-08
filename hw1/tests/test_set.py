"""
Файл для тестирования типа set
"""
import pytest


class TestSetMethods:
    def test_pop(self):
        """
        Проверка метода pop
        """
        zero = {}
        with pytest.raises(TypeError):
            assert zero.pop()

    def test_difference(self):
        """
        Проверка метода difference
        """
        first_set = {1, 2, 3}
        second_set = {1, 2}
        assert first_set.difference(second_set) == {3}

    def test_copy(self):
        """
        Проверка метода copy
        """
        sample = {'a', 'b', 'c'}
        new_sample = sample.copy()
        assert new_sample == sample


def test_with_fixture_set(def_set):
    """
    Проверка на совпадение множеств
    :param def_set: fixture, return set
    """
    print(def_set)
    assert def_set == {'a', 'b', 'c'}


@pytest.mark.parametrize('num1, num2', [({1, 2}, {3, 4}), ({5, 6}, {7, 8}), ({0}, {0})])
def test_limit(num1, num2):
    """
    Проверка на равную длину множеств num1 и num2
    :param num1: set with ints
    :param num2: set with ints
    """
    assert len(num1) == len(num2)
