from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

API_TOKEN = "7905959493:AAGhBqJjM-qtEeSUbBiROA-bDGAzX9_lNnw"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send /getowner <@channelusername> to get creator info.")

async def get_owner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗ Use format: /getowner @channelusername")
        return

    channel_username = context.args[0]
    try:
        chat = await context.bot.get_chat(channel_username)
        admins = await context.bot.get_chat_administrators(chat.id)

        text = f"📢 Channel: {chat.title}\n🆔 ID: `{chat.id}`\n\n"
        owner = None

        for admin in admins:
            if admin.status == 'creator':
                owner = admin.user
                text += "👑 Owner:\n"
                text += f"• Name: {owner.full_name}\n"
                text += f"• Username: @{owner.username}\n" if owner.username else ""
                text += f"• ID: `{owner.id}`\n"
                break

        if not owner:
            text += "❗ Owner info not available (might be private)."

        await update.message.reply_text(text, parse_mode="Markdown")
    except Exception as e:
        logger.error(f"Error: {e}")
        await update.message.reply_text("❌ Error: Invalid or inaccessible channel/group.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(API_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("getowner", get_owner))

    app.run_polling()