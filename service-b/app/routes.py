from fastapi import APIRouter

router = APIRouter()

@router.post("/coordinates")
def receive_coordinates(data: dict):
    send_data = data

    return {"status": "received"}
