import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 ALPHA Music Bot\n\n"
        "Welcome! 🤖\n"
        "Voice Chat Music System is ready.\n\n"
        "Use /help to see commands."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎧 ALPHA Music Commands\n\n"
        "/play - Play music\n"
        "/pause - Pause music\n"
        "/resume - Resume music\n"
        "/skip - Skip track\n"
        "/stop - Stop music\n"
        "/queue - Show queue"
    )

def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is not configured.")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("ALPHA Music Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
