import os
from dotenv import load_dotenv

# ✅ Full absolute path to .env
dotenv_path = "/Users/dushyant/Desktop/telegram bot/.env"

load_dotenv(dotenv_path=dotenv_path)

print("📢 DEBUG --- Checking .env loading...")
print("TELEGRAM_BOT_TOKEN =", os.getenv("TELEGRAM_BOT_TOKEN"))
print("WEBHOOK_URL =", os.getenv("WEBHOOK_URL"))
