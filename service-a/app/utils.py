from shared import models
from pydantic import ValidationError


def check_ip(ip: str):
    try:
        the_ip = models.Ip(my_ip=ip)
        return {'succeeded': True}
    except ValidationError as e:
        return {'message': str(e), 'succeeded': False}
    


def check_coordinate(latitude, longitude):
    try:
        coordinate = models.Location(coordinate=(latitude, longitude))
        return {'latitude': coordinate.coordinate.latitude, 'longitude':coordinate.coordinate.longitude, 'succeeded': True} 
    except ValidationError as e:
        return {'message': str(e),'succeeded': False} 