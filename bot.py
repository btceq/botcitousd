import os
import requests
from telegram.ext import Application, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")

API_URL = "https://s3.amazonaws.com/dolartoday/data.json"

async def start(update, context):
    await update.message.reply_text(
        "¡Hola! Soy tu bot conversor de USDT a VES.\n"
        "Usa /usdtav <cantidad> para convertir de USDT a bolívares.\n"
        "Usa /vesusdt <cantidad> para convertir de VES a USDT."
    )

async def usdtav(update, context):
    try:
        cantidad = float(context.args[0]) if context.args else 1
        response = requests.get(API_URL)
        tasa = response.json()["USD"]["promedio"]
        resultado = cantidad * tasa
        await update.message.reply_text(f"{cantidad} USDT equivale a {resultado:.2f} VES")
    except Exception as e:
        await update.message.reply_text("Error al obtener la tasa o valor inválido.")

async def vesusdt(update, context):
    try:
        cantidad = float(context.args[0]) if context.args else 1
        response = requests.get(API_URL)
        tasa = response.json()["USD"]["promedio"]
        resultado = cantidad / tasa
        await update.message.reply_text(f"{cantidad} VES equivale a {resultado:.2f} USDT")
    except Exception as e:
        await update.message.reply_text("Error al obtener la tasa o valor inválido.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("usdtav", usdtav))
    app.add_handler(CommandHandler("vesusdt", vesusdt))
    print("Bot activo...")
    app.run_polling()

if __name__ == "__main__":
    main()