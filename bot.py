import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import re

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Your bot token here
BOT_TOKEN = "7905959493:AAGhBqJjM-qtEeSUbBiROA-bDGAzX9_lNnw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me any public Telegram channel link to try to get owner ID (if possible).")

async def get_owner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    match = re.search(r'(https://t.me/[\w_]+)', text)

    if match:
        channel_url = match.group(1)

        try:
            # Dummy logic, real way to get owner ID from public channel isn't directly allowed via bot API
            await update.message.reply_text(f"Sorry, can't get owner ID from {channel_url} due to Telegram restrictions.")
        except Exception as e:
            await update.message.reply_text("Error: " + str(e))
    else:
        await update.message.reply_text("Please send a valid Telegram channel link (e.g., https://t.me/example_channel)")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("owner", get_owner))
    app.add_handler(CommandHandler("get", get_owner))
    app.add_handler(CommandHandler("id", get_owner))
    app.add_handler(CommandHandler("check", get_owner))
    app.add_handler(CommandHandler("whois", get_owner))

    app.run_polling()

if __name__ == '__main__':
    main()