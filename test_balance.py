from okx.Account import Account
import json
import traceback

api_key = "8ce4bd62-9328-495e-9556-2bf1107b3ac2"
secret_key = "AB2C36344430A6080F3C5645155074B3"
passphrase = "Slipknot221989@"

accountAPI = Account(
    api_key=api_key,
    api_secret_key=secret_key,
    passphrase=passphrase,
    use_server_time=True,
    flag='0'
)

try:
    print("Отримую баланс...")
    balance = accountAPI.get_account_balance("USDT")
    print("Відповідь OKX:")
    print(json.dumps(balance, indent=2, ensure_ascii=False))
except Exception as e:
    print("Помилка:")
    traceback.print_exc()
