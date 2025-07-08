import allure
import requests

import data


class AdMethods:
    @allure.step('Создание объявления')
    def create_ad(self, payload: dict, access_token: str):
        files = {key: (None, str(value)) for key, value in payload.items()}
        headers = {
            'Authorization': f'Bearer {access_token}',
        }
        response = requests.post(
            f'{data.BASE_URL}{data.CREATE_AD_URL}',
            files=files,
            headers=headers
        )
        return response, response.status_code

    @allure.step('Изменение объявления')
    def patch_ad(self, payload: dict, access_token: str, id):
        files = {key: (None, str(value)) for key, value in payload.items()}
        headers = {
            'Authorization': f'Bearer {access_token}',
        }
        response = requests.patch(
            f'{data.BASE_URL}{data.UPDATE_OFFER_URL}{id}',
            files=files,
            headers=headers
        )
        return response, response.status_code

    @allure.step('Удаление объявления')
    def delete_ad(self, access_token: str, id):
        headers = {
            'Authorization': f'Bearer {access_token}',
        }
        response = requests.delete(
            f'{data.BASE_URL}{data.LISTING_URL}{id}', headers=headers)
        return response, response.status_code