import os
import uuid
from py3xui import Api, Client

# Установите переменные окружения в вашей системе или в коде
os.environ["XUI_HOST"] = "https://169.40.4.70:17253/ZbG1wa6WHfYvSrQPzd"  # Адрес вашей панели
os.environ["XUI_USERNAME"] = "YcVLvRISvi"
os.environ["XUI_PASSWORD"] = "CToXAnhQQp"

# Создаем экземпляр API, данные подтянутся из переменных окружения
api = Api.from_env()

# 1. Выполняем вход (обязательный шаг)
api.login()

# 2. Получаем список всех inbound-правил
inbounds = api.inbound.get_list()

inbound_id = 8

# Создаем нового клиента
new_client = Client(
    id=str(uuid.uuid4()),  # Генерируем уникальный UUID для клиента
    email="Артем | Для ноута",
    enable=True,
    total_gb= 0,
    expiry_time=0  # 0 означает "без срока годности"
)

# Добавляем клиента на панель
api.client.add(inbound_id, [new_client])
print(f"Клиент {new_client.email} успешно добавлен в inbound {inbound_id}")