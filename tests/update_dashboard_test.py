import os
import httpretty
from collections import namedtuple
import pytest

from ..dashboard import *

@pytest.fixture(scope="function", autouse=True)
def setup_envars():
    os.environ['DASHBOARD_HOST'] = 'https://localhost'
    os.environ['AUTH_TOKEN'] = 'our auth token'

@pytest.fixture(scope="function", autouse=True)
def enable_httpretty():
    httpretty.enable()

    def disable_httpretty():
        httpretty.disable()


@pytest.fixture
def compiled_data():
    CompiledData = namedtuple('Data', ['total_distance', 'total_moving_time', 'average_speed', 'max_speed'])
    return CompiledData(total_distance=12345, total_moving_time=600, average_speed=10, max_speed=15)

def test_update_total_distance(compiled_data):
    httpretty.register_uri(httpretty.POST, 'https://localhost/widgets/total_distance')

    update_total_distance(compiled_data)

    assert httpretty.has_request()

    last_request = httpretty.last_request()
    assert last_request.method == 'POST'
    assert last_request.parsed_body.get('current') == 12.3
    assert last_request.parsed_body.get('auth_token') == 'our auth token'

def test_update_average_speed(compiled_data):
    httpretty.register_uri(httpretty.POST, 'https://localhost/widgets/average_speed')

    update_average_speed(compiled_data)

    assert httpretty.has_request()

    last_request = httpretty.last_request()
    assert last_request.method == 'POST'
    assert last_request.parsed_body.get('current') == 36.0
    assert last_request.parsed_body.get('auth_token') == 'our auth token'

def test_update_max_speed(compiled_data):
    httpretty.register_uri(httpretty.POST, 'https://localhost/widgets/maximum_speed')

    update_max_speed(compiled_data)

    assert httpretty.has_request()

    last_request = httpretty.last_request()
    assert last_request.method == 'POST'
    assert last_request.parsed_body.get('current') == 54.0
    assert last_request.parsed_body.get('auth_token') == 'our auth token'

def test_update_max_speed(compiled_data):
    httpretty.register_uri(httpretty.POST, 'https://localhost/widgets/total_moving_time')

    update_total_moving_time(compiled_data)

    assert httpretty.has_request()

    last_request = httpretty.last_request()
    assert last_request.method == 'POST'
    assert last_request.parsed_body.get('current') == 0.2
    assert last_request.parsed_body.get('auth_token') == 'our auth token'
