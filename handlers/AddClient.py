import os
import uuid
from py3xui import Api, Client
from dotenv import load_dotenv

load_dotenv()

# --- Настройки сервера
XUI_URL = os.getenv('URL')
XUI_USERNAME = os.getenv('LOGIN')
XUI_PASSWORD = os.getenv('PASSWORD')

print(XUI_USERNAME)

# --- Подключение к API ---
api = Api(XUI_URL, XUI_USERNAME, XUI_PASSWORD)
api.login()

# 2. Получаем список всех inbound-правил
inbounds = api.inbound.get_list()

inbound_id = 8

# Создаем нового клиента
new_client = Client(
    id=str(uuid.uuid4()),  # Генерируем уникальный UUID для клиента
    email="Test",
    enable=True,
    total_gb= 0,
    expiry_time=0  # 0 означает "без срока годности"
)

# Добавляем клиента на панель
api.client.add(inbound_id, [new_client])
print(f"Клиент {new_client.email} успешно добавлен в inbound {inbound_id}")