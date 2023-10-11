import telebot
import requests

BOTTOKEN = '6620210358:AAGZxUgIEUUkUVU_jFxzwbwucKcLk9ORazI'
BASEURL = 'https://api.binance.com/api/v3'

def get_digital_currency_price(symbol):
    response = requests.get(BASEURL+f'/ticker/price?symbol={symbol}')
    return response


bot = telebot.TeleBot(BOTTOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "سلام چطوری گوگولی  این یه ربات قیمت ارز های دیجیتاله")



# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     if message.text == 'salam':
#         bot.reply_to(message, 'Aleyke Salam')
#     else:
# 	    bot.reply_to(message, message.text)



@bot.message_handler(func=lambda m: True)
def show_price(message):
    symbol = message.text.upper()
    result = get_digital_currency_price(symbol)
    data = result.json()
    if result.status_code == 400:
        bot.reply_to(message, 'Symbol Is Not Correct')
    else:
        bot.reply_to(message, f"{symbol} Price Is : {data['price']}")





bot.infinity_polling()







