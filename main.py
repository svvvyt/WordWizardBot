import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from dict_api_requests import get_word
from phrases import phrases



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=phrases["start"])

async def learn_words(update: Update, context: ContextTypes.DEFAULT_TYPE):
    word = get_word()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=word)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=phrases["unknown"])


if __name__ == '__main__':
    application = ApplicationBuilder().token('6476987073:AAHY851LIedcHRw3TUtR0u--E5GV-fGnMHI').build()

    start_handler = CommandHandler('start', start)
    learn_words_handler = CommandHandler('learn_words', learn_words)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    application.add_handler(start_handler)
    application.add_handler(learn_words_handler)
    application.add_handler(unknown_handler)

    application.run_polling()
