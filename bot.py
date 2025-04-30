import os
from telegram.ext import Application, CommandHandler
import requests

TOKEN = os.getenv("BOT_TOKEN")  # Usa variable de entorno
API_URL = "https://s3.amazonaws.com/dolartoday/data.json"

async def usdtav(update, context):
    try:
        cantidad = float(context.args[0]) if context.args else 1
        response = requests.get(API_URL)
        tasa = response.json()["USD"]["promedio"]
        resultado = cantidad * tasa
        await update.message.reply_text(f"{cantidad} USDT equivale a {resultado:.2f} VES")
    except Exception as e:
        await update.message.reply_text("Error al obtener la tasa o valor inválido.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("usdtav", usdtav))
    print("Bot activo...")
    app.run_polling()

if __name__ == "__main__":
    main()