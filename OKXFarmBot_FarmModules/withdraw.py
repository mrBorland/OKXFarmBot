import requests
import time
import hmac
import hashlib
import json

API_KEY = '8ce4bd62-9328-495e-9556-2bf1107b3ac2'
API_SECRET = b'AB2C36344430A6080F3C5645155074B3'
PASSPHRASE = 'Slipknot221989@'

def get_okx_time():
    r = requests.get("https://www.okx.com/api/v5/public/time")
    return str(int(r.json()["data"][0]["ts"]))

def generate_signature(timestamp, method, request_path, body):
    message = f'{timestamp}{method}{request_path}{body}'
    return hmac.new(API_SECRET, message.encode('utf-8'), hashlib.sha256).hexdigest()

def auto_withdraw():
    url = "https://www.okx.com/api/v5/asset/withdrawal"
    amount = "2.00"
    timestamp = get_okx_time()

    body = {
        "ccy": "USDT",
        "amt": amount,
        "dest": "4",
        "toAddr": "TTb8QfyLAsXtTyZZ1SZ1CUZt6HGPfJb3Wo",
        "chain": "USDT-TRC20"
    }

    body_str = json.dumps(body)

    headers = {
        "OK-ACCESS-KEY": API_KEY,
        "OK-ACCESS-SIGN": generate_signature(timestamp, "POST", "/api/v5/asset/withdrawal", body_str),
        "OK-ACCESS-TIMESTAMP": timestamp,
        "OK-ACCESS-PASSPHRASE": PASSPHRASE,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=body, headers=headers)
    print("Результат виводу:", response.json())

auto_withdraw()
