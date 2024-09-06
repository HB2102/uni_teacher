from redis import Redis
from dotenv import load_dotenv
import os


load_dotenv()

REDIS_URL = os.getenv('REDIS_URL')

redis_connection = Redis.from_url(REDIS_URL)


def get_redis():
    redis_db = redis_connection
    try:
        yield redis_db
    finally:
        redis_db.close()