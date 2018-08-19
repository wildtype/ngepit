from io import StringIO
from unittest.mock import patch, NonCallableMock, Mock
from ..cycling import CyclingSession

moving_data = NonCallableMock(moving_distance=10, moving_time=20, max_speed=30)
dummy_parsed_gpx = NonCallableMock(get_moving_data=Mock(return_value=moving_data))
gpx_fh = StringIO()

@patch('gpxpy.parse', return_value='dummy_parsed_gpx')
def test_init_accept_params_gpx_file_handle_then_parse_it(dummy_gpxpy_parse):
    session = CyclingSession(gpx_fh)

    dummy_gpxpy_parse.assert_called_with(gpx_fh)
    assert session.gpx_data == 'dummy_parsed_gpx'

@patch('gpxpy.parse', return_value=dummy_parsed_gpx)
def test_summary_it_calls_get_moving_data_of_parsed_gpx_and_use_its_values(dummy_gpxpy_parse):
    session = CyclingSession(gpx_fh)
    summary = session.summary()

    assert dummy_parsed_gpx.get_moving_data.called
    assert summary.distance == 10
    assert summary.moving_time == 20
    assert summary.average_speed == .5
    assert summary.max_speed == 30
