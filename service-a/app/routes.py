from fastapi import APIRouter, FastAPI
import service
import requests
app = FastAPI()
router = APIRouter()


@router.post("/post_to_redit/{ip}")
async def read_users(ip: str):
    result  = service.getting_location_by_ip(ip=ip)
    url = "http://localhost:3036/post_to_redit" #only exampel
    send = requests.post(url=url, json=result ,timeout=3)
    return send.status_code.as_integer_ratio()


app.include_router(router)