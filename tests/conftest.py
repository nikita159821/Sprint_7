import os
import sys
import pytest

from data import ORDER_COLOR_BLACK, ORDER_COLOR_BLACK_AND_GREY, ORDER


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)


@pytest.fixture(params=[ORDER_COLOR_BLACK, ORDER_COLOR_BLACK_AND_GREY, ORDER])
def order_data(request):
    return request.param
