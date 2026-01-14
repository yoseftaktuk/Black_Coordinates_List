from fastapi import APIRouter
from shared.models import Coordinates 
from storage import save_coordinates,get_all_coordinates


router = APIRouter()


@router.post("/coordinates")
def receive_coordinates(data:Coordinates):
    save_coordinates(data)
    return {"status": "received"}



@router.get("/coordinates")
def get_coordinates():
    all_coordinates = get_all_coordinates()
    return all_coordinates

