from py3xui import Api
from dotenv import load_dotenv
import os

load_dotenv()

XUI_HOST = os.getenv('URL')
XUI_USERNAME = os.getenv('LOGIN')
XUI_PASSWORD = os.getenv('PASSWORD')
EXTERNAL_IP = os.getenv('IP_SERVER')
INBOUND_ID = int(os.getenv('INBOUND_ID'))
SUB_PORT = os.getenv('SUB_PORT')

async def checkclient(USER_EMAIL):
    api = Api(XUI_HOST, XUI_USERNAME, XUI_PASSWORD)
    api.login()

    def get_client_by_email(email):
        inbounds = api.inbound.get_list()

        for inbound in inbounds:
            if hasattr(inbound, 'settings') and hasattr(inbound.settings, 'clients') and (inbound.id == INBOUND_ID):
                for client in inbound.settings.clients:
                    if client.email == email:
                        return client, inbound
        return None, None


    client, inbound = get_client_by_email(USER_EMAIL)
    if client and inbound:
        return f"https://{EXTERNAL_IP}:{SUB_PORT}/sub/{client.sub_id}"
    else:
        return None