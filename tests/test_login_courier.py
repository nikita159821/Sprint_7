import allure

from endpoints.login_courier_objects import LoginCourier


class TestLogin:

    @allure.title("Проверка авторизации")
    def test_login_courier(self):
        login_courier = LoginCourier()
        login_courier.login_courier()
        login_courier.check_response_is_200()
        login_courier.check_response_is_id()

    @allure.title("Проверка авторизации без логина и пароля")
    def test_login_courier_empty_payload(self):
        courier_empty_payload = LoginCourier()
        courier_empty_payload.login_courier_empty_payload()
        courier_empty_payload.check_login_courier_empty_payload()
        courier_empty_payload.check_response_is_400()

    @allure.title("Проверка авторизации с несуществующей парой логин-пароль")
    def test_login_with_invalid_credentials(self):
        invalid_credentials = LoginCourier()
        invalid_credentials.login_with_invalid_credentials()
        invalid_credentials.check_login_with_invalid_credentials_is_404()
