import telebot

BOT_TOKEN = "7786170997:AAGlB-0oXF81arw-FgziNahPoaiCfx6-C_8"
bot = telebot.TeleBot(BOT_TOKEN)

user_data = {}

@bot.message_handler(commands=['start'])
def start_handler(message):
    user_data[message.chat.id] = {"result": None}  
    bot.send_message(
        message.chat.id,
        "Salom! 😊 Men kalkulyatorman.\n"
        "Matematik hisoblarni amalga oshirish uchun birinchi raqamni kiriting:"
    )
    bot.register_next_step_handler(message, get_first_number)

def get_first_number(message):
    try:
        number = float(message.text)
        user_data[message.chat.id]["result"] = number
        bot.send_message(message.chat.id, "Ajoyib. Endi operatsiyani kiriting (+, -, *, /):")
        bot.register_next_step_handler(message, get_operator)
    except ValueError:
        bot.send_message(message.chat.id, "Iltimos, haqiqiy son kiriting.")
        bot.register_next_step_handler(message, get_first_number)

def get_operator(message):
    operator = message.text
    if operator in ["+", "-", "*", "/"]:
        user_data[message.chat.id]["operator"] = operator
        bot.send_message(message.chat.id, "Yaxshi. Endi ikkinchi raqamni kiriting:")
        bot.register_next_step_handler(message, get_second_number)
    else:
        bot.send_message(message.chat.id, "Iltimos, to'g'ri operatorni kiriting (+, -, *, /):")
        bot.register_next_step_handler(message, get_operator)

def get_second_number(message):
    try:
        number = float(message.text)
        chat_id = message.chat.id
        operator = user_data[chat_id]["operator"]
        result = user_data[chat_id]["result"]

        if operator == "+":
            result += number
        elif operator == "-":
            result -= number
        elif operator == "*":
            result *= number
        elif operator == "/":
            if number == 0:
                bot.send_message(chat_id, "0 ga bo'lib bo'lmaydi. Boshqa raqam kiriting:")
                bot.register_next_step_handler(message, get_second_number)
                return
            result /= number

        user_data[chat_id]["result"] = result

        bot.send_message(chat_id, f"Natija: {result}")
        bot.send_message(chat_id, "Hisob-kitoblarni davom ettirmoqchimisiz? (Ha yoki Yo'q):")
        bot.register_next_step_handler(message, ask_continue)
    except ValueError:
        bot.send_message(message.chat.id, "Iltimos, haqiqiy son kiriting.")
        bot.register_next_step_handler(message, get_second_number)

def ask_continue(message):
    chat_id = message.chat.id
    if message.text.lower() in ["ha", "yes"]:
        bot.send_message(chat_id, "Operatsiyani kiriting (+, -, *, /):")
        bot.register_next_step_handler(message, get_operator)
    else:
        bot.send_message(chat_id, "Xayr! 😊 Yana hisoblash uchun /start buyrug'ini kiriting.")
        user_data.pop(chat_id, None)

if __name__ == "__main__":
    bot.polling()
