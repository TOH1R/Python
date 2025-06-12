import logging
import wikipedia 

from aiogram import Bot, Dispatcher, executor, types, filters 

API_TOKEN = "7246455037:AAHoQFvLuiVAOx1U6sGPkUN0A8z0lrjYQXI"

#Language
language_mapping = {
    "uzbek": "uz",
    "english": "en",
    "russian": "ru",
}

start_command = """
Wikipedia botiga xush kelibsiz!

Shunchaki istalgan malumoti kiriting, masalan, “kitob” , men sizga bu haqda malumot topib beraman.

Tilni o'zgartirish kerakmi? /set_lang buyrug'idan foydalaning.

Qo'shimcha ma'lumot yoki yordamga muhtoj bo'lsangiz, /help ni kiriting.

"""

help_command = """
Wikipedia botiga xush kelibsiz!

Qanday foydalaniladi:
Har qanday mavzu bo'yicha ma'lumot olish uchun xabaringizga malumot so'zni yuboring, men sizga tegishli ma'lumotlarni taqdim etaman. Misol uchun, agar siz "kitoblar" haqida bilmoqchi bo'lsangiz, shunchaki "kitob" ni kiriting.

Tilni o'zgartirish:
Siz quyidagi buyruqlar yordamida bot tilini o'zgartirishingiz mumkin:
/set_lang "ruscha" - Rus tiliga o'tish
/set_lang "english" - Ingliz tiliga o'tish
/set_lang "uzbek" - Uzbek tiliga o'tish

Qaytadan boshlash:
Yangi qidiruv yoki yangilashni boshlash uchun /start buyrug'idan foydalaning.

Yordam kerakmi?
Agar siz men haqimda ko'proq bilmoqchi bo'lsangiz yoki yordamga muhtoj bo'lsangiz, shunchaki /help yozing.

"""





logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#start
@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply(start_command)

#help
@dp.message_handler(commands=["help"])
async def send_discription(message: types.Message):
    await message.reply(help_command)
    


@dp.message_handler(commands=["set_lang"])
async def send_language(message: types.Message):
    try:
        lang = message.text.replace("/set_lang", "").strip().lower()

        if lang  in language_mapping:
            wikipedia.set_lang(language_mapping[lang])
            await message.answer(f"Language: {language_mapping[lang]}")
        else:
            await message.answer("Quyidagi tillardan birini kiriting. O'zbek, ingliz, rus")
    except Exception as e:
        print(e)
        await message.answer("Xatolik yuz berdi. Qayta urinib ko'ring.")

@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Ushbu mavzu bo'yicha hech qanday maqola topilmadi")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)




