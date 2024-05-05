import allure

from endpoints.receiving_orders_objects import ReceivingOrders


class TestOrderList:
    @allure.title("Проверка на получения списка заказов")
    def test_order_list(self):
        order_list = ReceivingOrders()
        order_list.order_list()
        order_list.check_order_list()
        order_list.check_response_is_200()
