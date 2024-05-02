from endpoints.create_courier_objects import CreateCourier


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
    courier_empty_payload.check_create_courier_empty_payload_is_400()
