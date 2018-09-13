from gdrive import GpxFiles
from cycling import CyclingSession, CompiledCyclingData
from dashboard import update_gcs, generate_html

def main(request):
    gpx_files = GpxFiles()
    compilation = CompiledCyclingData()

    for file in gpx_files:
        compilation.add(CyclingSession(file))

    total_distance = round(compilation.total_distance/1000.0, 1)
    average_speed = round(compilation.average_speed * 3600/1000.0, 1)
    max_speed = round(compilation.max_speed * 3600/1000.0, 1)
    total_moving_time = round(compilation.total_moving_time/3600.0, 1)

    html = generate_html(total_distance, total_moving_time, max_speed, average_speed)
    update_gcs(html)
