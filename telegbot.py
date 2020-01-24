import telebot


bot = telebot.TeleBot('926769897:AAEJPSp4BOrg5ba_iwobt2zkbIgT9F1dtIc')
from weather import weather
from exchange import currence
from  meduzanews import meduzanews

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Погода', 'Валюта', 'Новости')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # bot.send_message(message.from_user.id, "Для получения команд Напиши Функции или Ф/F")
    if message.text == "функции" or message.text == "Функции" or message.text == "ф" or message.text == "f" or message.text == "F" or message.text == "Ф":
        bot.send_message(message.chat.id, 'Привет, ты написал мне Функции', reply_markup=keyboard1)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Для получения команд Напиши Функции или Ф/F")
    elif  message.text == "Погода":
        a, _ = weather()
        bot.send_message(message.from_user.id, a)
    elif  message.text == "Валюта":
        b, _ = currence()
        bot.send_message(message.from_user.id, b)
    elif  message.text == "Новости":
        c = meduzanews()
        bot.send_message(message.from_user.id, c)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data =='Погода':
        pass
    elif call.data == "Валюта":
        pass
    elif call.data == "Новости":
        c = meduzanews()
        bot.send_message(message.from_user.id, c)
    else:
        bot.send_message(message.from_user.id, 'я тебя не понимать')


bot.polling(none_stop=True, interval=0)
