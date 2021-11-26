from app.loadmonth import LoadMonth
import numpy as np
from datetime import datetime
import pytest

def test_loadmonth_creation():
    name = "Mar.22"
    month = LoadMonth(name)
    if month.name == name:
        assert True
    else:
        assert False

@pytest.fixture
def month():
    return LoadMonth("test")

def test_window(month):
    month.window_append(3.45)
    if isinstance(month.window_get(), np.ndarray):
        assert 3.45 == month.window_get()[0]
    else:
        assert False

def test_load_data(month):
    month.window_append(3.50)
    month.window_pop()
    month.window_append(-4.50)
    month.load_data(datetime(1970,1,1,0,0), 4.50, month.window_get())
    assert 4.50 == month.get_value(datetime(1970,1,1,0,0))[0]
    assert -4.50 == month.window_get()[0]
