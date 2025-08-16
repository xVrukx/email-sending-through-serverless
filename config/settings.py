import os
from dotenv import load_dotenv

load_dotenv()

Email_host = os.getenv('Email_host')
Email_port = int(os.getenv('Email_port',587))
Email_name = os.getenv('Email_name')
Email_password = os.getenv('Email_password')

try:
    if all([Email_name,Email_port,Email_host,Email_password]):
        print('All set no problem in getting the credentials')
    elif not all([Email_name,Email_port,Email_host,Email_password]):
        print('Error:error occored while getting the credentials')
except Exception as e:
    print(f'Error:faild in settings logic {e}')