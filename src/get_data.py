import requests
from datetime import datetime


def get_iss_location():
    location = requests.get('http://api.open-notify.org/iss-now.json')
    location_json = location.json()
    location_json['iss_position']['timestamp'] = datetime.now().strftime(format = '%Y%m%d_%H%M')
    return location_json['iss_position']

    