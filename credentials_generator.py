import requests
import random
import string

import data


def register_new_user_and_return_email_password_token():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_random_email(length):
        allowed_chars = string.ascii_lowercase + string.digits + "._%+-"
        first_part = ''.join(random.choice(allowed_chars) for _ in range(length))
        email = f"{first_part}@test.com"
        return email

    user_credentials = []

    email = generate_random_email(10)
    password = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "submitPassword": password
    }

    response = requests.post(f'{data.BASE_URL}{data.SIGNUP_URL}', json=payload)

    data_js = response.json()
    raw = data_js.get("access_token")
    access_token = (raw.get("access_token") if isinstance(raw, dict) else raw)

    if response.status_code == 201:
        user_credentials.append(email)
        user_credentials.append(password)
        user_credentials.append(access_token)

    return user_credentials