import telebot
from telebot import types
bot = telebot.TeleBot('926769897:AAEJPSp4BOrg5ba_iwobt2zkbIgT9F1dtIc') #token blya
from weather import weather
from exchange import currence
from  meduzanews import meduzanews
from rssnews import overclockersnews
from rssnews import habrhabr
from probki import probki



@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == "функции" or message.text == "Функции" or message.text == "ф" or message.text == "f" or message.text == "F" or message.text == "Ф":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Погода")
        item2 = types.KeyboardButton('Валюта')
        item3 = types.KeyboardButton('Новости')
        item4 = types.KeyboardButton('Пробки')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, "Кнопки должны были появится!",  reply_markup=markup)
        pass
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Пользуйся кнопками! Если у тебя нет кнопок напиши Функции(Ф/F) или  функции(ф/f) и появятся кнопки!")
    elif  message.text == "Погода":
        a, _ = weather()
        bot.send_message(message.from_user.id, a)
    elif  message.text == "Валюта":
        b, _ = currence()
        bot.send_message(message.from_user.id, b)
    elif  message.text == "Пробки":
        d=probki()
        bot.send_message(message.from_user.id, d)
        bot.send_photo(message.from_user.id, open('probki.jpg', 'rb'))
    elif  message.text == "Новости":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Meduza", callback_data='meduza')
        item2 = types.InlineKeyboardButton("Overclockers", callback_data='overclockers')
        item3 = types.InlineKeyboardButton("Habr(Bestday)", callback_data='habrday')
        item4 = types.InlineKeyboardButton("HabrHabr(Bestweek)", callback_data='habrweek')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, 'Новости', reply_markup=markup)

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю! Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data =='meduza':
        c=meduzanews()
        bot.send_message(call.message.chat.id, c)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Новости Медузы",
                              reply_markup=None)
    elif call.data == 'overclockers':
        c=overclockersnews()
        bot.send_message(call.message.chat.id, c)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Новости Overclockers",
                              reply_markup=None)
    elif call.data == 'habrday':
        c=habrhabr(0)
        bot.send_message(call.message.chat.id, c)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Новости HabrHabr - лучшее за день ",
                              reply_markup=None)
    elif call.data == 'habrweek':
        c=habrhabr(1)
        bot.send_message(call.message.chat.id, c)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Новости HabrHabr - лучшее за неделю",
                              reply_markup=None)
    else:
        bot.send_message(message.from_user.id, 'я тебя не понимать')

















bot.polling(none_stop=True, interval=0)


# https://pastebin.com/zwWjLMYM
# https://mastergroosha.github.io/telegram-tutorial/