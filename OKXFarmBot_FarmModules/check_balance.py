import requests
import time
import hmac
import hashlib

API_KEY = '8ce4bd62-9328-495e-9556-2bf1107b3ac2'
API_SECRET = b'AB2C36344430A6080F3C5645155074B3'
PASSPHRASE = 'Slipknot221989@'

def generate_signature(timestamp, method, request_path, body):
    message = f'{timestamp}{method}{request_path}{body}'
    return hmac.new(API_SECRET, message.encode('utf-8'), hashlib.sha256).hexdigest()

def check_balance():
    url = "https://www.okx.com/api/v5/account/balance?ccy=USDT"
    timestamp = str(time.time())
    
    headers = {
        "OK-ACCESS-KEY": API_KEY,
        "OK-ACCESS-SIGN": generate_signature(timestamp, "GET", "/api/v5/account/balance?ccy=USDT", ""),
        "OK-ACCESS-TIMESTAMP": timestamp,
        "OK-ACCESS-PASSPHRASE": PASSPHRASE,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    print("Результат балансу:", response.json())

check_balance()
