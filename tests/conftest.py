import pytest

from credentials_generator import register_new_user_and_return_email_password_token


@pytest.fixture
def create_user_fixture():
    def _create():
        return register_new_user_and_return_email_password_token()
    return _create