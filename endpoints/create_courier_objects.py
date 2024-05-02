import requests
import random
import string

from tests.data import URL


class CreateCourier:

    def __init__(self):
        self.response_status = None
        self.response = None
        self.login_pass = None

    # Метод создания курьера
    def create_courier(self):
        self.login_pass = self.register_new_courier_and_return_login_password()
        login, password, first_name = self.login_pass
        self.response = requests.post(f'{URL}api/v1/courier', data={
            "login": login,
            "password": password,
            "firstName": first_name
        })
        self.response_status = self.response.status_code

    # Метод проверяет статус код после создания курьера
    def check_create_courier_is_201(self):
        assert self.response.status_code == 201

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

        # возвращаем список с учетными данными
        return [login, password, first_name]
