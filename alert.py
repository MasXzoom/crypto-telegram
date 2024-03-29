import os
import logging
import requests
import json
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackContext
from dotenv import load_dotenv

# Load configuration from .env file
load_dotenv()

# Configuration
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
CRYPTO_SYMBOLS = os.getenv('CRYPTO_SYMBOLS').split(',')
API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=usd'
ALERT_THRESHOLD = 1  # Set threshold to 1% for both increase and decrease
MONITORING_INTERVAL = 120  # Check every 2 minutes
PRICES_FILE = 'previous_prices.json'  # Store previous prices here

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def fetch_crypto_price(symbol):
    try:
        response = requests.get(API_URL.format(symbol))
        response.raise_for_status()
        data = response.json()
        return data[symbol]['usd']
    except requests.RequestException as e:
        logging.error(f"Error fetching price for {symbol}: {e}")
        return None

def load_prices():
    try:
        with open(PRICES_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_prices(prices):
    with open(PRICES_FILE, 'w') as file:
        json.dump(prices, file)

def generate_message(symbol, change_percent, current_price):
    direction = "naik" if change_percent > 0 else "turun"
    sign = "+" if change_percent > 0 else ""
    return f"Harga {symbol.upper()} {direction}: {sign}{change_percent:.2f}% menjadi ${current_price}."

async def check_prices(context: CallbackContext):
    previous_prices = load_prices()
    
    for symbol in CRYPTO_SYMBOLS:
        current_price = fetch_crypto_price(symbol)
        if current_price is None:
            continue
        previous_price = previous_prices.get(symbol, current_price)
        change_percent = (current_price - previous_price) / previous_price * 100 if previous_price else 0

        if abs(change_percent) >= ALERT_THRESHOLD:
            message = generate_message(symbol, change_percent, current_price)
            await context.bot.send_message(chat_id=CHAT_ID, text=message)
        
        previous_prices[symbol] = current_price

    save_prices(previous_prices)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Bot pemantau harga kripto siap.")

def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    job_context = {'previous_prices': {}}
    application.job_queue.run_repeating(check_prices, interval=MONITORING_INTERVAL, first=0, data=job_context)

    application.run_polling()

if __name__ == '__main__':
    main()
