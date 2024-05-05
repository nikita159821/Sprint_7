URL = 'http://qa-scooter.praktikum-services.ru/'
COURIER = 'api/v1/courier'
ORDERS = 'api/v1/orders?'
LOGIN = 'api/v1/courier/login'
COURIER_ID = 'courierId=298008'
USER_ID = 297526

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

ORDER_LIST = {'orders':
                  [{'id': 236364, 'courierId': 298008, 'firstName': 'Петр', 'lastName': 'Петров',
                    'address': 'ул. Ленина 11',
                    'metroStation': '2', 'phone': '89504564545', 'rentTime': 1,
                    'deliveryDate': '2024-02-23T19:00:00.000Z',
                    'track': 61731, 'color': ['BLACK'], 'comment': '', 'createdAt': '2024-01-29T15:35:30.471Z',
                    'updatedAt': '2024-05-03T05:08:10.469Z', 'status': 1},
                   {'id': 275644, 'courierId': 298008, 'firstName': 'Петр', 'lastName': 'Петров',
                    'address': 'ул. Ленина 11',
                    'metroStation': '2', 'phone': '89504564545', 'rentTime': 1,
                    'deliveryDate': '2024-02-23T19:00:00.000Z',
                    'track': 61731, 'color': ['BLACK'], 'comment': '', 'createdAt': '2024-05-03T05:08:10.488Z',
                    'updatedAt': '2024-05-03T05:08:10.488Z', 'status': 1}],
              'pageInfo': {'page': 0, 'total': 2, 'limit': 30}, 'availableStations':
                  [{'name': 'Черкизовская', 'number': '2', 'color': '#D92B2C'}]}

MESSAGE_CHECK_CREATE_DUPLICATE = 'Этот логин уже используется. Попробуйте другой.'
MESSAGE_CHECK_CREATE_COURIER_EMPTY = 'Недостаточно данных для создания учетной записи'
MESSAGE_CHECK_LOGIN_COURIER_EMPTY = 'Недостаточно данных для входа'
MESSAGE_CHECK_LOGIN_WITH_INVALID_CREDENTIALS = 'Учетная запись не найдена'
