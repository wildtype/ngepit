import gpxpy
from collections import namedtuple

CyclingSessionSummary = namedtuple('CyclingSessionSummary', ['distance', 'moving_time', 'average_speed', 'max_speed', 'total_uphill', 'total_downhill'])

class CyclingSession:
    '''Per-session/gpx file data'''

    def __init__(self, gpx_file):
        self.gpx_file = gpx_file
        self.gpx_data = gpxpy.parse(self.gpx_file)

    def summary(self):
        moving_data = self.gpx_data.get_moving_data()

        distance = moving_data.moving_distance
        moving_time = moving_data.moving_time
        average_speed = distance/moving_time
        max_speed = moving_data.max_speed

        return CyclingSessionSummary(distance=distance, moving_time=moving_time, average_speed=average_speed, max_speed=max_speed, total_uphill=0, total_downhill=0)

