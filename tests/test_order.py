from endpoints.create_order_objects import CreateOrder
from endpoints.receiving_orders_objects import ReceivingOrders


class TestOrder:
    def test_create_order(self, order_data):
        order = CreateOrder()
        order.send_order_request(order_data)
        order.check_send_request()
        order.check_response_is_201()

    def test_order_list(self):
        order_list = ReceivingOrders()
        order_list.order_list()
        order_list.check_order_list()
        order_list.check_response_is_200()
