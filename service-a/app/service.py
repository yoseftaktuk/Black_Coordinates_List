import requests
from requests import HTTPError
import utils


class Service:
    def __init__(self):

        self.BASEURL = 'http://api2:8000'

    def getting_location_by_ip(self, ip: str):
        try:
            response = requests.get(f'''http://ip-api.com/json/{ip}''')
            result = response.json()
            check = utils.check_coordinate(result['lat'], result['lon'])#Checking that the coordinates are correct
            if check['bool']:
                return {'ip': result['query'], 'longitude':result['lon'], 'latitude':  result['lat']}
            return check['message']
        except HTTPError as e:
            return {'message': str(e)}

    def send_to_service_b(self, data: dict):
        try:
            url = f'{self.BASEURL}/coordinates'
            send = requests.post(url=url, json=data ,timeout=3)
            return send.json()
        except HTTPError as e:
            return {'message': str(e)}
        
    def get_all(self):
        """This function sends a get request to the server
        to retrieve all the stored information."""
        url = f'{self.BASEURL}/coordinates'
        try:
            result = requests.get(url=url, timeout=3)
            return {'result': result.json(), "succeeded": True}    
        except HTTPError as e:
            return {'message': str(e), 'succeeded': False}    