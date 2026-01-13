from fastapi import APIRouter, FastAPI, HTTPException
import service
import requests
from requests import HTTPError 
app = FastAPI()
router = APIRouter()


@router.post("/post_to_redit/{ip}")
def read_users(ip: str):
    result  = service.getting_location_by_ip(ip=ip)
    send = service.send_to_service_b(result)
    return send

