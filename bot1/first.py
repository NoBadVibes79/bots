import requests
import telebot
import webbrowser
from telebot import types



bot = telebot.TeleBot('6004800515:AAHaoQJ2kgfofcjrRdQJd1IMMJP8GQKXM_M') # podklychenie tg
me_id = "722895694" # my id


#! функция для получения message в этот же чат
#? @bot.message_handler(content_types=['text'])
#? def get_user_message(message):
#?     if message.text.lower() != "хз":
#?         bot.send_message(message.chat.id, message)\

#! SimpleCustomFilter для логических значений, таких как is_admin = true
class IsAdmin(telebot.custom_filters.SimpleCustomFilter):
    key='is_admin'
    @staticmethod
    def check(message):
        return bot.get_chat_member(message.chat.id,message.from_user.id).status in ['administrator','creator']

bot.add_custom_filter(IsAdmin())
@bot.message_handler(is_admin=True, commands=['admin']) # Check if user is admin
def admin_rep(message):
    bot.send_message(message.chat.id, "Hi admin")

@bot.message_handler(is_admin=False, commands=['admin']) # If user is not admin
def not_admin(message):
    bot.send_message(message.chat.id, "You are not admin")

#! команда для получения месседж из любого места
@bot.message_handler(commands=['message'])
def get_any_message(message):
    me_id =  "722895694" # my id
    not_me_mess = f' Привет, <b><em>{message.from_user.first_name}</em></b> Данные успешно отправлены администратору - <u><em>@Sad_Manners</em></u>'
    if message.chat.type == "private":
        bot.send_message(message.chat.id, message)
    else:
        bot.send_message(message.chat.id, not_me_mess, parse_mode='html' )
        bot.forward_message(me_id, message.chat.id, message.id)
        bot.send_message(me_id, message)

#! пересылка сообщений из каналов ( только если бот админ )
@bot.channel_post_handler(content_types=['text']) # обработчик сообщений из каналов
def channel_post (message): 
    if message.text.lower() != "всем привет":
        bot.forward_message(me_id, message.chat.id, message.id)


@bot.message_handler(commands=['start']) # учим бота командам, ([,'idi_naxuy']) можно добавить любую команду
def start(message): # функция на ответы, прописать можно что угодно, message - параметр
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Посетить веб сайт')
    markup.row(btn1)
    btn2 = types.KeyboardButton("Удалить фото")
    btn3 = types.KeyboardButton("Изменить текст")
    markup.row(btn2, btn3)
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>' # что мы отдаем в сообщении
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup) 
    bot.register_next_step_handler(message, on_click) #? передаем дейвствие на функцию, которая будет срабатываеть следующей, так можно последовательно выстраить логику в боте

def on_click(message):
    if message.text == 'Посетить веб сайт':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Deleted')
    

#! Получение фотки и настройка кнопок
@bot.message_handler(content_types=['photo']) # обработка фото
def get_user_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Посетить веб сайт", url="http://estudio-5.com/")
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton("Удалить фото", callback_data='delete')
    btn3 = types.InlineKeyboardButton("Изменить текст", callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Вау, крутое фото!', reply_markup=markup)

#TODO: обработка функции delete
@bot.callback_query_handler(func=lambda callback: True) # декоратор для орбработки callback_data, метода = анонимная функция, если она возвращает пустое значение, то true
def callback_message(callback):
    if callback.data == 'delete': # only delete
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1) # в функции (чат(в котором работаешь), айди сообщения(которое нужно удалить)) удаление предпоследнего сообщения( тут фото )
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

@bot.message_handler(commands=['website']) # обращение для кнопок inline
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="http://estudio-5.com/"))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)


@bot.message_handler(commands=['help']) # обращение для кнопок Main
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1) # для мобилы ресайз, row_width=1 - кол-во кнопок в строке
    website = types.KeyboardButton('Веб сайт')
    start = types.KeyboardButton('Start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Выберите то, что вас интересует( Рекомендую Веб Сайт )', reply_markup=markup)

@bot.message_handler(is_admin=True, commands=['site']) #TODO: open web if u admin
def site(message):
    webbrowser.open('http://estudio-5.com/')

@bot.message_handler(is_admin=False, commands=['site']) #TODO: no open web
def site(message):
    bot.send_message(message.chat.id, "You are not admin \U0001F606", parse_mode='html')


@bot.message_handler(commands=['hello']) #! Двойная обработка хендлера
@bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == "\U0001F606")
def send_something(message):
    bot.send_message(message.chat.id, "Я тебя не понимаю \U0001F606", parse_mode='html')

@bot.message_handler(content_types=['text']) # обработка текстовых сообщений
def get_user_text(message):
    if message.text.lower() == "hello":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="http://estudio-5.com/"))
        hello = f"И тебе привет, <b><em>{message.from_user.first_name} <u>{message.from_user.username}</u></em></b> \N{sauropod}"
        bot.send_message(message.chat.id, hello, parse_mode='html', reply_markup=markup)
    elif message.text.lower() == "id":
        bot.reply_to(message, f"Твой ID: {message.from_user.id}", parse_mode='html')
    elif message.text.lower() == "photo":
        photo = open('img.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text.lower() == "запиши голосовое сообщение":
        rain = open('rain.mp3', 'rb')
        bot.send_voice(message.chat.id, rain)
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю \U0001F606 \U0001F606", parse_mode='html')


# @bot.message_handler(chat_types=)





bot.polling(none_stop=True) # none stop work