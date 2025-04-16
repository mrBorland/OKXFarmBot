import subprocess import time from telegram import Update from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes from okx.Account import Account

TOKEN = "7626770291:AAG3UC1h3vt1aR9h0ALAgq3oo9RlvsMGSzI" ALLOWED_CHAT_ID = 6821675571

api_key = "8ce4bd62-9328-495e-9556-2bf1107b3ac2" secret_key = "AB2C36344430A6080F3C5645155074B3" passphrase = "Slipknot221989@"

accountAPI = Account( api_key=api_key, api_secret_key=secret_key, passphrase=passphrase, use_server_time=False, flag='0' )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): if update.effective_chat.id != ALLOWED_CHAT_ID: return await update.message.reply_text("OKXFarmBot: Привіт, Тоні! Я готовий до команд.")

async def farm(update: Update, context: ContextTypes.DEFAULT_TYPE): if update.effective_chat.id != ALLOWED_CHAT_ID: return subprocess.Popen(["python3", "main.py"]) await update.message.reply_text("Фарм запущено!")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE): if update.effective_chat.id != ALLOWED_CHAT_ID: return await update.message.reply_text("Бот працює, все добре!")

async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE): if update.effective_chat.id != ALLOWED_CHAT_ID: return await update.message.reply_text("Виведення буде реалізовано найближчим часом.")

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE): if update.effective_chat.id != ALLOWED_CHAT_ID: return try: balance = accountAPI.get_account_balance("USDT") usdt = balance['data'][0]['details'][0]['cashBal'] await update.message.reply_text(f"Баланс USDT: {usdt}") except Exception as e: await update.message.reply_text(f"Помилка: {e}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start)) app.add_handler(CommandHandler("farm", farm)) app.add_handler(CommandHandler("status", status)) app.add_handler(CommandHandler("withdraw", withdraw)) app.add_handler(CommandHandler("balance", balance))

app.run_polling()
