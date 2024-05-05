from endpoints.create_courier_objects import CreateCourier


class TestCreateCourie:
    def test_create_courier(self):
        new_create_courier = CreateCourier()
        new_create_courier.create_courier()
        new_create_courier.check_response_is_201()
        new_create_courier.check_courier_creation_response_body()

    def test_create_duplicate_courier(self):
        duplicate_courier = CreateCourier()
        duplicate_courier.create_duplicate_courier()
        duplicate_courier.check_create_duplicate_courier_is_409()

    def test_create_courier_empty_payload(self):
        courier_empty_payload = CreateCourier()
        courier_empty_payload.create_courier_empty_payload()
        courier_empty_payload.check_response_is_400()
