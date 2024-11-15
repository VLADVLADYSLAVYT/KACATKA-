import base64
import json
import hashlib

# Ваші ключі з LiqPay
public_key = 'sandbox_i28524890692'
private_key = 'sandbox_N1zqYl44YbkLIpj73bEujO3kYSpdDiwMooSpyLAZ'

# Дані для платежу
liqpay_data = {
    "public_key": public_key,
    "version": "3",
    "action": "pay",
    "amount": "300",
    "currency": "UAH",
    "description": "Чашка Касатка",
    "order_id": "order_id_1"
}

# Перетворення даних у формат Base64
data_string = base64.b64encode(json.dumps(liqpay_data).encode()).decode()

# Генерація підпису
signature_string = private_key + data_string + private_key
signature = base64.b64encode(hashlib.sha1(signature_string.encode()).digest()).decode()

print("LIQPAY_DATA:", data_string)
print("LIQPAY_SIGNATURE:", signature)
