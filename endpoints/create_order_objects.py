import json

import allure
import requests

from endpoints.base_response_checker import ResponseChecker
from tests.data import URL, ORDERS


class CreateOrder(ResponseChecker):

    @allure.step('Создаем заказ')
    def send_order_request(self, order_data):
        payload = json.dumps(order_data)
        self.response = requests.post(f'{URL}{ORDERS}', data=payload)

    # Метод проверяет, что в теле возвращается track
    def check_send_request(self):
        response_body = self.response.json()
        assert "track" in response_body
