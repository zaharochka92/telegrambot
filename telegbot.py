import telebot
from telebot import types
from weather import weather
from exchange import currence
#from  meduzanews import meduzanews
from rssnews import overclockersnews
from rssnews import habrhabr, meduzanews
from probki import probki
from mikrotik import mikrotik_cmd
from aruba import arubainfo
from teletokens import *


bot = telebot.TeleBot(teletoken) #token
devhome = {'device_type': 'cisco_ios', 'username': user_mikro, 'password': password_mikro, 'verbose': True, 'ip': ip_mikro_home} # create dict for netmiko lib to connect to mikrotik
devdacha = {'device_type': 'cisco_ios', 'username': user_mikro, 'password': password_mikro, 'verbose': True, 'ip': ip_mikro_dacha}

@bot.message_handler(content_types=['text'])


def get_text_messages(message):

    if message.text == "функции" or message.text == "Функции" or message.text == "ф" or message.text == "f" or message.text == "F" or message.text == "Ф":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # клавиатура основного функционала бота
        item1 = types.KeyboardButton("Погода")  # парсинг погода с сайта openweather
        item2 = types.KeyboardButton('Валюта')  # парсинг курс валют с цб
        item3 = types.KeyboardButton('Новости') # новости
        item4 = types.KeyboardButton('Пробки') # пробки
        item5 = types.KeyboardButton('Telekom')
        # item6 = types.KeyboardButton('Flibustabook')
        markup.add(item1, item2, item3, item4, item5)
        bot.send_message(message.chat.id, "Кнопки должны были появится!",  reply_markup=markup)
        pass
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Пользуйся кнопками! Если у тебя нет кнопок напиши Функции(Ф/F) или  функции(ф/f) и появятся кнопки!")
    elif  message.text == "Погода":
        a, _ = weather(openweather_token)
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
        item4 = types.InlineKeyboardButton("Habr(Bestweek)", callback_data='habrweek')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, 'Новости', reply_markup=markup)
    # info telecom service later make functions
    elif  message.text == "Telekom":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Mikrohome", callback_data='mikrohome')
        item2 = types.InlineKeyboardButton("Mikrodacha", callback_data='mikrodacha')
        item3 = types.InlineKeyboardButton("ArubaCloud", callback_data='arubacloud')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, 'Telekom', reply_markup=markup)
    # flibusta temp off
    # elif message.text == 'Flibustabook':
    #     bot.send_message(message.from_user.id, "Я помогу найти книгу на сайте Flibusta")
    #     bot.send_message(message.from_user.id, "введи название книги")
    #     bot.register_next_step_handler(message, get_book_name)

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю! Напиши /help.")




# def get_book_name(message):
#     bookname= message.text
#     if bookname.count(' ')!=0:
#         bookname = bookname.replace(' ', '+')
#     url=f'https://flibusta.appspot.com/booksearch?BK9fzvf3=&ask={bookname}&chs=on&cha=on&chb=on'
#     bot.send_message(message.from_user.id, url)




@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data =='meduza':

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Новости Медузы",
                              reply_markup=None)
        result = meduzanews()
        if len(result) > 4096:
            for x in range(0, len(result), 4096):
                bot.send_message(call.message.chat.id, result[x:x + 4096])
        else:
            bot.send_message(call.message.chat.id, result)


    elif call.data == 'overclockers':

        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Новости Overclockers",
                              reply_markup = None)
        result = overclockersnews()
        bot.send_message(call.message.chat.id, result)
    elif call.data == 'habrday':

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Новости HabrHabr - лучшее за день ",
                              reply_markup=None)
        result = habrhabr(0)
        bot.send_message(call.message.chat.id, result)
    elif call.data == 'habrweek':

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Новости HabrHabr - лучшее за неделю",
                              reply_markup=None)
        result = habrhabr(1)
        bot.send_message(call.message.chat.id, result)

    elif call.data == 'mikrodacha':
        c=mikrotik_cmd(devdacha)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Информация Микротик Дача",
                              reply_markup=None)
        result = mikrotik_cmd(devdacha)
        bot.send_message(call.message.chat.id, result)
    elif call.data == 'mikrohome':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Информация Микротик Дом",
                              reply_markup=None)
        result = mikrotik_cmd(devhome)
        bot.send_message(call.message.chat.id, result)
    elif call.data == 'arubacloud':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Информация по облаку этого бота",
                              reply_markup=None)
        result = arubainfo(arubalogin, arubapassword)
        bot.send_message(call.message.chat.id, result)

    else:
        bot.send_message(message.from_user.id, 'я тебя не понимать')

bot.polling(none_stop=True, interval=0) #start bot

# i used this guide
# https://pastebin.com/zwWjLMYM
# https://mastergroosha.github.io/telegram-tutorial/