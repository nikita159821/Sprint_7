import random
import string

import requests
from endpoints.base_endpoints import Endpoints

from tests.data import URL, CREATE_DUPLICATE_COURIER, MESSAGE_CHECK_CREATE_DUPLICATE, MESSAGE_CHECK_CREATE_COURIER_EMPTY


class CreateCourier(Endpoints):

    # Генерируем login, password, first_name
    def register_new_courier_and_return_login_password(self):
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # возвращаем словарь с учетными данными
        payload = {"login": login, "password": password, "firstName": first_name}
        return payload

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
    def check_create_courier_empty_payload(self):
        response_body = self.response.json()
        assert response_body["message"] == MESSAGE_CHECK_CREATE_COURIER_EMPTY
