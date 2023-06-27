import requests
import telebot
import webbrowser
import random
from bs4 import BeautifulSoup as bs
from telebot import types

bot = telebot.TeleBot('TOKEN')
url_jokes = 'https://anekdot.ru/last/good/'

r = requests.get(url_jokes)
# print(r.text) - увидеть текст, print(r.status_code) - увидеть статус
#! обработка в парсере


def parser(url):
    # через суп достаем текст со страницы
    soup = bs(r.text, 'html.parser')
    jokes = soup.find_all('div', class_='text')  # находим наш див
    # возвращаем без погрешностей ( дивы с классами и т.д. ))
    return [c.text for c in jokes]


list_of_jokes = parser(url_jokes)
random.shuffle(list_of_jokes)  # перемешиваем


# команда для пользователя
@bot.message_handler(commands=['joke'])
def jokes_first_step(message):
    bot.send_message(
        message.chat.id, 'Чтобы посмеятся введи любую цифру')


@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '0123456789':  # обрабатывает все эти цифры
        # отдаем сообщение, с 1 по списку
        bot.send_message(message.chat.id, list_of_jokes[0])
        # удаляем первый номер, который запостился
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Введи любую цифру')


bot.polling(none_stop=True)
