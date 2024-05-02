from endpoints.create_courier_objects import CreateCourier


def test_create_courier():
    new_create_courier = CreateCourier()
    new_create_courier.create_courier()
    new_create_courier.check_create_courier_is_201()
