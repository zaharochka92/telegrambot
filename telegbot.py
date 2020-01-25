import telebot
from telebot import types
bot = telebot.TeleBot('926769897:AAEJPSp4BOrg5ba_iwobt2zkbIgT9F1dtIc') #token blya
from weather import weather
from exchange import currence
from  meduzanews import meduzanews

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Погода")
item2 = types.KeyboardButton('Валюта')
item3 = types.KeyboardButton('Новости', callback_data='news')
markup.add(item1, item2, item3)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == "функции" or message.text == "Функции" or message.text == "ф" or message.text == "f" or message.text == "F" or message.text == "Ф":
    #     #     # bot.send_message(message.chat.id, 'Привет, ты написал мне Функции', reply_markup=keyboard1)
        bot.send_message(message.from_user.id, 'functions', reply_markup=markup)
    #     bot.send_message(message.chat.id, "Функции",  reply_markup=markup)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Для получения команд Напиши Функции или Ф/F")
    elif  message.text == "Погода":
        a, _ = weather()
        bot.send_message(message.from_user.id, a)
    elif  message.text == "Валюта":
        b, _ = currence()
        bot.send_message(message.from_user.id, b)
    # elif  message.text == "Новости":
    #     )
    elif message.text == "Meduza":
        c = meduzanews()
        bot.send_message(message.from_user.id, c, reply_markup=None)
        # else:
        #     bot.send_message(message.from_user.id, 'Dobavim pozje')
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data =='news':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item11 = types.KeyboardButton("Meduza")
        item22 = types.KeyboardButton('Overclockers')
        markup.add(item11, item22)
        bot.send_message(message.from_user.id, 'News', reply_markup=markup1)
    elif call.data == "Валюта":
        pass
    elif call.data == "Новости":
        c = meduzanews()
        bot.send_message(message.from_user.id, c)
    else:
        bot.send_message(message.from_user.id, 'я тебя не понимать')

















bot.polling(none_stop=True, interval=0)


# https://pastebin.com/zwWjLMYM
# https://mastergroosha.github.io/telegram-tutorial/