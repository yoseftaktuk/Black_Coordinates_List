from pydantic.networks import IPvAnyAddress
from pydantic import BaseModel, ValidationError, Field
from pydantic_extra_types.coordinate import Coordinate 



class Ip(BaseModel):
    my_ip: IPvAnyAddress


class Location(BaseModel):
    coordinate: Coordinate

    
class Coordinates(BaseModel):
    ip: str
    latitude: float
    longitude: float