from telegram import *
from telegram.ext import *

BOT_TOKEN = '5860575345:AAHAPeKHj_OXmHEFz83XX-pDFh_t0EcP9iQ'
BOT_USERNAME = 'kasunlearnbot1_bot'
GROUP_ID = '-1001957772502'
GROUP_NAME = 'learnbot1_group'


async def startCommand(update: Update, context: CallbackContext):
    await update.message.reply_text('Hey the bot is running!')

if __name__ == '__main__':
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', startCommand))

    print('Bot running!')
    app.run_polling(1)
