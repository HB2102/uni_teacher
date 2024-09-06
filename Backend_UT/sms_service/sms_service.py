from dotenv import load_dotenv
import os
from ippanel import Client

load_dotenv()

API_KEY = os.getenv('API_KEY')
SENDER = os.getenv('SENDER')
sms = Client(API_KEY)


def get_sms_service():
    sms_service = sms
    try:
        yield sms_service
    finally:
        pass