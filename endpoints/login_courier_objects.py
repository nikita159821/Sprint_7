import requests

from endpoints.base_endpoints import Endpoints
from tests.data import COURIER_LOGIN, URL


class LoginCourier(Endpoints):

    # курьер может авторизоваться
    def login_courier(self):
        payload = COURIER_LOGIN
        self.response = requests.post(f'{URL}api/v1/courier/login', data=payload)


