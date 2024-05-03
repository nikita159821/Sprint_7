from endpoints.create_courier_objects import CreateCourier
from endpoints.create_order_objects import CreateOrder
from endpoints.login_courier_objects import LoginCourier
from endpoints.receiving_orders_objects import ReceivingOrders


def test_create_courier():
    new_create_courier = CreateCourier()
    new_create_courier.create_courier()
    new_create_courier.check_response_is_201()


def test_create_duplicate_courier():
    duplicate_courier = CreateCourier()
    duplicate_courier.create_duplicate_courier()
    duplicate_courier.check_create_duplicate_courier_is_409()


def test_create_courier_empty_payload():
    courier_empty_payload = CreateCourier()
    courier_empty_payload.create_courier_empty_payload()
    courier_empty_payload.check_response_is_400()


def test_login_courier():
    login_courier = LoginCourier()
    login_courier.login_courier()
    login_courier.check_response_is_200()
    login_courier.check_response_is_id()


def test_login_courier_empty_payload():
    courier_empty_payload = LoginCourier()
    courier_empty_payload.login_courier_empty_payload()
    courier_empty_payload.check_login_courier_empty_payload()
    courier_empty_payload.check_response_is_400()


def test_login_with_invalid_credentials():
    invalid_credentials = LoginCourier()
    invalid_credentials.login_with_invalid_credentials()
    invalid_credentials.check_login_with_invalid_credentials_is_404()


def test_create_order(order_data):
    order = CreateOrder()
    order.send_order_request(order_data)
    order.check_send_request()


def test_order_list():
    order_list = ReceivingOrders()
    order_list.order_list()
    order_list.check_order_list()
