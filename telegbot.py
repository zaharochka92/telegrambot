import telebot
from telebot import types
bot = telebot.TeleBot('926769897:AAEJPSp4BOrg5ba_iwobt2zkbIgT9F1dtIc') #token blya
from weather import weather
from exchange import currence
from  meduzanews import meduzanews
from rssnews import overclockersnews
from rssnews import habrhabr
from probki import probki
from mikrotik import mikrotik_cmd




@bot.message_handler(content_types=['text'])


def get_text_messages(message):

    if message.text == "функции" or message.text == "Функции" or message.text == "ф" or message.text == "f" or message.text == "F" or message.text == "Ф":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # клавиатура основного функционала бота
        item1 = types.KeyboardButton("Погода")  # парсинг погода с сайта опен везер
        item2 = types.KeyboardButton('Валюта')  # парсинг курс валют с цб
        item3 = types.KeyboardButton('Новости')
        item4 = types.KeyboardButton('Пробки')
        item5 = types.KeyboardButton('Mikrotik')
        item6 = types.KeyboardButton('Flibustabook')
        markup.add(item1, item2, item3, item4, item5, item6)
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
        item4 = types.InlineKeyboardButton("Habr(Bestweek)", callback_data='habrweek')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, 'Новости', reply_markup=markup)
    elif  message.text == "Mikrotik":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("home", callback_data='mikrohome')
        item2 = types.InlineKeyboardButton("dacha", callback_data='mikrodacha')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Mikrotik', reply_markup=markup)
    elif message.text == 'Flibustabook':
        bot.send_message(message.from_user.id, "Я помогу найти книгу на сайте Flibusta")
        bot.send_message(message.from_user.id, "введи название книги")
        bot.register_next_step_handler(message, get_book_name)

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю! Напиши /help.")




def get_book_name(message):
    bookname= message.text
    if bookname.count(' ')!=0:
        bookname = bookname.replace(' ', '+')
    url=f'https://flibusta.appspot.com/booksearch?BK9fzvf3=&ask={bookname}&chs=on&cha=on&chb=on'
    bot.send_message(message.from_user.id, url)




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


    elif call.data == 'mikrodacha':
        c=mikrotik_cmd('192.168.42.200')
        bot.send_message(call.message.chat.id, c)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Информация Микротик Дача",
                              reply_markup=None)
    elif call.data == 'mikrohome':
        c=mikrotik_cmd('192.168.42.100')
        bot.send_message(call.message.chat.id, c)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Информация Микротик Дом",
                              reply_markup=None)
    else:
        bot.send_message(message.from_user.id, 'я тебя не понимать')

















bot.polling(none_stop=True, interval=0)


# https://pastebin.com/zwWjLMYM
# https://mastergroosha.github.io/telegram-tutorial/