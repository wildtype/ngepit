from gdrive import GpxFiles
from cycling import CyclingSession, CompiledCyclingData
from dashboard import update_dashboard

def main(request):
    gpx_files = GpxFiles()
    compilation = CompiledCyclingData()

    for file in gpx_files:
        compilation.add(CyclingSession(file))

    update_dashboard(compilation)
