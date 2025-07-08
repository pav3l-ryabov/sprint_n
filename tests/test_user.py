import allure

import data as data
from methods.user_methods import UserMethods


class TestUser:
    @allure.title('Тест создания рандомного юзера')
    def test_create_new_random_user(self, create_user_fixture):
        email, password, access_token = create_user_fixture()
        assert all((email, password, access_token)), \
            'пользователь не создался, т.к. ни одно из полей email, password, access_token не может быть пустым'

    @allure.title('Тест создания уже существующего юзера')
    def test_create_existing_user(self, create_user_fixture):
        email, password, _ = create_user_fixture()
        payload = {
            "email": email,
            "password": password,
            "submitPassword": password
        }
        response, status = UserMethods.create_user(self, payload)
        assert status == 400, f'Ожидали 400, получили {status}'
        assert data.RESPONSE_BODY_EXIST_USER == response.json(), f'Ответ не соответствует ожидаемому: {response.json()}'

    @allure.title('Тест авторизации юзера')
    def test_auth_user(self, create_user_fixture):
        email, password, _ = create_user_fixture()
        payload = {
            "email": email,
            "password": password
        }
        response, status = UserMethods.login_user(self, payload)
        assert status == 201, f'Ожидали 200, получили {status}'