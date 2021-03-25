"""
Тестирование страницы регистрации
"""
import allure
import pytest

from clients.mysql_orm_client.builder import MysqlOrmBuilder
from ui_tests.base import BaseCase
from ui.pages.start_page import StartPage


@allure.feature('Тестирование страницы регистрации')
class TestRegistrationForm(BaseCase):
    """
    В некторых тестах используется фикстура fake_data (библиотека faker),
    которая возвращает словарь со случайным username, password и email.
    """

    @pytest.fixture(scope='function', autouse=True)
    def reg_page(self, driver):
        """
        Переход на страницу регистрации.
        """
        StartPage(driver).go_to_registration_page()

    @allure.title('Тест нахождения на странице')
    def test_title_check_registration_page(self):
        """
        Тест проверяет, что сейчас открыта страница регистрации.
        Проверяет наличие строки в исходном коде страницы.
        """
        with allure.step('Проверка страницы'):
            assert 'Registration' in self.driver.page_source

    @allure.title('Тест валидации полей')
    def test_validation_check_registration_page(self):
        """
        Тест проверяет наличие валидации у полей username, password,
        email, confirm и term.
        Наличие валидации подтверждается тегом required.
        """
        with allure.step('Проверка валидации'):
            self.registration_page.check_valid_registration_page()

    @allure.title('Негативный тест на длину username')
    def test_incorrect_username_length(self, fake_data):
        """
        Негативный тест на регистрацию.
        Проверяется невозможность зарегистрировать пользователя с коротким username.
        Ожидаемая ошибка: 'Incorrect username length'.
        """
        with allure.step('Попытка регистрации'):
            self.registration_page.do_registration(username='test',
                                                   email=fake_data['email'],
                                                   password=fake_data['password'],
                                                   confirm=fake_data['password'])
        with allure.step('Поиск сообщения об ошибке'):
            self.registration_page.find(self.registration_page.locators.USERNAME_ERROR, 2)

    @allure.title('Негативный тест на длину email')
    def test_invalid_email_length(self, fake_data):
        """
        Негативный тест на регистрацию.
        Проверяется невозможность зарегистрировать пользователя с коротким email.
        Ожидаемая ошибка: 'Incorrect email length'.
        """
        with allure.step('Попытка регистрации'):
            self.registration_page.do_registration(username=fake_data['username'],
                                                   email='test',
                                                   password=fake_data['password'],
                                                   confirm=fake_data['password'])
        with allure.step('Поиск сообщения об ошибке'):
            self.registration_page.find(self.registration_page.locators.EMAIL_ERROR_LENGTH, 2)

    @allure.title('Негативный тест на некорректный email')
    def test_incorrect_email(self, fake_data):
        """
        Негативный тест на регистрацию.
        Проверяется невозможность зарегистрировать пользователя с неправильным email.
        Ожидаемая ошибка: 'Invalid email address'.
        """
        with allure.step('Попытка регистрации'):
            self.registration_page.do_registration(username=fake_data['username'],
                                                   email='incorrect_email',
                                                   password=fake_data['password'],
                                                   confirm=fake_data['password'])
        with allure.step('Поиск сообщения об ошибке'):
            self.registration_page.find(self.registration_page.locators.EMAIL_ERROR_INVALID, 2)

    @allure.title('Негативный тест на различающиеся пароли')
    def test_negative_password_confirm(self, fake_data):
        """
        Негативный тест на регистрацию.
        Проверяется невозможность зарегистрировать пользователя с неверным confirm.
        Ожидаемая ошибка: 'Passwords must match'.
        """
        with allure.step('Попытка регистрации'):
            self.registration_page.do_registration(username=fake_data['username'],
                                                   email=fake_data['email'],
                                                   password=fake_data['password'],
                                                   confirm=fake_data['password'][::-1])
        with allure.step('Поиск сообщения об ошибке'):
            self.registration_page.find(self.registration_page.locators.PASSWORD_ERROR, 2)

    @allure.title('Негативный тест на все поля')
    def test_all_incorrect(self):
        """
        Негативный тест на регистрацию.
        Случай, когда все поля заполнены неверно.
        Ожидаемый результат: ошибка с текстом.
        """
        with allure.step('Попытка регистрации'):
            self.registration_page.do_registration(username='test',
                                                   email='incorrect',
                                                   password='000',
                                                   confirm='0')
        with allure.step('Поиск сообщения об ошибке'):
            self.registration_page.find(self.registration_page.locators.SOMETHING_MESSAGE, 2)

    @allure.title('Тест перехода на страницу авторизации')
    def test_go_back_login(self):
        """
        Тест переходит на страницу авторизации.
        Проверяет наличие строки в исходном коде страницы.
        """
        with allure.step('Переход на страницу авторизации'):
            self.registration_page.click(self.registration_page.locators.GO_BACK_LOGIN_BUTTON, 2)
            assert 'Welcome to the TEST SERVER' in self.driver.page_source

    @allure.title('Позитивный тест на регистрацию')
    def test_correct_registration(self, fake_data):
        """
        Позитивный тест на регистрацию.
        Проверка корректной регистрации.
        В случае успешной регистрации, осуществляется переход в ЛК пользователя:
        наличие 'Logged as' на странице ЛК.
        Далее проверяется при помощи orm наличие пользователя в БД.
        """
        with allure.step('Регистрация'):
            self.registration_page.do_registration(username=fake_data['username'],
                                                   email=fake_data['email'],
                                                   password=fake_data['password'],
                                                   confirm=fake_data['password'])
        with allure.step('Проверка регистрации'):
            self.cabinet_page.find(self.cabinet_page.locators.LOGGED_AS, 2)
        with allure.step('Проверка БД'):
            user = MysqlOrmBuilder().select_from_table(fake_data['username'])
            assert user.username == fake_data['username']
            assert user.access == 1
