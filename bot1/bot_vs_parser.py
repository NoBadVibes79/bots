import requests
import telebot
import webbrowser
import random
from bs4 import BeautifulSoup as bs
from telebot import types

bot = telebot.TeleBot('6004800515:AAHaoQJ2kgfofcjrRdQJd1IMMJP8GQKXM_M')
url_jokes = 'https://anekdot.ru/last/good/'

r = requests.get(url_jokes)
#print(r.text) - увидеть текст, print(r.status_code) - увидеть статус
#! обработка в парсере
def parser(url):   
	soup = bs(r.text, 'html.parser') # через суп достаем текст со страницы
	jokes = soup.find_all('div', class_='text') # находим наш див
	return [c.text for c in jokes] # возвращаем без погрешностей ( дивы с классами и т.д. ))

list_of_jokes = parser(url_jokes)
random.shuffle(list_of_jokes) # перемешиваем 

@bot.message_handler(commands=['joke']) # команда для пользователя
def jokes_first_step(message):
	bot.send_message(message.chat.id, 'Чтобы посмеятся введи любую цифру')

@bot.message_handler(content_types=['text'])
def jokes(message):
	if message.text.lower() in '0123456789': # обрабатывает все эти цифры
		bot.send_message(message.chat.id, list_of_jokes[0]) # отдаем сообщение, с 1 по списку
		del list_of_jokes[0] # удаляем первый номер, который запостился
	else:
		bot.send_message(message.chat.id, 'Введи любую цифру')


bot.polling(none_stop=True)







