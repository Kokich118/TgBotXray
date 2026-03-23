import uuid
from py3xui import Api
from dotenv import load_dotenv
import os

load_dotenv("server.env")

# --- Настройки сервера (замените на свои) ---
XUI_HOST = os.getenv('URL')      # Адрес панели
XUI_USERNAME = os.getenv('LOGIN')
XUI_PASSWORD = os.getenv('PASSWORD')
EXTERNAL_IP = os.getenv('IP_SERVER')               # Внешний IP или домен
SERVER_PORT = 25022                              # Порт сервера
USER_EMAIL = "2wuj6zqd"                # Email клиента
INBOUND_ID = 8                                 # ID inbound правила

# --- Подключение к API ---
api = Api(XUI_HOST, XUI_USERNAME, XUI_PASSWORD)
api.login()

# --- 1. Получаем inbound, чтобы извлечь настройки Reality ---
inbound = api.inbound.get_by_id(INBOUND_ID)

# --- 2. Извлекаем публичный ключ, SNI и shortId из настроек Reality ---
reality_settings = inbound.stream_settings.reality_settings.get("settings", {})
public_key = reality_settings.get("publicKey")
server_names = inbound.stream_settings.reality_settings.get("serverNames", [])
sni = server_names[0] if server_names else ""
short_ids = inbound.stream_settings.reality_settings.get("shortIds", [])
short_id = short_ids[0] if short_ids else ""

# --- 3. Получаем клиента по email и извлекаем его UUID ---
#    Важно: api.client.get_by_email() возвращает клиента с числовым ID,
#    а настоящий UUID хранится в inbound.settings.clients
client_from_inbound = None
for client in inbound.settings.clients:
    if client.email == USER_EMAIL:
        client_from_inbound = client
        break

if not client_from_inbound:
    raise ValueError(f"Клиент с email {USER_EMAIL} не найден")

user_uuid = client_from_inbound.id  # Это настоящий UUID клиента

# --- 4. Собираем строку подключения ---
#    Формат: vless://<UUID>@<сервер>:<порт>?параметры#<название>
connection_string = (
    f"vless://{user_uuid}@{EXTERNAL_IP}:{SERVER_PORT}"
    f"?type=tcp&security=reality&pbk={public_key}"
    f"&fp=chrome&sni={sni}&sid={short_id}&spx=%2F"
    f"#{USER_EMAIL}"
)

print(f"Строка подключения: {connection_string}")