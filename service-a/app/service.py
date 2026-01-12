import requests
from requests import HTTPError


def getting_location_by_ip(ip: str):
    try:
        new_result = {}
        response = requests.get(f'''http://ip-api.com/json/{ip}''')
        result = response.json()
        new_result['lat'] = result['lat']
        new_result['lon'] = result['lon']
        new_result['ip'] = result['query']
        return(new_result) 
    except HTTPError as e:
        raise str(e)


