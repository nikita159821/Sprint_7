import requests
from endpoints.base_endpoints import Endpoints

from tests.data import URL, CREATE_DUPLICATE_COURIER, MESSAGE_CHECK_CREATE_DUPLICATE, MESSAGE_CHECK_CREATE_COURIER_EMPTY


class CreateCourier(Endpoints):

    # Метод создания курьера с уникальными данными
    def create_courier(self):
        payload = self.register_new_courier_and_return_login_password()
        self.response = requests.post(f'{URL}api/v1/courier', json=payload)

    # Метод создания курьера не с уникальными данными
    def create_duplicate_courier(self):
        payload = CREATE_DUPLICATE_COURIER
        self.response = requests.post(f'{URL}api/v1/courier', data=payload)

    # Метод создания курьера без данных для регистрации
    def create_courier_empty_payload(self):
        self.response = requests.post(f'{URL}api/v1/courier')

    # Метод проверяет статус код после создания существующего курьера
    def check_create_duplicate_courier_is_409(self):
        response_body = self.response.json()
        assert response_body["code"] == 409
        assert response_body["message"] == MESSAGE_CHECK_CREATE_DUPLICATE

    # Метод проверяет статус код после создания курьера без данных для регистрации
    def check_create_courier_empty_payload_is_400(self):
        response_body = self.response.json()
        assert response_body["code"] == 400
        assert response_body["message"] == MESSAGE_CHECK_CREATE_COURIER_EMPTY
