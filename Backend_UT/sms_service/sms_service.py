from dotenv import load_dotenv
import os
from ippanel import Client

load_dotenv()

API_KEY = os.getenv('API_KEY')
SENDER = os.getenv('SENDER')
sms = Client(API_KEY)


APPROVE_REQUEST_PATTERN = os.getenv('APPROVE_REQUEST_PATTERN')
DENY_REQUEST_PATTERN = os.getenv('DENY_REQUEST_PATTERN')

VERIFICATION_PATTERN = os.getenv('VERIFICATION_PATTERN')
FORGET_PASSWORD_PATTERN = os.getenv('FORGET_PASSWORD_PATTERN')

APPROVE_ADD_SUBJECT_PATTERN = os.getenv('APPROVE_ADD_SUBJECT_PATTERN')
DENY_ADD_SUBJECT_PATTERN = os.getenv('DENY_ADD_SUBJECT_PATTERN')

APPROVE_ADD_UNI_PATTERN = os.getenv('APPROVE_ADD_UNI_PATTERN')
DENY_ADD_UNI_PATTERN = os.getenv('DENY_ADD_UNI_PATTERN')

APPROVE_ADD_TEACHER_PATTERN = os.getenv('APPROVE_ADD_TEACHER_PATTERN')
DENY_ADD_TEACHER_PATTERN = os.getenv('DENY_ADD_TEACHER_PATTERN')



def get_sms_service():
    sms_service = sms
    try:
        yield sms_service
    finally:
        pass