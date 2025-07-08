import allure
import requests

import data


class UserMethods:
    @allure.step('Создание пользователя')
    def create_user(self, payload):
        response = requests.post(f'{data.BASE_URL}{data.SIGNUP_URL}', json = payload)
        return response, response.status_code

    @allure.step('Логин пользователя')
    def login_user(self, payload):
        response = requests.post(f'{data.BASE_URL}{data.SIGNIN_URL}', json = payload)
        return response, response.status_code
