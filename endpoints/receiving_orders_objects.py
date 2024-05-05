import allure
import requests

from endpoints.base_response_checker import ResponseChecker
from tests.data import URL, COURIER_ID, ORDER_LIST, ORDERS


class ReceivingOrders(ResponseChecker):

    @allure.step('Возвращаем список заказов')
    def order_list(self):
        self.response = requests.get(f'{URL}{ORDERS}{COURIER_ID}')

    # Проверяем список заказов
    def check_order_list(self):
        response_body = self.response.json()
        assert response_body == ORDER_LIST

