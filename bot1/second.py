import telebot
from telebot import types

bot = telebot.TeleBot('TOKEN') # podklychenie tg

@bot.message_handler(commands=['start', 'main'])
def main(message):
    bot.send_message(message.chat.id, 'Privet!')

@bot.message_handler(content_types=['text']) #обработка текстовых сообщений
def get_user_text(message):
    if message.text.lower() == "hello":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="http://estudio-5.com/"))
        bot.send_message(message.chat.id, f"И тебе привет, <b><em>{message.from_user.first_name} <u>{message.from_user.username}</u></em></b>", parse_mode='html', reply_markup=markup)
    elif message.text.lower() == "id":
        bot.reply_to(message, f"Твой ID: {message.from_user.id}", parse_mode='html')
    elif message.text.lower() == "photo":
        photo = open('img.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text.lower() == "запиши голосовое сообщение":
        rain = open('rain.mp3', 'rb')
        bot.send_voice(message.chat.id, rain)
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')

bot.polling(none_stop=True) 