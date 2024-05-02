from endpoints.create_courier_objects import CreateCourier
from endpoints.create_order_objects import CreateOrder
from endpoints.login_courier_objects import LoginCourier


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


def test_send_color_request():
    send_color_request = CreateOrder()
    send_color_request.send_color_request_black()
    send_color_request.check_response_is_201()


def test_send_color_request_black_and_grey():
    color_request_black_and_grey = CreateOrder()
    color_request_black_and_grey.send_color_request_black_and_grey()
    color_request_black_and_grey.check_response_is_201()


def test_send_order_request():
    send_order_request = CreateOrder()
    send_order_request.send_order_request()
    send_order_request.check_response_is_201()


def test_check_send_request():
    heck_send_request = CreateOrder()
    heck_send_request.send_request_and_check()
    heck_send_request.check_send_request()
