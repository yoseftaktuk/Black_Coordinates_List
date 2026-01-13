import requests
from requests import HTTPError
import schemas
BASEURL = 'http://api2:8000'

def getting_location_by_ip(ip: str):
    try:
        response = requests.get(f'''http://ip-api.com/json/{ip}''')
        result = response.json()
        check = schemas.check_coordinate(result['lat'], result['lon'])
        if check['bool']:
            return {'ip': result['query'], 'longitude':result['lon'], 'latitude':  result['lat']}
        return check['message']
    except HTTPError as e:
        return {'message': str(e)}


def send_to_service_b(data: dict):
    try:
        url = f'{BASEURL}/coordinates'
        send = requests.post(url=url, json=data ,timeout=3)
        return send.json()
    except HTTPError as e:
        return {'message': str(e)}
    
def get_all():
    url = f'{BASEURL}/coordinates'
    try:
        result = requests.get(url=url, timeout=3)
        return {'result': result.json(), "bool": True}    
    except HTTPError as e:
        return {'message': str(e), 'bool': False}    