import redis
import os


REDIS_HOST = os.getenv("REDIS_HOST", "localhost")

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=6379,
    decode_responses=True
)

def save_coordinates(data):
    key = f"ip:{data.ip}"
    value = {
        "latitude": data.latitude,
        "longitude": data.longitude
    }
    redis_client.hset(key, mapping=value)


def get_all_coordinates():
    results = []

    keys = redis_client.keys("ip:*")

    for key in keys:
        data = redis_client.hgetall(key)

        results.append({
            "ip": key.replace("ip:", ""),
            "latitude": float(data.get("latitude")),
            "longitude": float(data.get("longitude"))
        })

    return results
















