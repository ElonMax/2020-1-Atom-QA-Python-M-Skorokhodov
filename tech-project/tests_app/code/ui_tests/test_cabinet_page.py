"""
Тестирование ЛК пользователя
"""
import time

import allure
import requests
import pytest
from selenium.webdriver.common.by import By

from clients.mysql_orm_client.builder import MysqlOrmBuilder
from ui_tests.base import BaseCase
from ui.pages.start_page import StartPage


@allure.feature('Тестирование страницы пользователя')
class TestCabinetPage(BaseCase):

    @pytest.fixture(scope='function', autouse=True)
    def autorization(self, driver, fake_data):
        """
        Фикстура на авторизацию пользователя.
        При помощи фикстуры fake_data и orm в БД добавляется случайный пользователь.
        Происходит авторизация.
        """
        MysqlOrmBuilder().add_user(username=fake_data['username'],
                                   email=fake_data['email'],
                                   password=fake_data['password'])
        StartPage(driver).autorization(user=fake_data['username'],
                                       password=fake_data['password'])

        self.username = fake_data['username']

    @allure.title('Тест нахождения на странице')
    def test_logged_check(self):
        """
        Тест проверяет, что сейчас открыт ЛК пользователя.
        Проверяет наличие строки в исходном коде страницы.
        """
        with allure.step('Проверка страницы'):
            assert 'Logged as' in self.driver.page_source

    @allure.title('Тест на выход пользователя')
    def test_logout(self):
        """
        Тест кнопки 'Logout'.
        После выхода из ЛК проверяет наличие строки в исходном коде страницы.
        """
        with allure.step('Нажатие на кнопку logout'):
            self.cabinet_page.click(self.cabinet_page.locators.LOGOUT_BUTTON, 2)
        with allure.step('Проверка страницы'):
            assert 'Welcome to the TEST SERVER' in self.driver.page_source

    @allure.title('Тест перехода по бренду приложения')
    def test_brand_click(self):
        """
        Тест кнопки бренда приложения.
        Кнопка возвращает главную страницу ЛК пользователя.
        """
        with allure.step('Нажатие на кнопку бренда'):
            self.cabinet_page.click(self.cabinet_page.locators.CABINET_PAGE_BUTTON, 2)
        with allure.step('Проверка страницы'):
            self.cabinet_page.find(self.cabinet_page.locators.LOGGED_AS, 2)

    @allure.title('Тест перехода по home')
    def test_home_click(self):
        """
        Тест кнопки 'Home'.
        Кнопка возвращает главную страницу ЛК пользователя
        """
        with allure.step('Нажатие на кнопку home'):
            self.cabinet_page.click(self.cabinet_page.locators.HOME_BUTTON, 2)
        with allure.step('Проверка страницы'):
            self.cabinet_page.find(self.cabinet_page.locators.LOGGED_AS, 2)

    @allure.title('Тест перехода на python.org')
    def test_python_click(self):
        """
        Тест перехода на сайт 'python.org'.
        После нажатия на кнопку 'Python' открывается новая вкладка с данным ресурсом.
        Проверяется наличие строки в title сайта.
        """
        with allure.step('Нажатие на кнопку python'):
            self.cabinet_page.go_outside_main(self.cabinet_page.locators.PYTHON_BUTTON)
        with allure.step('Проверка страницы'):
            assert 'Welcome to Python.org' in self.driver.title

    @allure.title('Тест перехода на History python')
    def test_history(self):
        """
        Тест перехода на сайт с историей python.
        После нажатия на кнопку 'History Python' открывается новая вкладка с данным ресурсом.
        Проверяется наличие строки в title сайта.
        """
        with allure.step('Нажатие на кнопку history python'):
            self.cabinet_page.go_outside_hide(self.cabinet_page.locators.PYTHON_BUTTON,
                                              self.cabinet_page.locators.PYTHON_HISTORY_BUTTON)
        with allure.step('Проверка страницы'):
            assert 'History of Python - Wikipedia' in self.driver.title

    @allure.title('Тест перехода на Flask')
    def test_flask(self):
        """
        Тест перехода на сайт с документацией Flask.
        После нажатия на кнопку 'About Flask' открывается новая вкладка с данным ресурсом.
        Проверяется наличие строки в title сайта.
        """
        with allure.step('Нажатие на кнопку about flask'):
            self.cabinet_page.go_outside_hide(self.cabinet_page.locators.PYTHON_BUTTON,
                                              self.cabinet_page.locators.ABOUT_FLASK_BUTTON)
        with allure.step('Проверка страницы'):
            assert 'Welcome to Flask' in self.driver.title

    @allure.title('Тест перехода на Download Centos7')
    def test_download_centos(self):
        """
        Тест перехода на сайт со скачиванием CentOS.
        После нажатия на кнопку 'Download Centos7' открывается новая вкладка с данным ресурсом.
        Проверяется наличие строки в title сайта.
        """
        with allure.step('Нажатие на кнопку Download Centos7'):
            self.cabinet_page.go_outside_hide(self.cabinet_page.locators.LINUX_BUTTON,
                                              self.cabinet_page.locators.DOWNLOAD_CENTOS_BUTTON)
        with allure.step('Проверка страницы'):
            assert 'CentOS' in self.driver.title

    @allure.title('Тест перехода на Wireshark News')
    def test_news(self):
        """
        Тест перехода на сайт с новостями Wireshark.
        После нажатия на кнопку 'News' открывается новая вкладка с данным ресурсом.
        Проверяется наличие строки в title сайта.
        """
        with allure.step('Нажатие на кнопку News'):
            self.cabinet_page.go_outside_hide(self.cabinet_page.locators.NETWORK_BUTTON,
                                              self.cabinet_page.locators.NEWS_BUTTON)
        with allure.step('Проверка страницы'):
            assert 'Wireshark · News' in self.driver.title

    @allure.title('Тест перехода на Wireshark Download')
    def test_download(self):
        """
        Тест перехода на сайт со скачиванием Wireshark.
        После нажатия на кнопку 'Download' открывается новая вкладка с данным ресурсом.
        Проверяется наличие строки в title сайта.
        """
        with allure.step('Нажатие на кнопку Download'):
            self.cabinet_page.go_outside_hide(self.cabinet_page.locators.NETWORK_BUTTON,
                                              self.cabinet_page.locators.DOWNLOAD_NET_BUTTON)
        with allure.step('Проверка страницы'):
            assert 'Wireshark · Go Deep.' in self.driver.title

    @allure.title('Тест перехода на Tcpdump Examples')
    def test_examples(self):
        """
        Тест перехода на сайт с Tcpdump Examples.
        После нажатия на кнопку 'Examples' открывается новая вкладка с данным ресурсом.
        Проверяется наличие строки в title сайта.
        """
        with allure.step('Нажатие на кнопку Examples'):
            self.cabinet_page.go_outside_hide(self.cabinet_page.locators.NETWORK_BUTTON,
                                              self.cabinet_page.locators.EXAMPLES_BUTTON)
        with allure.step('Проверка страницы'):
            assert 'Tcpdump Examples' in self.driver.title

    @allure.title('Тест перехода на What is an API?')
    def test_what_is_api(self):
        """
        Тест перехода на сайт с информациоей о API.
        После нажатия на кнопку 'What is an API?' открывается новая вкладка с данным ресурсом.
        Проверяется наличие строки в title сайта.
        """
        with allure.step('Нажатие на кнопку What is an API?'):
            self.cabinet_page.go_outside_main(self.cabinet_page.locators.WHAT_IS_BUTTON)
        with allure.step('Проверка страницы'):
            assert 'API - Wikipedia' in self.driver.title

    @allure.title('Тест перехода на Future of internet')
    def test_future(self):
        """
        Тест перехода на сайт со стайтьей об интернете.
        После нажатия на кнопку 'Future of internet' открывается новая вкладка с данным ресурсом.
        Проверяется наличие строки в title сайта.
        """
        with allure.step('Нажатие на кнопку Future of internet'):
            self.cabinet_page.go_outside_main(self.cabinet_page.locators.FUTURE_BUTTON)
        with allure.step('Проверка страницы'):
            assert 'What Will the Internet Be Like in the Next 50 Years?' in self.driver.title

    @allure.title('Тест перехода на Lets talk about SMTP?')
    def test_about_smtp(self):
        """
        Тест перехода на сайт с информацией о SMTP.
        После нажатия на кнопку 'Lets talk about SMTP?' открывается новая вкладка с данным ресурсом.
        Проверяется наличие строки в title сайта.
        """
        with allure.step('Нажатие на кнопку Lets talk about SMTP?'):
            self.cabinet_page.go_outside_main(self.cabinet_page.locators.SMTP_BUTTON)
        with allure.step('Проверка страницы'):
            assert 'SMTP — Википедия' in self.driver.title

    @allure.title('Тест факта о python')
    def test_facts(self):
        """
        Тест проверяет наличие случайного факта внизу страницы.
        """
        with allure.step('Поиск факта'):
            self.cabinet_page.find(self.cabinet_page.locators.FACTS, 10)

    @allure.title('Тест VK ID')
    def test_vk_id(self):
        """
        Тест проверяет получение VK ID для пользователя.
        В первую очередь пользователь добавляется в базу mock.
        Затем страница приложения обновляется и проверяется наличие
        VK ID в правом верхнем углу ЛК пользователя.
        """
        with allure.step('Добавление пользователя в базу mock'):
            requests.get(f'http://0.0.0.0:7777/add_user/{self.username}')
        with allure.step('Получение VK ID из mock'):
            response = requests.get(f'http://0.0.0.0:7777/check/{self.username}')
        with allure.step('Обновление страницы'):
            self.cabinet_page.click(self.cabinet_page.locators.HOME_BUTTON, 10)
        with allure.step('Поиск VK ID'):
            self.cabinet_page.find((By.XPATH, f"//li[text()='VK ID: {response.text}']"), 10)

    @allure.title('Тест на блокировку пользователя')
    def test_deautorization_user(self, fake_data):
        """
        Тест на деавторизацию после блокировки.
        После успешной авторизации, при помощи orm поле
        access меняется с 1 на 0.
        Следующий запрос на странице должен деавторизовывать пользователя.
        Проверяется, что произошел переход на страницу авторизации.
        """
        with allure.step('Блокировка пользователя через orm'):
            MysqlOrmBuilder().drop_access(fake_data['username'])
        with allure.step('Обновление страницы'):
            self.cabinet_page.click(self.cabinet_page.locators.HOME_BUTTON, 10)
        with allure.step('Проверка страницы'):
            assert 'Welcome to the TEST SERVER' in self.driver.page_source

    @allure.title('Проверка активности пользователя')
    def test_user_activity(self, fake_data):
        """
        Тест на 'активность пользователя'.
        Проверяет при помощи orm колонки active и start_active_time.
        """
        with allure.step('Выбор пользователя из БД'):
            user = MysqlOrmBuilder().select_from_table(fake_data['username'])
        with allure.step('Проверка active и start_active_time'):
            assert user.active == 1
            assert user.start_active_time is not None

    @allure.title('Проверка активности пользователя после logout')
    def test_logout_activity(self, fake_data):
        """
        Тест на поле active при выходе пользователя.
        Проверяет при помощи orm колонки active и start_active_time.
        """
        with allure.step('logout'):
            self.cabinet_page.click(self.cabinet_page.locators.LOGOUT_BUTTON, 10)
        with allure.step('Выбор пользователя из БД'):
            user = MysqlOrmBuilder().select_from_table(fake_data['username'])
        with allure.step('Проверка active и start_active_time'):
            assert user.active == 0
            assert user.start_active_time is None

    @allure.title('Негативный тест на VK ID')
    def test_without_vk_id(self):
        """
        Тест на отсутсвие VK ID у пользователя.
        Если приложению не удалось получить VK ID, то
        данное поле должно быть пустым.
        """
        with allure.step('Проверка отсутсвия VK ID'):
            self.cabinet_page.find(self.cabinet_page.locators.NONE_VK_ID, 10)
