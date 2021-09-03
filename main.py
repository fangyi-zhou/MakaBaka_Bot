import logging

from telegram.ext import Updater, CommandHandler

from bot_token import TOKEN

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="玛卡巴卡")


start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

updater.start_polling()
