import os
import requests

def update_total_distance(compiled_data):
    base_url = os.environ['DASHBOARD_HOST']
    auth_token = os.environ['AUTH_TOKEN']

    data = {
        'current': round(compiled_data.total_distance/1000.0, 1),
        'auth_token': auth_token
    }
    requests.post('{}/widgets/total_distance'.format(base_url), json=data)

def update_average_speed(compiled_data):
    base_url = os.environ['DASHBOARD_HOST']
    auth_token = os.environ['AUTH_TOKEN']

    data = {
        'current': round(compiled_data.average_speed * 3600/1000.0, 1),
        'auth_token': auth_token
    }
    requests.post('{}/widgets/average_speed'.format(base_url), json=data)

def update_max_speed(compiled_data):
    base_url = os.environ['DASHBOARD_HOST']
    auth_token = os.environ['AUTH_TOKEN']

    data = {
        'current': round(compiled_data.max_speed * 3600/1000.0, 1),
        'auth_token': auth_token
    }
    requests.post('{}/widgets/maximum_speed'.format(base_url), json=data)

def update_total_moving_time(compiled_data):
    base_url = os.environ['DASHBOARD_HOST']
    auth_token = os.environ['AUTH_TOKEN']

    data = {
        'current': round(compiled_data.total_moving_time/3600.0, 1),
        'auth_token': auth_token
    }
    requests.post('{}/widgets/total_moving_time'.format(base_url), json=data)

def update_dashboard(compiled_data):
    update_total_distance(compiled_data)
    update_total_moving_time(compiled_data)
    update_max_speed(compiled_data)
    update_average_speed(compiled_data)
