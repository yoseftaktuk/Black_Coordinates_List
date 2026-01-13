import requests
from requests import HTTPError
import schemas
BASEURL = 'http://192.168.20.179:8080'

def getting_location_by_ip(ip: str):
    try:
        response = requests.get(f'''http://ip-api.com/json/{ip}''')
        result = response.json()
        schemas.check_coordinate(result['lat'], result['lon'])
        return {'ip': result['query'], 'longitude':result['lon'], 'latitude':  result['lat']}
    except HTTPError as e:
        return {'message': str(e)}


def send_to_service_b(data: dict):
    try:
        url = f'{BASEURL}/coordinates'
        send = requests.post(url=url, json=data ,timeout=3)
        return send.json()
    except HTTPError as e:
        return {'message': str(e)}