import allure

from endpoints.create_order_objects import CreateOrder
from endpoints.receiving_orders_objects import ReceivingOrders


class TestOrder:
    @allure.title("Проверка успешности создания заказа")
    def test_create_order(self, order_data):
        order = CreateOrder()
        order.send_order_request(order_data)
        order.check_send_request()
        order.check_response_is_201()