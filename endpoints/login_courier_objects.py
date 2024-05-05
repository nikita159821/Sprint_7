import allure
import requests

from endpoints.base_response_checker import ResponseChecker
from tests.data import COURIER_LOGIN_AND_PASSWORD, URL, COURIER_LOGIN, MESSAGE_CHECK_LOGIN_COURIER_EMPTY, \
    INVALID_CREDENTIALS, MESSAGE_CHECK_LOGIN_WITH_INVALID_CREDENTIALS, LOGIN, USER_ID


class LoginCourier(ResponseChecker):

    @allure.step('Проходим авторизацию')
    def login_courier(self):
        payload = COURIER_LOGIN_AND_PASSWORD
        self.response = requests.post(f'{URL}{LOGIN}', data=payload)

    @allure.step('Заполняем все обязательные поля')
    def login_courier_empty_payload(self):
        payload = COURIER_LOGIN
        self.response = requests.post(f'{URL}{LOGIN}', data=payload)

    @allure.step('Проверяем тело  после авторзиции без пароля')
    def check_login_courier_empty_payload(self):
        response_body = self.response.json()
        assert response_body["message"] == MESSAGE_CHECK_LOGIN_COURIER_EMPTY

    @allure.step('Система возвращает ошибку, если неправильно указать логин или пароль')
    def login_with_invalid_credentials(self):
        payload = INVALID_CREDENTIALS
        self.response = requests.post(f'{URL}{LOGIN}', data=payload)

    @allure.step('Проверяем статус код и тело после авторзиции c несущ.данными')
    def check_login_with_invalid_credentials_is_404(self):
        response_body = self.response.json()
        assert response_body["code"] == 404
        assert response_body["message"] == MESSAGE_CHECK_LOGIN_WITH_INVALID_CREDENTIALS

    @allure.step('Проверяем,что возвращается id пользователя в теле')
    def check_response_is_id(self):
        response_body = self.response.json()
        assert response_body["id"] == USER_ID

