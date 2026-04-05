import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name

    keyboard = [
        [InlineKeyboardButton("📋 القائمة", callback_data="menu")],
        [InlineKeyboardButton("ℹ️ مساعدة", callback_data="help")],
        [InlineKeyboardButton("💬 تحدث", callback_data="talk")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"مرحبا {name} 👋\nاختار من هنا 👇",
        reply_markup=reply_markup
    )

# التعامل مع الضغط على الأزرار
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "menu":
        keyboard = [
            [InlineKeyboardButton("🔥 خدمات", callback_data="services")],
            [InlineKeyboardButton("📞 تواصل", callback_data="contact")],
            [InlineKeyboardButton("🔙 رجوع", callback_data="back")]
        ]
        await query.edit_message_text("📋 القائمة:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "services":
        await query.edit_message_text("🔥 نقدم خدمات رائعة 😎")

    elif query.data == "contact":
        await query.edit_message_text("📞 تواصل معنا عبر واتساب")

    elif query.data == "help":
        await query.edit_message_text("ℹ️ كيف يمكنني مساعدتك؟")

    elif query.data == "talk":
       await query.answer()
       await query.message.reply_text("يرجى الانتظار من فضلك حتى تصل الرسالة الى المديرة ⏳")

    elif query.data == "back":
        keyboard = [
            [InlineKeyboardButton("📋 القائمة", callback_data="menu")],
            [InlineKeyboardButton("ℹ️ مساعدة", callback_data="help")]
        ]
        await query.edit_message_text("🔙 رجعنا:", reply_markup=InlineKeyboardMarkup(keyboard))

# تشغيل البوت
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot Inline Buttons 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()
