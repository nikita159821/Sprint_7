import random
import string

import allure
import requests
from endpoints.base_response_checker import ResponseChecker

from tests.data import URL, CREATE_DUPLICATE_COURIER, MESSAGE_CHECK_CREATE_DUPLICATE, \
    MESSAGE_CHECK_CREATE_COURIER_EMPTY, COURIER, MESSAGE_CHECK_CREATE_COURIER


class CreateCourier(ResponseChecker):

    @allure.step('Генерируем login, password, first_name')
    def register_new_courier_and_return_login_password(self):
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {"login": login, "password": password, "firstName": first_name}
        return payload

    @allure.step('создаем курьера с уникальными данными')
    def create_courier(self):
        payload = self.register_new_courier_and_return_login_password()
        self.response = requests.post(f'{URL}{COURIER}', json=payload)

    @allure.step('создаем курьера не с уникальными данными')
    def create_duplicate_courier(self):
        payload = CREATE_DUPLICATE_COURIER
        self.response = requests.post(f'{URL}{COURIER}', data=payload)

    @allure.step('создаем курьера без данных для регистрации')
    def create_courier_empty_payload(self):
        self.response = requests.post(f'{URL}{COURIER}')

    @allure.step('Проверка статус кода после создания существующего курьера')
    def check_create_duplicate_courier_is_409(self):
        response_body = self.response.json()
        assert response_body["code"] == 409
        assert response_body["message"] == MESSAGE_CHECK_CREATE_DUPLICATE

    @allure.step('Проверка статус кода после создания курьера без данных для регистрации')
    def check_create_courier_empty_payload(self):
        response_body = self.response.json()
        assert response_body["message"] == MESSAGE_CHECK_CREATE_COURIER_EMPTY

    @allure.step('Проверка тела ответа после создания курьераи')
    def check_courier_creation_response_body(self):
        response_body = self.response.json()
        assert response_body["ok"] == MESSAGE_CHECK_CREATE_COURIER
