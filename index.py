from telegram import Update, ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '6789400457:AAHsI_kgWPXm7m3WLz-0vh_6Ve21yty5EBk'
YOUTUBE_CHANNEL_URL = "https://www.youtube.com/channel/UCFlixopro"  # Replace with your actual channel URL

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    chat_id = update.message.chat_id

    # Ensure the user has a username and handle missing values
    username = f"@{user.username}" if user.username else "N/A"
    full_name = f"{user.first_name} {user.last_name}".strip()

    message = (
        "┌───⭓ Telegram Chat Id\n"
        f"│» Name - {full_name}\n"
        f"│» Username - {username}\n"
        f"│» Chat id - <code>{chat_id}</code>\n"  # Use <code> to make the chat id copyable
        "│» Developed By - @nahidahmed01\n"
        f"│» YouTube Channel : <a href='{YOUTUBE_CHANNEL_URL}'>Flixopro</a>\n"
        "└─────────────────⧕"
    )

    await update.message.reply_text(message, parse_mode=ParseMode.HTML)

def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    application.run_polling()

if __name__ == '__main__':
    main()
  
