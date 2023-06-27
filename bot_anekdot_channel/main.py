import requests
import telebot
import webbrowser
import random
from bs4 import BeautifulSoup as bs
from telebot import types


# * Часть 1 - парсер

url_jokes = 'https://anekdot.ru/last/good/'

r = requests.get(url_jokes)


def parser(url):
    # через суп достаем текст со страницы
    soup = bs(r.text, 'html.parser')
    jokes = soup.find_all('div', class_='text')  # находим наш див
    # возвращаем без погрешностей ( дивы с классами и т.д. ))
    return [c.text for c in jokes]


list_of_jokes = parser(url_jokes)
random.shuffle(list_of_jokes)  # перемешиваем

# * Часть 2 - бот

bot = telebot.TeleBot('TOKEN')
TOKEN = "TOKEN"
# -1001987056770 id моего канала
chat_id = "id_channel"
# то что не получилось вставить (Запомните, <b>смех - продлевает жизнь!</b> <br>, <br> Это сообщение прислал мой бот, который умеет шутить <i>(парсер и сам бот написаны на Python).</i>)
message = f'Бот шутник пришел подарить вам немного хорошего настроения : {list_of_jokes[0]}'
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
# Эта строка отсылает сообщение
print(requests.get(url).json())
