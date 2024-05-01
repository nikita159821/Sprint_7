import requests
import pytest
from endpoints.create_courier_objects import CreateCourier


def test():
    new_test = CreateCourier()
    payload = {
        "login": "fasffasfsafsafsaff;ldkjlgjdgkljnfdlkbndlkfnbl",
        "password": "1234",
        "firstName": "saske"
    }

    new_test.create_courier(payload=payload)
    new_test.check_create_courier_is_200()
