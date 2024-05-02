from endpoints.create_courier_objects import CreateCourier


def test_create_courier():
    new_test = CreateCourier()
    new_test.create_courier()
    new_test.check_create_courier_is_201()
