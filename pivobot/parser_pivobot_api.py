import requests
import json
from operator import *
import telebot
from telebot import types

# краснодарский магнит
cookies_kr_mag = {
    '_gid': 'GA1.2.1532567463.1687979191',
    '_ym_uid': '168797919118725883',
    '_ym_d': '1687979191',
    '_ym_isad': '1',
    'subscribe_showed': '1',
    'visitorcity': 'krasnodar',
    'ec8956637a99787bd197eacd77acce5e': '%7B%22products_limit2%22%3A500%7D',
    '_ym_visorc': 'b',
    '_ga_VXB631NEPB': 'GS1.2.1688028658.3.1.1688028860.0.0.0',
    'PHPSESSID': '79ga4l2ndne49et2fhe2b1mv7b',
    '_gat': '1',
    '_ga_YL18X8Z772': 'GS1.1.1688028657.3.1.1688029677.0.0.0',
    '_ga': 'GA1.1.800302989.1687979191',
}

headers_kr_mag = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': '_gid=GA1.2.1532567463.1687979191; _ym_uid=168797919118725883; _ym_d=1687979191; _ym_isad=1; subscribe_showed=1; visitorcity=krasnodar; ec8956637a99787bd197eacd77acce5e=%7B%22products_limit2%22%3A500%7D; _ym_visorc=b; _ga_VXB631NEPB=GS1.2.1688028658.3.1.1688028860.0.0.0; PHPSESSID=79ga4l2ndne49et2fhe2b1mv7b; _gat=1; _ga_YL18X8Z772=GS1.1.1688028657.3.1.1688029677.0.0.0; _ga=GA1.1.800302989.1687979191',
    'Pragma': 'no-cache',
    'Referer': 'https://skidkaonline.ru/krasnodar/pivo-pivnye-napitki/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://skidkaonline.ru/apiv3/products/?limit=30&offset=0&pcategories_ids=414&city_id=72&fields=id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,daystitle,liked,started_today,published_today',
    cookies=cookies_kr_mag,
    headers=headers_kr_mag,
).json()


# print(response)
json_response = response.get('products')

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(json_response, file, indent=4, ensure_ascii=False)

item_prices_dict = {}

material_prices = response.get('products')


Sorted_response = sorted(
    json_response, key=lambda x: x['discount'], reverse=True)
#! краснодарский магнит

# пермский перекресток
cookies_pe_pe = {
    '_gid': 'GA1.2.1532567463.1687979191',
    '_ym_uid': '168797919118725883',
    '_ym_d': '1687979191',
    'subscribe_showed': '1',
    'ec8956637a99787bd197eacd77acce5e': '%7B%22products_limit2%22%3A500%7D',
    'discounts_viewed': '455604',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    'visitorcity': 'perm',
    '_gat': '1',
    'PHPSESSID': '79ga4l2ndne49et2fhe2b1mv7b',
    '_ga_YL18X8Z772': 'GS1.1.1688116802.11.1.1688117084.0.0.0',
    '_ga': 'GA1.1.800302989.1687979191',
    '_ga_VXB631NEPB': 'GS1.2.1688116803.13.1.1688117084.0.0.0',
}

headers_pe_pe = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': '_gid=GA1.2.1532567463.1687979191; _ym_uid=168797919118725883; _ym_d=1687979191; subscribe_showed=1; ec8956637a99787bd197eacd77acce5e=%7B%22products_limit2%22%3A500%7D; discounts_viewed=455604; _ym_isad=2; _ym_visorc=b; visitorcity=perm; _gat=1; PHPSESSID=79ga4l2ndne49et2fhe2b1mv7b; _ga_YL18X8Z772=GS1.1.1688116802.11.1.1688117084.0.0.0; _ga=GA1.1.800302989.1687979191; _ga_VXB631NEPB=GS1.2.1688116803.13.1.1688117084.0.0.0',
    'Pragma': 'no-cache',
    'Referer': 'https://skidkaonline.ru/perm/shops/perekrestok/pivo-pivnye-napitki/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response_pe_pe = requests.get(
    'https://skidkaonline.ru/apiv3/products/?limit=30&offset=0&pcategories_ids=414&shop_id=7&city_id=110&fields=id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,daystitle,liked,started_today,published_today',
    cookies=cookies_pe_pe,
    headers=headers_pe_pe,
).json()


json_response_pe_pe = response_pe_pe.get('products')

with open('data2.json', 'w', encoding='utf-8') as file:
    json.dump(json_response, file, indent=4, ensure_ascii=False)

#! пермский перекресток


#! часть с ботом

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Пиво Краснодар')
    btn2 = types.KeyboardButton('Пиво Пермь')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Привет, этот бот, может найти тебе самое дешевое пиво в Краснодаре в семейном Магните или в Перми в Перекрестке \nДля этого нажми на кнопку ниже или напиши в сообщении "Пиво Краснодар" или "Пиво Пермь" \nЕсли что-то забыл введи команду "/start"', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Пиво Краснодар')
    btn2 = types.KeyboardButton('Пиво Пермь')
    markup.add(btn1, btn2)
    if message.text.lower() == "пиво краснодар":
        for i in range(5):
            name = Sorted_response[i].get('name')
            price = Sorted_response[i].get('priceafter')
            url_img = Sorted_response[i].get('imagefull').get('src')
            end_discount = Sorted_response[i].get('enddate')
            price_before = Sorted_response[i].get('pricebefore')
            mess = f'Название пивчанского - <b>{name}</b> \nСейчас на скидке и стОит - <i>{price} рублей</i> \nДо этого стоил - <i>{price_before} рублей</i> \nСкидка закончится - {end_discount}'
            bot.send_photo(
                message.chat.id, photo=f'{url_img}', caption=mess, parse_mode='html', reply_markup=markup)
    elif message.text.lower() == "пиво пермь":
        for i in range(10):
            url_img = json_response_pe_pe[i].get('imagefull').get('src')
            end_discount = json_response_pe_pe[i].get('enddate')
            mess = f'Скидка закончится - {end_discount}'
            bot.send_photo(
                message.chat.id, photo=f'{url_img}', caption=mess, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
# for item in material_prices:
#     item_id = item.get('id')
#     item_base = item.get('pricebefore')
#     item_prices = item.get('priceafter')
#     item_name = item.get('name')

#     item_prices_dict[item_id] = {
#         'item_base': item_base,
#         'item_prices': item_prices,
#         'item_name': item_name,
#     }
#     print(item_prices_dict)
#     # sorted(item_prices_dict, key=attrgetter('priceafter'))
#     users = sorted(item_prices_dict, key=itemgetter('item_base'))
#     # w - перезапись файла, a - дозапись
#     with open('products_prices.json', 'w', encoding='utf-8') as file:
#         json.dump(users, file, indent=4, ensure_ascii=False)


# elif message.text.lower() == "photo":
#     photo = open('img.jpg', 'rb')
#     bot.send_photo(message.chat.id, photo)


# for item in json_response:
#     if item.get('pricebefore') != item.get('priceafter'):
#         return_str = f'Пивас {item.get('name')} сейчас на скидке и стоит {item.get('price')}'
#         bot.send_message(return_str)
