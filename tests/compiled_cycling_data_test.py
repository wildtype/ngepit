from unittest.mock import NonCallableMock, Mock
from ..cycling import CompiledCyclingData

def test_init_it_have_initial_data_with_values_zero():
    compiled = CompiledCyclingData()

    assert compiled.total_distance == 0
    assert compiled.total_moving_time == 0
    assert compiled.average_speed == 0
    assert compiled.max_speed == 0

def test_add_it_accept_cycling_session_as_params_and_update_data():
    cycling_session_1 = Mock(summary=Mock(return_value=NonCallableMock(distance=10, moving_time=20, average_speed=.5, max_speed=30)))
    cycling_session_2 = Mock(summary=Mock(return_value=NonCallableMock(distance=10, moving_time=20, average_speed=.5, max_speed=30)))

    compiled = CompiledCyclingData()

    compiled.add(cycling_session_1)
    assert compiled.total_distance == 10
    assert compiled.total_moving_time == 20
    assert compiled.average_speed == .5
    assert compiled.max_speed == 30

    compiled.add(cycling_session_2)
    assert compiled.total_distance == 20
    assert compiled.total_moving_time == 40
    assert compiled.average_speed == .5
    assert compiled.max_speed == 30


def test_add_it_update_max_speed_only_if_new_session_is_higher():
    cycling_session_1 = Mock(summary=Mock(return_value=NonCallableMock(distance=10, moving_time=20, average_speed=.5, max_speed=30)))
    cycling_session_2 = Mock(summary=Mock(return_value=NonCallableMock(distance=10, moving_time=20, average_speed=.5, max_speed=50)))

    compiled = CompiledCyclingData()
    compiled.max_speed = 40

    compiled.add(cycling_session_1)
    assert compiled.max_speed == 40

    compiled.add(cycling_session_2)
    assert compiled.max_speed == 50
