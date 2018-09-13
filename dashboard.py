from google.cloud import storage
import datetime
import pytz

def generate_html(total_distance=0, total_moving_time=0, max_speed=0, average_speed=0):
    css = '''*{margin:0;padding:0;outline:0;font-size:1em;font-weight:400;font-style:normal;border:0;text-decoration:none;list-style-type:none}body{font:16px/1.4 monospace}.stats{max-width:640px;margin:1em}.stats__title{font-weight:700;font-size:1.4em}.separator{margin-top:.6em;margin-bottom:.6em}.stats__info{font-size:.7em;color:#555}'''

    html_template = '''<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><title>My Cycling Stats</title><style>{css}</style></head><body><div class="stats"><h1 class="stats__title">My Cycling Stats</h1><p class="stats__info">last updated: {last_updated}</p><p class="separator">=====</p><p class="stats__metric">Total distance: <span class="stats__metric-value stats__total-distance">{total_distance} km</span></p><p class="stats__metric">Average speed: <span class="stats__metric-value stats__average-speed">{avg_speed} km/h</span></p><p class="stats__metric">Maximum speed: <span class="stats__metric-value stats__max-speed">{max_speed} km/h</span></p><p class="stats__metric">Total moving time: <span class="stats__metric-value stats__total-moving-time">{total_moving_time} hours</span></p><p class="stats__credit" style="font-size: .8em;margin-top: 1em;"><a href="https://github.com/wildtype/ngepit" style="color: #888;">source code</a></p></div></body></html>'''

    last_updated = datetime.datetime.now().astimezone(pytz.timezone('Asia/Jakarta')).strftime('%d %b %Y, %H:%M')

    return html_template.format(css=css, last_updated=last_updated, total_distance=total_distance, avg_speed=average_speed, max_speed=max_speed, total_moving_time=total_moving_time)

def update_gcs(html):
    client = storage.Client()
    bucket = client.get_bucket('cycling.prehistoric.me')
    blob = bucket.blob('index.html')
    blob.upload_from_string(html, content_type='text/html')

