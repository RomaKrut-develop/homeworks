from telebot import TeleBot
import json
import requests

bot = TeleBot("7433749136:AAF5sWxEPseJFSru6SdocZMbcO-VsmMBkyU")

print('Bot has been started')

@bot.message_handler(commands=['start'])
def command_start(message):
    bot.reply_to(message, f"Здраствуйте, {message.from_user.first_name}..")

@bot.message_handler(commands=['valute'])
def valute(message):
    api = json.loads(requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text)
    words_list = ' '.join(message.text.strip().split(' ')[1:])

    if words_list[0].isupper():
        valute = api['Valute'][words_list]
        text_list = []
        for key, value in valute.items():
            text_list.append(f'{key} - {value}')
        bot.reply_to(message, "\n".join(text_list))
    elif words_list[0] == words_list[0].capitalize():
        if len(words_list) == 1:
            word = words_list[0].capitalize()
        if len(words_list) == 2:
            word = words_list[0].capitalize() + words_list.lower()

# @bot.message_handler(commands=['simple'])
# def simple(message):
#     pass
#     # with open("preview.webp", 'rb') as file:
#     #     bot.send_photo(message.chat.id, file)

# # @bot.message_handler(commands=['add_task'])
# # def add_task(message):

bot.polling()