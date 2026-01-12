import requests
from requests import HTTPError


def getting_location_by_ip(ip: str):
    try:
        response = requests.get(f'''http://ip-api.com/json/{ip}''')
        result = response.json()
        return(result) 
    except HTTPError as e:
        raise str(e)


