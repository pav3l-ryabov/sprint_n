BASE_URL = 'https://qa-desk.stand.praktikum-services.ru'
SIGNUP_URL = '/api/signup'
SIGNIN_URL = '/api/signin'
CREATE_AD_URL = '/api/create-listing'
UPDATE_OFFER_URL = '/api/update-offer/'
LISTING_URL = '/api/listings/'

RESPONSE_BODY_EXIST_USER = {
    "statusCode": 400,
    "message": "Почта уже используется"
}

AD_BODY = {
            "name": "Название",
            "category": "Авто",
            "condition": "Новый",
            "city": "Москва",
            "description": "Текст объявления",
            "price": "1000"
        }
NEW_AD_BODY = {
            "name": "Название_new",
            "category": "Авто_new",
            "condition": "Новый_new",
            "city": "Москва_new",
            "description": "Текст объявления_new",
            "price": "5555"
        }