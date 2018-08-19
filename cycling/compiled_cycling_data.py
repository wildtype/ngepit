import gpxpy
from collections import namedtuple

class CompiledCyclingData:
    def __init__(self):
        self.total_distance = 0
        self.total_moving_time = 0
        self.average_speed = 0
        self.max_speed = 0

    def add(self, cycling_session):
        session_data = cycling_session.summary()

        self.total_distance += session_data.distance
        self.total_moving_time += session_data.moving_time
        self.average_speed = self.total_distance/self.total_moving_time

        if session_data.max_speed > self.max_speed:
            self.max_speed = session_data.max_speed
