"""
Тестирование страницы авторизации
"""
import allure
import pytest

from clients.mysql_orm_client.builder import MysqlOrmBuilder
from ui_tests.base import BaseCase


@allure.feature('Тестирование стартовой страницы')
class TestAutorizationForm(BaseCase):
    """
    В некторых тестах используется фикстура fake_data (библиотека faker),
    которая возвращает словарь со случайным username, password и email.
    """

    @allure.title('Тест нахождения на странице')
    def test_title_check_start_page(self):
        """
        Тест проверяет, что сейчас открыта страница авторизации.
        Проверяет наличие строки в исходном коде страницы.
        """
        with allure.step('Проверка страницы'):
            assert 'Welcome to the TEST SERVER' in self.driver.page_source

    @allure.title('Тест валидации полей')
    def test_validation_check_start_page(self):
        """
        Тест проверяет наличие валидации у полей username и password.
        Наличие валидации подтверждается тегом 'required' у полей.
        """
        with allure.step('Проверка валидации'):
            self.start_page.check_valid_start_page()

    @allure.title('Негативный тест на авторизацию')
    def test_negative_autorization_start_page(self, fake_data):
        """
        Негативный тест на авторизацию.
        Подтверждением неправильной авторизации является сообщение
        'Invalid username or password'.
        """
        with allure.step('Авторизация незарегистрированного пользователя'):
            self.start_page.autorization(user=fake_data['username'],
                                         password=fake_data['password'])
        with allure.step('Поиск сообщения об ошибке'):
            self.start_page.find(self.start_page.locators.ERROR_MESSAGE, 2)

    @allure.title('Позитивный тест на авторизацию')
    def test_correct_login(self, fake_data):
        """
        Позитивный тест на авторизацию.
        При помощи orm пользователь добавляется в БД.
        Происходит попытка авторизации.
        Подтверждением входа является строка 'Logged as' на странице ЛК поьзователя.
        """
        with allure.step('Добавление пользователя через orm'):
            MysqlOrmBuilder().add_user(username=fake_data['username'],
                                       email=fake_data['email'],
                                       password=fake_data['password'])
        with allure.step('Авторизация добавленного пользователя'):
            self.start_page.autorization(user=fake_data['username'],
                                         password=fake_data['password'])
        with allure.step('Проверка успешной авторизации'):
            self.cabinet_page.find(self.cabinet_page.locators.LOGGED_AS, 2)

    @allure.title('Тест перехода к регистрации')
    def test_go_to_registration_test(self):
        """
        Тест переходит на страницу регистрации.
        Проверяет наличие строки в исходном коде страницы.
        """
        with allure.step('Переход на страницу регистрации'):
            self.start_page.go_to_registration_page()
            assert 'Registration' in self.driver.page_source

    @allure.title('Тест попытки входа заблокированного пользователя')
    def test_autorization_block_user(self, fake_data):
        """
        Тест на авторизацию заблокированного пользователя.
        При помощи orm добавляется заблокированный пользователь.
        Ожидается текстовая ошибка.
        """
        with allure.step('Создание через orm заблокированного пользователя'):
            MysqlOrmBuilder().add_user(username=fake_data['username'],
                                       email=fake_data['email'],
                                       password=fake_data['password'],
                                       access=0)
        with allure.step('Попытка авторизации'):
            self.start_page.autorization(user=fake_data['username'],
                                         password=fake_data['password'])
        with allure.step('Поиск сообщения об ошибке'):
            self.start_page.find(self.start_page.locators.BLOCK_MESSAGE, 2)
