import os
import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram.constants import ChatAction

# logs
logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN manquant !")

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

# buttons handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # 📋 menu
    if query.data == "menu":
        keyboard = [
            [InlineKeyboardButton("🔥 خدمات", callback_data="services")],
            [InlineKeyboardButton("📞 تواصل", callback_data="contact")],
            [InlineKeyboardButton("🔙 رجوع", callback_data="back")]
        ]
        await query.edit_message_text(
            "📋 القائمة:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # 🔥 services
    elif query.data == "services":
        await query.edit_message_text("🔥 نقدم خدمات رائعة 😎")

    # 📞 contact
    elif query.data == "contact":
        await query.answer()

        await query.message.reply_text("يرجى الانتظار من فضلك حتى تصل الرسالة الى المديرة ⏳")

        # typing animation
        for _ in range(5):
            await context.bot.send_chat_action(
                chat_id=query.message.chat_id,
                action=ChatAction.TYPING
            )
            await asyncio.sleep(1)

        # bouton final
        keyboard = [
            [InlineKeyboardButton("🔥🔥 تواصل معي حبيبي انا لايف هنا 🍑👄 🔥🔥", url="https://sprlv.link/svy8zi6d")]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.message.reply_text("ㅤ", reply_markup=reply_markup)

    # ℹ️ help
    elif query.data == "help":
        await query.edit_message_text("ℹ️ كيف يمكنني مساعدتك؟")

    # 💬 talk
    elif query.data == "talk":
        await query.answer()

        await query.message.reply_text("يرجى الانتظار من فضلك حتى تصل الرسالة الى المديرة ⏳")

        # typing animation
        for _ in range(5):
            await context.bot.send_chat_action(
                chat_id=query.message.chat_id,
                action=ChatAction.TYPING
            )
            await asyncio.sleep(1)

        keyboard = [
            [InlineKeyboardButton("🔥🔥 تواصل معي حبيبي انا لايف هنا 🍑👄 🔥🔥", url="https://sprlv.link/svy8zi6d")]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.message.reply_text("ㅤ", reply_markup=reply_markup)

    # 🔙 back
    elif query.data == "back":
        keyboard = [
            [InlineKeyboardButton("📋 القائمة", callback_data="menu")],
            [InlineKeyboardButton("ℹ️ مساعدة", callback_data="help")]
        ]

        await query.edit_message_text(
            "🔙 رجعنا:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

# run bot
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot running 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()
