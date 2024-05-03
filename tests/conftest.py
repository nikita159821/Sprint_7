import sys
import os

import pytest

from tests.data import ORDER_COLOR_BLACK, ORDER_COLOR_BLACK_AND_GREY, ORDER

# Добавляем путь к директории
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture(params=[ORDER_COLOR_BLACK, ORDER_COLOR_BLACK_AND_GREY, ORDER])
def order_data(request):
    return request.param
