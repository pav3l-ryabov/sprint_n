import allure

from data import AD_BODY, NEW_AD_BODY
from methods.ad_methods import AdMethods


class TestAd:
    @allure.title('Тест создания объявления')
    def test_create_new_ad(self, create_user_fixture):
        email, password, access_token = create_user_fixture()
        payload = AD_BODY
        response, status = AdMethods().create_ad(payload, access_token)

        assert status == 201, f'Ожидали 201, получили {status}'

    @allure.title('Тест редактирования объявления')
    def test_update_ad(self, create_user_fixture):
        email, password, access_token = create_user_fixture()
        payload = AD_BODY
        ad_methods = AdMethods()
        response, status = ad_methods.create_ad(payload, access_token)

        data = response.json()
        id = data.get('id')
        new_payload = NEW_AD_BODY
        response, status = ad_methods.patch_ad(new_payload, access_token, id)

        assert status == 200, f'Ожидали 200, получили {status}'

    @allure.title('Тест редактирования объявления не тем пользователем, который его создал')
    def test_update_ad_with_invalid_token(self, create_user_fixture):
        email, password, access_token = create_user_fixture()
        payload = AD_BODY
        ad_methods = AdMethods()
        response, status = ad_methods.create_ad(payload, access_token)
        data = response.json()
        id = data.get('id')

        new_email, new_password, new_access_token = create_user_fixture()
        new_payload = NEW_AD_BODY
        response, status = ad_methods.patch_ad(new_payload, new_access_token, id)

        assert status == 401, f'Ожидали 401, получили {status}'

    @allure.title('Тест удаления объявления')
    def test_delete_ad(self, create_user_fixture):
        email, password, access_token = create_user_fixture()
        payload = AD_BODY
        ad_methods = AdMethods()
        response, status = ad_methods.create_ad(payload, access_token)

        data = response.json()
        id = data.get('id')
        response, status = ad_methods.delete_ad(access_token, id)

        assert status == 200, f'Ожидали 200, получили {status}'