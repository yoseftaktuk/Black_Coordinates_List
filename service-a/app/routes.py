from fastapi import APIRouter, FastAPI, HTTPException
import service
from shared import models

app = FastAPI()
router = APIRouter()


@router.post("/post_to_redit/{ip}")

def read_users(ip: str):
    check = models.check_ip(ip)#Checks that the IP is correct.
    if check['bool']:
        try:
            result  = service.getting_location_by_ip(ip=ip)#Sends a get request to get location by IP
            send = service.send_to_service_b(result)#Sends a post request to  api server to save in redis
            return send
        except HTTPException as e:
            return {'message': str(e)}
    return {'masseges': check['message'][:75]}    

@router.get('/get_all')
def get_all_items():
    result = service.get_all()
    if result['bool']:
        return result['result']
    return result['bool']
    

