import requests
from telebot import *
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import webbrowser
import json
import random
TOKEN= '6165585308:AAFqLhFGa10yIc-4S0ktm_E3_oxqO8lBtto'



bot = TeleBot(TOKEN)


keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('👍Годные тайтлы'))
keyboard.add(KeyboardButton('🤷‍♂️Рандомное аниме'))


keyboard.add(KeyboardButton('Об авторе и боте'))

#-=-=-=-=-Получение списка anime-=-=-=-=-=-=-=-=
url = "https://api.jikan.moe/v4/anime"

response = requests.get(url)

data = response.json()
anime_titles = [item['title'] for item in data['data']]

# for i in anime_titles:
#     print(i)


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=



@bot.message_handler(regexp='автор')
def about_author(message):
    bot.send_message(message.chat.id, 'Автор Наум')

@bot.message_handler(regexp='🤷‍♂️Рандомное Аниме')
def godnie_taitls(message):
    bot.send_message(message.chat.id, f'Нашел для тебя: {anime_titles[random.randint(1,20)]}', reply_markup=keyboard)


@bot.message_handler(regexp='👍Годные тайтлы')
def godnie_taitl(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEJOoRkfzAXYWnuBMaa7SOhGnKLtchlIQACriIAAvThCUilx87YPT22ey8E')
    a = '\n'.join(str(x) for x in anime_titles)
    bot.send_message(message.chat.id, a)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Я бот, который советует тебе аниме, чтобы тебе не было скучно", reply_markup=keyboard)
    bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEJNUlkfJxisSAeZ5X3M1am1HJlQXwdrgACogMAAh4QYVWLQatEtVFxri8E')


@bot.message_handler(regexp='открой сайт')
def opener(message):
    webbrowser.open('https://animego.org/')

bot.infinity_polling()

