import requests


class CreateCourier:
    response = None
    response_data = None
    response_status = None

    def create_courier(self, payload):
        self.response = requests.post('http://qa-scooter.praktikum-services.ru/api/v1/courier', json=payload)
        self.response_data = self.response.json()
        self.response_status = self.response.status_code

    def check_create_courier_is_200(self):
        assert self.response.status_code == 201
