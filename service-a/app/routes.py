from fastapi import APIRouter, FastAPI, HTTPException
import service
import utils

app = FastAPI()
router = APIRouter()
service_manager = service.Service()

@router.post("/post_to_redit/{ip}")

def read_users(ip: str):
    check = utils.check_ip(ip)#Checks that the IP is correct.
    if check['succeeded']:
        try:
            result  = service_manager.getting_location_by_ip(ip=ip)#Sends a get request to get location by IP
            send = service_manager.send_to_service_b(result)#Sends a post request to  api server to save in redis
            return send
        except HTTPException as e:
            return {'message': str(e)}
    return {'masseges': check['message'][:75]}    

@router.get('/get_all')
def get_all_items():
    result = service_manager.get_all()
    if result['succeeded']:
        return result['result']
    return result['succeeded']
    

