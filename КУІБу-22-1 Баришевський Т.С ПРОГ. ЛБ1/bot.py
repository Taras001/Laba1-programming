from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    commands = """
    Привіт! Команди:
/menu - меню 
/whisper - "Тихий"
/scream - "Гучний"
    """
    await update.message.reply_text(commands)
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    commands = """
    Команди:
/menu - меню 
/whisper - "Тихий"
/scream - "Гучний"
    """
    await update.message.reply_text(commands)
async def whisper(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Тихий")
async def scream(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Гучний")


def main():
    token = 'bot_token_from_BotFather'
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("whisper", whisper))
    app.add_handler(CommandHandler("scream", scream))
    print("Бот працює")
    app.run_polling()
if __name__ == "__main__":
    main()