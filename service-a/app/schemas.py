from pydantic.networks import IPvAnyAddress
from pydantic import BaseModel, ValidationError, Field
from pydantic_extra_types.coordinate import Coordinate 



class Ip(BaseModel):
    my_ip: IPvAnyAddress


class Location(BaseModel):
    coordinate: Coordinate


def check_ip(ip: str):
    try:
        the_ip = Ip(my_ip=ip)
        return the_ip.my_ip
    except ValidationError as e:
        return {'message': str(e)}
    


def check_coordinate(latitude, longitude):
    try:
        coordinate = Location(coordinate=(latitude, longitude))
        return {'latitude': coordinate.coordinate.latitude, 'longitude':coordinate.coordinate.longitude} 
    except ValidationError as e:
        return {'message': str(e)} 
    




