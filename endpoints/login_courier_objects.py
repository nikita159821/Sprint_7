import requests

from endpoints.base_endpoints import Endpoints
from tests.data import COURIER_LOGIN_AND_PASSWORD, URL, COURIER_LOGIN, MESSAGE_CHECK_LOGIN_COURIER_EMPTY, \
    INVALID_CREDENTIALS, MESSAGE_CHECK_LOGIN_WITH_INVALID_CREDENTIALS


class LoginCourier(Endpoints):

    # курьер может авторизоваться
    def login_courier(self):
        payload = COURIER_LOGIN_AND_PASSWORD
        self.response = requests.post(f'{URL}api/v1/courier/login', data=payload)

    # Для авторизации нужно передать все обязательные поля
    def login_courier_empty_payload(self):
        payload = COURIER_LOGIN
        self.response = requests.post(f'{URL}api/v1/courier/login', data=payload)

    # Метод проверяет статус код и тело после авторзиции без пароля
    def check_login_courier_empty_payload_is_400(self):
        response_body = self.response.json()
        assert response_body["code"] == 400
        assert response_body["message"] == MESSAGE_CHECK_LOGIN_COURIER_EMPTY

    # Система вернёт ошибку, если неправильно указать логин или пароль
    def login_with_invalid_credentials(self):
        payload = INVALID_CREDENTIALS
        self.response = requests.post(f'{URL}api/v1/courier/login', data=payload)

    # Метод проверяет статус код и тело после авторзиции c несущ.данными
    def check_login_with_invalid_credentials_is_404(self):
        response_body = self.response.json()
        assert response_body["code"] == 404
        assert response_body["message"] == MESSAGE_CHECK_LOGIN_WITH_INVALID_CREDENTIALS

