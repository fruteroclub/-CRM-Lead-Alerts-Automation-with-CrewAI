#!/usr/bin/env python3
"""
Script para obtener el Topic ID de Telegram
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Get updates from the bot
url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
response = requests.get(url)
data = response.json()

print("🔍 Últimos mensajes recibidos por el bot:\n")

if data.get("ok") and data.get("result"):
    for update in data["result"][-5:]:  # Últimos 5 mensajes
        message = update.get("message", {})
        chat = message.get("chat", {})

        chat_id = chat.get("id")
        chat_title = chat.get("title", "Sin título")
        message_thread_id = message.get("message_thread_id")
        text = message.get("text", "")

        print(f"📱 Chat: {chat_title}")
        print(f"   Chat ID: {chat_id}")

        if message_thread_id:
            print(f"   🧵 Thread/Topic ID: {message_thread_id}")
            print(f"   ✅ TELEGRAM_GROUP_ID={chat_id}")
            print(f"   ✅ TELEGRAM_THREAD_ID={message_thread_id}")
        else:
            print(f"   ℹ️  No es un topic (mensaje en grupo principal)")

        print(f"   Texto: {text[:50]}...")
        print()
else:
    print("❌ No hay mensajes recientes. Envía un mensaje al bot en el topic.")
