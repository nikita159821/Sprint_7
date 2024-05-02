import random
import string


class Endpoints:
    response = None

    def check_response_is_201(self):
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

        # возвращаем словарь с учетными данными
        payload = {"login": login, "password": password, "firstName": first_name}
        return payload
