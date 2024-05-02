URL = 'http://qa-scooter.praktikum-services.ru/'

CREATE_DUPLICATE_COURIER = {
    "login": "ninja",
    "password": "1234",
    "firstName": "saske"
}

COURIER_LOGIN_AND_PASSWORD = {
    "login": "testyyyy_2",
    "password": "test"
}

COURIER_LOGIN = {
    "login": "",
    "password": ""
}

INVALID_CREDENTIALS = {
    "login": "ninja",
    "password": "1234"
}

ORDER_COLOR_BLACK = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}

ORDER_COLOR_BLACK_AND_GREY = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK",
        "GREY"
    ]
}

ORDER = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha"
}


MESSAGE_CHECK_CREATE_DUPLICATE = 'Этот логин уже используется. Попробуйте другой.'
MESSAGE_CHECK_CREATE_COURIER_EMPTY = 'Недостаточно данных для создания учетной записи'
MESSAGE_CHECK_LOGIN_COURIER_EMPTY = 'Недостаточно данных для входа'
MESSAGE_CHECK_LOGIN_WITH_INVALID_CREDENTIALS = 'Учетная запись не найдена'
