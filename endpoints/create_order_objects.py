import json

import requests

from endpoints.base_endpoints import Endpoints
from tests.data import ORDER_COLOR_BLACK, URL, ORDER_COLOR_BLACK_AND_GREY, ORDER


class CreateOrder(Endpoints):

    # можно указать один из цветов — BLACK или GREY
    def send_color_request_black(self):
        payload = json.dumps(ORDER_COLOR_BLACK)  # Преобразуем словарь в JSON-строку
        self.response = requests.post(f'{URL}api/v1/orders', data=payload)

    # можно указать оба цвета
    def send_color_request_black_and_grey(self):
        payload = json.dumps(ORDER_COLOR_BLACK_AND_GREY)  # Преобразуем словарь в JSON-строку
        self.response = requests.post(f'{URL}api/v1/orders', data=payload)

    # можно совсем не указывать цвет
    def send_order_request(self):
        payload = json.dumps(ORDER)  # Преобразуем словарь в JSON-строку
        self.response = requests.post(f'{URL}api/v1/orders', data=payload)

