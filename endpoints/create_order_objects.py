import json

import pytest
import requests

from endpoints.base_endpoints import Endpoints
from tests.data import ORDER_COLOR_BLACK, URL, ORDER_COLOR_BLACK_AND_GREY, ORDER


class CreateOrder(Endpoints):

    def send_order_request(self, order_data):
        payload = json.dumps(order_data)
        self.response = requests.post(f'{URL}api/v1/orders', data=payload)

    # Метод проверяет, что в теле возвращается track
    def check_send_request(self):
        response_body = self.response.json()
        assert "track" in response_body
