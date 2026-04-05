import os
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# logs (important pour Railway)
logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN manquant !")

# 🔘 boutons
keyboard = [
    ["📋 القائمة", "ℹ️ مساعدة"],
    ["💬 تحدث", "❌ خروج"]
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    message = f"مرحبا {name} 👋\nكيف حالك يا حبيبي 😘"
    await update.message.reply_text(message, reply_markup=reply_markup)

# messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📋 القائمة":
        reply = "هذه هي القائمة 😎"
    elif text == "ℹ️ مساعدة":
        reply = "كيف يمكنني مساعدتك؟"
    elif text == "💬 تحدث":
        reply = "أنا هنا للدردشة 😄"
    elif text == "❌ خروج":
        reply = "إلى اللقاء 👋"
    else:
        reply = "لم أفهم 🤔"

    await update.message.reply_text(reply)

# 🚀 lancement
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    print("Bot running 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()
