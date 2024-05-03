import requests

from endpoints.base_endpoints import Endpoints
from tests.data import URL, TEST, COURIER_ID


class ReceivingOrders(Endpoints):

    # возвращается список заказов
    def order_list(self):
        self.response = requests.get(f'{URL}api/v1/orders?{COURIER_ID}')
        print(self.response.json())

    # Проверяем список заказов
    def check_order_list(self):
        response_body = self.response.json()
        assert response_body == TEST

