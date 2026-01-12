from pydantic import BaseModel

class Coordinates(BaseModel):
    ip: str
    latitude: float
    longitude: float
