import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from bot_token import TOKEN

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="玛卡巴卡")


def goodnight(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="晚安玛卡巴卡")

start_handler = CommandHandler("start", start)
goodnight_handler = MessageHandler(Filters.regex("^晚安.*") |
                                   Filters.regex(".*晚安$"), goodnight)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(goodnight_handler)

updater.start_polling()
