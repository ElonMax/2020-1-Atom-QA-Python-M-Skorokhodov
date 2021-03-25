"""
Тестирование API приложения
"""
import allure
import requests

from clients.mysql_orm_client.builder import MysqlOrmBuilder


@allure.feature('Тестирование API')
class TestApi:

    @allure.title('Проверка статуса приложения')
    def test_status(self, api_client):
        """
        Тест проверяет статус приложения.
        Выполняется GET запрос к '/status'.
        Форма ответа {'status': 'ok'}.
        """
        with allure.step('Получение статуса'):
            response = api_client.status()
        with allure.step('Подтверждение статуса'):
            assert 'ok' in response.text

    @allure.title('Добавление пользователя')
    def test_add_user(self, autorization_api, another_fake):
        """
        Тест проверяет добавление пользователя через API.
        Через orm осуществялется проверка, что пользователь добавлен в БД.
        """
        with allure.step('Добавление пользователя через API'):
            autorization_api.add_user(username=another_fake['username'],
                                      password=another_fake['password'],
                                      email=another_fake['email'])
        with allure.step('Проверка БД'):
            assert MysqlOrmBuilder().select_from_table(another_fake['username']).username == another_fake['username']

    @allure.title('Удаление пользователя')
    def test_delete_user(self, autorization_api, another_fake):
        """
        Тест проверяет удаление пользователя через API.
        Через orm осуществляется добавление пользователя в БД и
        проверка, что пользователь успешно удален.
        """
        with allure.step('Добавление пользователя через БД'):
            MysqlOrmBuilder().add_user(username=another_fake['username'],
                                       password=another_fake['password'],
                                       email=another_fake['email'])
        with allure.step('Удаление пользователя через API'):
            autorization_api.delete_user(username=another_fake['username'])
        with allure.step('Проверка отуствия пользователя в БД'):
            assert MysqlOrmBuilder().select_from_table(another_fake['username']) is None

    @allure.title('Блокировка пользователя')
    def test_block_user(self, autorization_api, another_fake):
        """
        Тест проверяет блокировку пользователя через API.
        Через orm осуществляется добавление пользователя в БД и
        проверка, что поле access у пользователя стало равно 0.
        """
        with allure.step('Добавление пользователя через БД'):
            MysqlOrmBuilder().add_user(username=another_fake['username'],
                                       password=another_fake['password'],
                                       email=another_fake['email'])
        with allure.step('Блокировка пользователя через API'):
            autorization_api.block_user(username=another_fake['username'])
        with allure.step('Проверка access в БД'):
            assert MysqlOrmBuilder().select_from_table(another_fake['username']).access == 0

    @allure.title('Разблокировка пользователя')
    def test_unblock_user(self, autorization_api, another_fake):
        """
        Тест проверяет разблокировку пользователя через API.
        Через orm осуществялется добавление пользователя в БД с
        access=0 и проверка, что access изменился на 1.
        """
        with allure.step('Добавление заблокированного пользователя через БД'):
            MysqlOrmBuilder().add_user(username=another_fake['username'],
                                       password=another_fake['password'],
                                       email=another_fake['email'],
                                       access=0)
        with allure.step('Разблокировка пользователя через API'):
            autorization_api.unblock_user(username=another_fake['username'])
        with allure.step('Проверка access в БД'):
            assert MysqlOrmBuilder().select_from_table(another_fake['username']).access == 1

    @allure.title('Проверка 304')
    def test_not_modify(self, autorization_api, fake_data):
        """
        Тест проверяет код 304 (Сущность существует/не изменилась).
        Попытка добавить существущего пользователя через API.
        """
        with allure.step('Добавление существующего пользователя'):
            autorization_api.add_user(username=fake_data['username'],
                                      password=fake_data['password'],
                                      email=fake_data['email'],
                                      status_code=304)

    @allure.title('Проверка 404')
    def test_not_exists(self, autorization_api):
        """
        Тест проверяет код 404 (Сущности не существует).
        Попытка удаления несуществующего пользователя.
        """
        with allure.step('Удаление несуществующего пользователя'):
            autorization_api.delete_user(username='test',
                                         status_code=404)

    @allure.title('Проверка 401')
    def test_unautorized(self, api_client):
        """
        Тест проверяет код 401 (Пользователь не авторизован).
        Попытка авторизации несуществующего пользователя.
        """
        with allure.step('Авторизация несуществующего пользователя'):
            api_client.login(username='app_test_1', password='test', status_code=401)

    @allure.title('Find me error')
    def test_find_me_error(self, autorization_api):
        """
        Тест на Find me error.
        GET запрос по '/static/scripts/findMeError.js'
        """
        with allure.step('Запрос к find me error'):
            autorization_api._request('GET', '/static/scripts/findMeError.js')

    @allure.title('Проверка 400')
    def test_bad_request(self, autorization_api, another_fake):
        """
        Тест на код 400 (Плохой запрос).
        Попытка отправить некорректный POST запрос через API по адресу '/api/add_user'.
        """
        with allure.step('Добавление пользователя с некорректными данными'):
            autorization_api.bad_request_add_user(username=another_fake['username'],
                                                  status_code=400)
