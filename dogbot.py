from telegram.ext import Updater, CommandHandler
import requests
import re

TOKEN = '1026813***************'


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


url = get_url()


def bop(bot, update):
    url = get_url()
    chat_id = -1234567
    bot.send_photo(chat_id=chat_id, photo=url)


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
