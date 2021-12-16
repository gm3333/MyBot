import telebot
from telebot import types

token = '2138734201:AAFwS2BlMjscbpV23vvok9ZxpcZMw1Kb8aU'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row('Want','I want some tea', 'I want to sleep', '/help')
    bot.send_message(message.chat.id, 'Hi! Do you want to know a new info about MTUCI',
                     reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id,
                                      'What I can do:'
                                      '/info - Info about MTUCI'
                                      '/pictures - Pics with MTUCI'
                                      '/support - online-support for discuss about any problems with bot')


@bot.message_handler(commands=['info'])
def help_message(message):
    bot.send_message(message.chat.id, 'Info about MTUCI:')

@bot.message_handler(commands=['pictures'])
def help_message(message):
    bot.send_message(message.chat.id, 'Pics with MTUCI:')

@bot.message_handler(commands=['support'])
def help_message(message):
    bot.send_message(message.chat.id, 'Lets speak with online-support')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == 'want':
        bot.send_message(message.chat.id, 'So, you need to be redirected to https://mtuci.ru/')
    if message.text.lower() == 'i want some tea':
        bot.send_message(message.chat.id, 'You need to stand up and go to the kithen to do this')
    if message.text.lower() == 'i want to sleep':
        bot.send_message(message.chat.id, 'So, go to bed')

bot.polling()