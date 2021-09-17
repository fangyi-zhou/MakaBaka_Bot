import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from bot_token import TOKEN

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def reply_text(text):
    def reply_func(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    return reply_func


goodnight_handler = MessageHandler(
    Filters.regex("^晚安.*") | Filters.regex(".*晚安$"), reply_text("晚安玛卡巴卡")
)
hughug_handler = MessageHandler(
    Filters.regex("哭哭") | Filters.regex("呜呜") | Filters.regex("要抱抱"),
    reply_text("抱抱玛卡巴卡"),
)
dispatcher.add_handler(goodnight_handler)
dispatcher.add_handler(hughug_handler)

updater.start_polling()
