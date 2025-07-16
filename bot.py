from fastapi import FastAPI, Request
import os
import requests

app = FastAPI()

# ✅ Hardcoded for your test
TELEGRAM_BOT_TOKEN = "7810201020:AAHz9e1I93UkpYrefVOnypiDk6EEAJZHGjY"
WEBHOOK_URL = "https://0bc030f04ad4.ngrok-free.app/webhook"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

@app.get("/")
def root():
    return {"message": "Bot is alive!"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("📬 Got update from Telegram:", data)  # ✅ DEBUG

    if "message" not in data:
        print("⚠️ No 'message' in update.")
        return {"ok": False}

    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    if text == "/start":
        reply = "Hi! I am your upgraded bot."
    elif text == "/trend":
        reply = "Today's trend is oversized blazers with denim!"
    else:
        reply = f"You said: {text}"

    send_message(chat_id, reply)
    return {"ok": True}

def send_message(chat_id, text):
    response = requests.post(
        f"{TELEGRAM_API_URL}/sendMessage",
        json={"chat_id": chat_id, "text": text}
    )
    print("📤 Telegram API response:", response.status_code, response.text)  # ✅ DEBUG
