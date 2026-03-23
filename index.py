import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv("server.env")

# Читаем переменные
bot_token = os.getenv('USER')
server_ip = os.getenv('IP_SERVER')
server_port = os.getenv('PORT')

print(f"Token: {bot_token}")
print(f"Server: {server_ip}:{server_port}")