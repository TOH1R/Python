import telebot
from telebot import types
import random

token = '7489626550:AAGs2zQKkjAzDkaWJPU9p1PXHIVj3fN15sg'
bot = telebot.TeleBot(token)

qogoz = "✋"
qaychi = "✌️"
quduq = "✊"
elementlar = [qogoz, qaychi, quduq]

galaba, maglubiyat, durrang = 0, 0, 0

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
for element in elementlar:
    item = types.KeyboardButton(element)
    markup.add(item)
item = types.KeyboardButton("📊 Statistika")
markup.add(item)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Pastdagi tugmalardan birini bosing👇", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def message_reply(message):
    global galaba, maglubiyat, durrang
    user = message.text
    bot_choice = random.choice(elementlar)

    if user == qogoz:
        if bot_choice == qogoz:
            bot.send_message(message.chat.id, bot_choice)
            bot.send_message(message.chat.id, "Durrang", reply_markup=markup)
            durrang += 1
        elif bot_choice == qaychi:
            bot.send_message(message.chat.id, bot_choice, reply_markup=markup)
            bot.send_message(message.chat.id, "Siz yutqazdingiz", reply_markup=markup)
            maglubiyat += 1
        else:
            bot.send_message(message.chat.id, bot_choice, reply_markup=markup)
            bot.send_message(message.chat.id, "Siz yutdingiz", reply_markup=markup)
            galaba += 1
    elif user == qaychi:
        if bot_choice == qaychi:
            bot.send_message(message.chat.id, bot_choice)
            bot.send_message(message.chat.id, "Durrang", reply_markup=markup)
            durrang += 1
        elif bot_choice == qogoz:
            bot.send_message(message.chat.id, bot_choice)
            bot.send_message(message.chat.id, "Siz yutdingiz", reply_markup=markup)
            galaba += 1
        else:
            bot.send_message(message.chat.id, bot_choice)
            bot.send_message(message.chat.id, "Siz yutqazdingiz", reply_markup=markup)
            maglubiyat += 1
    elif user == quduq:
        if bot_choice == qaychi:
            bot.send_message(message.chat.id, bot_choice)
            bot.send_message(message.chat.id, "Siz yutdingiz", reply_markup=markup)
            galaba += 1
        elif bot_choice == qogoz:
            bot.send_message(message.chat.id, bot_choice)
            bot.send_message(message.chat.id, "Siz yutqazdingiz", reply_markup=markup)
            maglubiyat += 1
        else:
            bot.send_message(message.chat.id, bot_choice)
            bot.send_message(message.chat.id, "Durrang", reply_markup=markup)
            durrang += 1
    elif user == "📊 Statistika":
        stat = types.InlineKeyboardMarkup()
        stat.row(types.InlineKeyboardButton('🗑 Tozalash', callback_data='clear'))
        bot.send_message(message.chat.id, f"🏆 G'alaba: {galaba} ta\n🚫 Mag'lubiyat: {maglubiyat} ta\n🤝 Durrang: {durrang} ta", reply_markup=stat)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
  global galaba, maglubiyat, durrang
  if call.data == 'clear':
    galaba,maglubiyat,durrang=0,0,0
    bot.send_message(call.message.chat.id, "Statistika tozalandi")
    stat = types.InlineKeyboardMarkup()
    stat.row(types.InlineKeyboardButton('🗑 Tozalash', callback_data='clear'))
    bot.send_message(call.message.chat.id, f"🏆 G'alaba: {galaba} ta\n🚫 Mag'lubiyat: {maglubiyat} ta\n🤝 Durrang: {durrang} ta",reply_markup=stat)

bot.infinity_polling()
