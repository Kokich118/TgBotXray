import os
import uuid
from py3xui import Api, Client
from dotenv import load_dotenv

load_dotenv()

XUI_URL = os.getenv('URL')
XUI_USERNAME = os.getenv('LOGIN')
XUI_PASSWORD = os.getenv('PASSWORD')
inbound_id = int(os.getenv('INBOUND_ID'))

def delete_client(telegram_name):
    api = Api(XUI_URL, XUI_USERNAME, XUI_PASSWORD)
    api.login()

    client = api.client.get_by_email(telegram_name)
    api.client.delete(inbound_id, client.uuid)