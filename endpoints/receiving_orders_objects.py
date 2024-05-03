import allure
import requests

from endpoints.base_endpoints import Endpoints
from tests.data import URL, COURIER_ID, ORDER_LIST


class ReceivingOrders(Endpoints):

    @allure.step('Возвращаем список заказов')
    def order_list(self):
        self.response = requests.get(f'{URL}api/v1/orders?{COURIER_ID}')
        print(self.response.json())

    # Проверяем список заказов
    def check_order_list(self):
        response_body = self.response.json()
        assert response_body == ORDER_LIST

