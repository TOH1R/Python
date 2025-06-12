from aiogram import Router, filters, types, F
from aiogram.filters import state
from aiogram.types import CallbackQuery

from app.states import Registration, Card
from aiogram.fsm.context import FSMContext
from app.keyboard import (main_button_lang, main_menu_uzbek, main_menu_rus, mars_itschool, kurs_menu_uzbek, kurs_menu_rus, mars_itschool_rus,
                          Fronted, Fronted_rus, Backend_rus, Backend,Mobile_dasturlash,Mobile_dasturlash_rus, Samar_Badriddinov_rus,
                          Flutter_gacha,Flutter_gacha_rus, Python, Python_rus, C_rus,C, php,php_rus,Java,Java_rus,Frontend_Saud_Abdulwahed,Frontend_Saud_Abdulwahed_rus,
                          HTMLvaCSS,HTMLvaCSS_rus,JavaScript_Saidbek_Arislonov,JavaScript_Saidbek_Arislonov_rus,
                          Samar_Badriddinov1, chat_gpt, chat_gpt_rus,
                          
                          
                          )

from aiogram import Router, filters, types, F
from aiogram.filters import state
from aiogram.types import CallbackQuery
from aiogram.types import FSInputFile
from aiogram import types, Bot, Dispatcher, filters, F
import asyncio
import openai
from aiogram.fsm.context import FSMContext
from app.states import Chatgpt

# from Rus.keyboard_rus import ()   



dp = Router()
orders = []
order = []






#Chatgpt
openai.api_key = "sk-proj-lsZStoLjK1BSTxdAc8C4T3BlbkFJeIrTB7DF2hzeR7r7EKLW"

def answer_process(question):
    response = openai.Completion.create(
        model='gpt-3.5-turbo-instruct',
        prompt=f"{question}",
        max_tokens=1000,
    )
    if response['choices'][0]['text']:
        answer = response['choices'][0]['text']
        answer.replace("_", "\\_")
        answer.replace("*", "\\*")
        answer.replace("[", "\\[")
        answer.replace("`", "\\`")
        answer.replace("=", "\\=")
        return answer
    else:
        return "Nima divossan? "


@dp.message(F.text == "Yordam")
async def chatgpt_function(message: types.Message, state: FSMContext):
    await state.set_state(Chatgpt.text)
    await message.answer("Man chatGPT, nima yordam kerak?", reply_markup=chat_gpt)
    
    
@dp.message(Chatgpt.text)
async def text_function(message: types.Message, state: FSMContext):
    if message.text == "Chiqish":
        await state.clear()
        await message.answer("Siz menyuga qaytingiz", reply_markup=main_menu_uzbek)
    else:
        
        result = await answer_process(question=message.text)
        await message.answer(result)
        await state.clear()
    
    
    
@dp.message(F.text == "Помощь")
async def chatgpt_function(message: types.Message, state: FSMContext):
    await state.set_state(Chatgpt.text)
    await message.answer("Мужик, ЧатGPT, в чем тебе нужна помощь?", reply_markup=chat_gpt_rus)
    






#Contact
contact_button = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="Kontakt jo'natish☎️", request_contact=True)]
], resize_keyboard=True)

location_button = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="Lokatsa📍",request_location=True)]
], resize_keyboard=True)


@dp.message(filters.Command("location"))
async def lang_function(message: types.Message):
    await message.answer(text="Lokatsiya📍", reply_markup=location_button)


@dp.message(filters.Command("start"))
async def start_function(message: types.Message, state: FSMContext):
    await state.set_state(Registration.first_name)
    await message.answer("Xush kelibsiz, ismingizni kiriting")


@dp.message(Registration.first_name)
async def first_name_function(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(Registration.last_name)
    await message.answer("Siz ismingizni kiritdingiz endi familyangizni kiriting")


@dp.message(Registration.last_name)
async def last_name_function(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(Registration.phone_number)
    await message.answer("Siz familyangizni kiritdingiz endi raqamingizni kiriting", reply_markup=contact_button)

@dp.message(Registration.phone_number)
async def last_name_function(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(Registration.location)
    await message.answer("Siz telefon raqamingizni kiritingiz endi, Locatsiyangizi kiriting", reply_markup=location_button)


@dp.message(Registration.location)
async def phone_number_function(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.location)
    await message.answer("Hamma ma'lumotingiz qabul qilindi", reply_markup=main_button_lang)
    await state.clear()


# uzbek tili
@dp.message(F.text == "uzbek tili")
async def uz_language(mesagge: types.Message):
    await mesagge.answer("Siz Uzbek tilini tanladingiz", reply_markup=main_menu_uzbek)


# rus tili
@dp.message(F.text == "rus tili")
async def fast(message: types.Message):
    await message.answer(text="Вы выбрали русский", reply_markup=main_menu_rus)



#tillar
@dp.message(F.text == "Язык")
async def til(message: types.Message):
    await message.answer("Вы вернулись, чтобы изменить язык", reply_markup=main_button_lang)


@dp.message(F.text == "Tillar")
async def til(message: types.Message):
    await message.answer("Siz tilni ozgartirishga qaytingiz", reply_markup=main_button_lang)


#information
@dp.message(F.text == "Information")
async def til(message: types.Message):
    photo = "https://telegra.ph/file/cc58ab8cc433f77db0169.jpg"
    await message.answer_photo(photo=photo, caption="Bu bot Mars it school o'uvchisi tomonidan yaratilgan", reply_markup=mars_itschool)
    
@dp.message(F.text == "Информация")
async def til(message: types.Message):
    photo = "https://telegra.ph/file/cc58ab8cc433f77db0169.jpg"
    await message.answer_photo(photo=photo, caption="Этот бот был создан школой Mars it School", reply_markup=mars_itschool_rus)


    
#saitga kirish    
@dp.callback_query(F.data == "sait")
async def bekor(callbaack: CallbackQuery):
    await callbaack.answer(text="Siz buyurtmani bekor qildingiz")

#kurs
@dp.message(F.text == "Kurs")
async def til(message: types.Message):
    await message.answer("Siz tilni ozgartirishga qaytingiz", reply_markup=kurs_menu_uzbek) 

@dp.message(F.text == "Курсы")
async def til(message: types.Message):
    await message.answer("Вы вернулись, чтобы изменить язык", reply_markup=kurs_menu_rus) 
    
    
    
#orqaga qaytish    
@dp.message(F.text == "Orqaga")
async def orqaga(message: types.Message):
    await message.answer("Siz menyuga qaytingiz", reply_markup=main_menu_uzbek)    
 
@dp.message(F.text == "Orqaga qaytish")
async def orqaga(message: types.Message):
    await message.answer("Kurs bolimiga qaytingiz", reply_markup=kurs_menu_uzbek)   
 
@dp.message(F.text == "Orqaga Qaytish")
async def orqaga(message: types.Message):
    await message.answer("Fronted bolimiga qaytingiz", reply_markup=Fronted)
    
@dp.message(F.text == "orqaga qaytish")
async def orqaga(message: types.Message):
    await message.answer("Backend bolimiga qaytingiz", reply_markup=Backend)         
 
 
@dp.message(F.text == "orqaga Qaytish")
async def orqaga(message: types.Message):
    await message.answer("Mobile dasturlash bolimiga qaytingiz", reply_markup=Mobile_dasturlash) 
    
     
 
 
 
    
@dp.message(F.text == "Назад")
async def orqaga(message: types.Message):
    await message.answer("Вы вернулись в меню", reply_markup=main_menu_rus)

@dp.message(F.text == "назад")
async def orqaga(message: types.Message):
    await message.answer("Вернуться в раздел Бэкэнд", reply_markup=Backend_rus)       
    
@dp.message(F.text == "Возвращаться")
async def orqaga(message: types.Message):
    await message.answer("Вернуться в раздел курса", reply_markup=kurs_menu_rus)            
    
@dp.message(F.text == "возвращаться")
async def orqaga(message: types.Message):
    await message.answer("Вернуться в раздел Фронтенд", reply_markup=Fronted_rus)  


@dp.message(F.text == "ВозвращатьсЯ")
async def orqaga(message: types.Message):
    await message.answer("Вернуться в раздел Мобильное программирование", reply_markup=Mobile_dasturlash_rus) 
    

    
     
    




#Menyuga qaytihs
@dp.message(F.text == "Asosiy Menyuga qaytish")
async def orqaga(message: types.Message):
    await message.answer("Siz menyuga qaytingiz", reply_markup=main_menu_uzbek)
    
    
@dp.message(F.text == "Вернуться в главное меню")
async def orqaga(message: types.Message):
    await message.answer("Вы вернулись в меню", reply_markup=main_menu_rus)       
          
    
        

#Fronted
@dp.message(F.text == "Fronted")
async def orqaga(message: types.Message):
    await message.answer("Fronted ga Xush kelibsiz", reply_markup=Fronted)    


@dp.message(F.text == "Фронтенд")
async def orqaga(message: types.Message):
    await message.answer("Добро пожаловать в Фронтед", reply_markup=Fronted_rus)            
      
      
#backend           
@dp.message(F.text == "Backend")
async def orqaga(message: types.Message):
    await message.answer("Backend ga Xush kelibsiz", reply_markup=Backend)    


@dp.message(F.text == "Бэкэнд")
async def orqaga(message: types.Message):
    await message.answer("Добро пожаловать в Бэкэнд", reply_markup=Backend_rus)  


#Mobile dasturlash
@dp.message(F.text == "Mobile dasturlash")
async def orqaga(message: types.Message):
    await message.answer("Mobile dasturlash ga Xush kelibsiz", reply_markup=Mobile_dasturlash)    


@dp.message(F.text == "Мобильное программирование")
async def orqaga(message: types.Message):
    await message.answer("Добро пожаловать в Мобильное программирование", reply_markup=Mobile_dasturlash_rus)  
    
    

    
    

#kurslar
#Suniy Inteleknt
@dp.message(F.text == "Samar Badriddinov")
async def orqaga(message: types.Message):
    await message.answer("Samar Badriddinov Bolimiga ga Xush kelibsiz", reply_markup=Samar_Badriddinov1)    


@dp.message(F.text == "Самар Бадриддинов")
async def orqaga(message: types.Message):
    await message.answer("Добро пожаловать в Самар Бадриддинов Болими ", reply_markup=Samar_Badriddinov_rus)   
    
#Mobile_dasturlash 
@dp.message(F.text == "Flutter 0 dan PRO gacha")
async def orqaga(message: types.Message):
    await message.answer("Flutter 0 dan PRO gacha Bolimiga ga Xush kelibsiz", reply_markup=Flutter_gacha)   
    



@dp.message(F.text == "Флаттер от 0 до PRO")
async def orqaga(message: types.Message):
    await message.answer("Добро пожаловать в Флаттер от 0 до PRO Болими ", reply_markup=Flutter_gacha_rus)

      
      
#Backend
@dp.message(F.text == "Python")
async def orqaga(message: types.Message):
    await message.answer("Python Bolimiga ga Xush kelibsiz", reply_markup=Python)   
    
    
@dp.message(F.text == "C++")
async def orqaga(message: types.Message):
    await message.answer("C++ Bolimiga ga Xush kelibsiz", reply_markup=C)        

@dp.message(F.text == "PHP")
async def orqaga(message: types.Message):
    await message.answer("PHP Bolimiga ga Xush kelibsiz", reply_markup=php)  

@dp.message(F.text == "Java")
async def orqaga(message: types.Message):
    await message.answer("Java Bolimiga ga Xush kelibsiz", reply_markup=Java) 


@dp.message(F.text == "Питон")
async def orqaga(message: types.Message):
    await message.answer("Добро пожаловать в Питон Болими ", reply_markup=Python_rus)
    
@dp.message(F.text == "C++")
async def orqaga(message: types.Message):
    await message.answer("Добро пожаловать в C++ Болими ", reply_markup=C_rus) 
    
    
@dp.message(F.text == "PHP")
async def orqaga(message: types.Message):
    await message.answer("Добро пожаловать в PHP Болими ", reply_markup=php_rus)                       
      
@dp.message(F.text == "Джава")
async def orqaga(message: types.Message):
    await message.answer("Добро пожаловать в Джава Болими ", reply_markup=Java_rus)       




#Fronted
@dp.message(F.text == "Frontend (Saud Abdulwahed)")
async def orqaga(message: types.Message):
    await message.answer("Python Bolimiga ga Xush kelibsiz", reply_markup=Frontend_Saud_Abdulwahed)   
    
    
@dp.message(F.text == "HTML va CSS")
async def orqaga(message: types.Message):
    await message.answer("HTML va CSS Bolimiga ga Xush kelibsiz", reply_markup=HTMLvaCSS)        

@dp.message(F.text == "JavaScript (Saidbek Arislonov)")
async def orqaga(message: types.Message):
    await message.answer("JavaScript (Saidbek Arislonov) Bolimiga ga Xush kelibsiz", reply_markup=JavaScript_Saidbek_Arislonov)  

    





@dp.message(F.text == "Фронтенд (Сауд Абдулвахед)")
async def orqaga(message: types.Message):
    await message.answer("Добро пожаловать в Питон Болими ", reply_markup=Frontend_Saud_Abdulwahed_rus)
    
@dp.message(F.text == "HTML и CSS")
async def orqaga(message: types.Message):
    await message.answer("Добро пожаловать в HTML и CSS Болими ", reply_markup=HTMLvaCSS_rus) 
    
    
@dp.message(F.text == "JavaScript (Саидбек Арислонов)")
async def orqaga(message: types.Message):
    await message.answer("Добро пожаловать в JavaScript (Саидбек Арислонов) Болими ", reply_markup=JavaScript_Saidbek_Arislonov_rus)                       










#Mobile_dasturlash
@dp.message(F.text == "1-modul")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("mobile_1.mp4")
    await message.answer_video(video=mek, caption="Flutter 0 dan 1 dars Kirish\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "2-modul")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("mobile_2.mp4")
    await message.answer_video(video=mek, caption="Flutter 0 dan. 2-Dars. Widgets beginner, Text fonts, Stateful vs Stateless\n\n\n👉https://t.me/Kurs577_bot")        







#Mobile_dasturlash_rus
@dp.message(F.text == "1-модуль")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("mobile_1.mp4")
    await message.answer_video(video=mek, caption="Урок флаттера 0 из 1 Войти\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "2-модуль")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("mobile_2.mp4")
    await message.answer_video(video=mek, caption="Из Флаттера 0. Урок 2. Виджеты для начинающих, Текстовые шрифты, Stateful vs Stateless\n\n\n👉https://t.me/Kurs577_bot")   



         
    
    
    
#python
@dp.message(F.text == "1 dars")
async def Samar_Badriddinov(message: types.Message):
    mek1 = FSInputFile("python_1.mp4")
    await message.answer_video(video=mek1, caption="Python dasturlash darslari | 1-dars | Pythonni o'rnatish va muhitni sozlash\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "2 dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("python_2.mp4")
    await message.answer_video(video=mek, caption="Python dasturlash darslari | 2-dars | Chiqish ma'lumoti\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "3 dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("python_3.mp4")
    await message.answer_video(video=mek, caption="Python dasturlash darslari | 3-dars | Ma`lumot turlari va o’zgaruvchilar\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "4 dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("python_4.mp4")
    await message.answer_video(video=mek, caption="Python dasturlash darslari | 4-dars | Ma`lumot turlari va o’zgaruvchilar\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "5 dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("python_5.mp4")
    await message.answer_video(video=mek, caption="Python dasturlash darslari | 5-dars | Arifmetik operatorlar\n\n\n👉https://t.me/Kurs577_bot") 

@dp.message(F.text == "6 dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("python_6.mp4")
    await message.answer_video(video=mek, caption="Python dasturlash darslari | 6-dars | Chiziqli algoritmlar\n\n\n👉https://t.me/Kurs577_bot")        
    
    
#python rus    
@dp.message(F.text == "1 Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("python_1.mp4")
    await message.answer_video(video=mek, caption="Уроки программирования на Python | Урок 1 | Установка Python и настройка среды\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "2 Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("python_2.mp4")
    await message.answer_video(video=mek, caption="Уроки программирования на Python | Урок 2 | Выходная информация\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "3 Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("python_3.mp4")
    await message.answer_video(video=mek, caption="Уроки программирования на Python | Урок 3 Часть 1 | Типы данных и переменные\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "4 Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("python_4.mp4")
    await message.answer_video(video=mek, caption="Уроки программирования на Python | Урок 4 | Типы данных и переменные\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "5 Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("python_5.mp4")
    await message.answer_video(video=mek, caption="Уроки программирования на Python | Урок 5 | Арифметические операторы\n\n\n👉https://t.me/Kurs577_bot") 

@dp.message(F.text == "6 Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("python_6.mp4")
    await message.answer_video(video=mek, caption="Уроки программирования на Python | Урок 6 | Линейные алгоритмы\n\n\n👉https://t.me/Kurs577_bot")        
    
    
    
#C++
@dp.message(F.text == "#1 dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("c_1.mp4")
    await message.answer_video(video=mek, caption="C++ ga kirish - C++da dasturlash darslari\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "#2 dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("c_2.mp4")
    await message.answer_video(video=mek, caption="Dastlabki buyruqlar - C++da dasturlash darslari\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "#3 dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("c_3.mp4")
    await message.answer_video(video=mek, caption="O'zgaruvchilar - C++da dasturlash darslari\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "#4 dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("c_4.mp4")
    await message.answer_video(video=mek, caption=" Increament va decreament amallari - C++da dasturlash darslari\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "#5 dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("c_5.mp4")
    await message.answer_video(video=mek, caption="Haqiqiy sonlar - C++da dasturlash darslari\n\n\n👉https://t.me/Kurs577_bot") 

@dp.message(F.text == "#6 dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("c_6.mp4")
    await message.answer_video(video=mek, caption=" Mantiqiy amallar - C++da dasturlash darslari\n\n\n👉https://t.me/Kurs577_bot")        
    
    
#c++ rus    
@dp.message(F.text == "#1 Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("c_1.mp4")
    await message.answer_video(video=mek, caption="Введение в C++ - уроки программирования на C++\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "#2 Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("c_2.mp4")
    await message.answer_video(video=mek, caption="Основные команды — уроки программирования на C++\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "#3 Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("c_3.mp4")
    await message.answer_video(video=mek, caption="Переменные — Уроки программирования на C++\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "#4 Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("c_4.mp4")
    await message.answer_video(video=mek, caption="Операции увеличения и уменьшения — уроки программирования на C++\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "#5 Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("c_5.mp4")
    await message.answer_video(video=mek, caption="Действительные числа — Учебники по программированию на C++\n\n\n👉https://t.me/Kurs577_bot") 

@dp.message(F.text == "#6 Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("c_6.mp4")
    await message.answer_video(video=mek, caption="Логические операции — уроки программирования на C++\n\n\n👉https://t.me/Kurs577_bot")     
    
#php    
@dp.message(F.text == "1 modul")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("php_1.mp4")
    await message.answer_video(video=mek, caption="1-dars. PHP da dastlabki loyihani yaratish\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "2 modul")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("php_2.mp4")
    await message.answer_video(video=mek, caption="2-dars. PHP da o'zgaruvchilar\n\n\n👉https://t.me/Kurs577_bot")        


#php_rus
@dp.message(F.text == "1 модуль")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("php_1.mp4")
    await message.answer_video(video=mek, caption="Урок 1. Создание первоначального проекта на PHP\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "2 модуль")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("php_2.mp4")
    await message.answer_video(video=mek, caption="Урок 2. Переменные в PHP\n\n\n👉https://t.me/Kurs577_bot") 
        
        
        
#java
@dp.message(F.text == "1_dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("java_1.mp4")
    await message.answer_video(video=mek, caption="Java Darslari #1-dars Java dasturlash tili haqida va kerakli dasturlarni o'rnatish\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "2_dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("java_2.mp4")
    await message.answer_video(video=mek, caption="Java Darslari #2 dars Javada bizning birinchi kodimiz va console bilan ishlash\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "3_dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("java_3.mp4")
    await message.answer_video(video=mek, caption="Java Darslari #3 dars Javada o’zgaruvchilar haqida va ular bilan ishlash\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "4_dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("java_4.mp4")
    await message.answer_video(video=mek, caption="Java Darslari #4 dars Javada ma’lumot turlari haqida data types\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "5_dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("java_5.mp4")
    await message.answer_video(video=mek, caption="Java Darslari #5 dars Javada Ineteger ma'lumot turlari bilan ishlash va matematik operatorlar\n\n\n👉https://t.me/Kurs577_bot") 

@dp.message(F.text == "6_dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("java_6.mp4")
    await message.answer_video(video=mek, caption="Java Darslari #6 dars Javada float va double data type haqida, type casting\n\n\n👉https://t.me/Kurs577_bot")        
    
    
#java rus    
@dp.message(F.text == "1-Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("java_1.mp4")
    await message.answer_video(video=mek, caption="Уроки Java №1 Урок о языке программирования Java и установке необходимых программ\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "2-Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("java_2.mp4")
    await message.answer_video(video=mek, caption="Уроки Java №2 Урок Наш первый код на Java и работа с консолью\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "3-Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("java_3.mp4")
    await message.answer_video(video=mek, caption="Уроки Java №3. Урок о переменных и работе с ними в Java\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "4-Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("java_4.mp4")
    await message.answer_video(video=mek, caption="Уроки Java №4, урок о типах данных в Java\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "5-Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("java_5.mp4")
    await message.answer_video(video=mek, caption="Уроки Java №5 Урок Работа с целочисленными типами данных и математическими операторами в Java\n\n\n👉https://t.me/Kurs577_bot") 

@dp.message(F.text == "6-Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("java_6.mp4")
    await message.answer_video(video=mek, caption="Уроки Java №6, урок о типах данных float и double в Java, приведение типов\n\n\n👉https://t.me/Kurs577_bot")     
 
 
 
 
#fronted
@dp.message(F.text == "dars 1")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("fron_1.mp4")
    await message.answer_video(video=mek, caption="Frontend. 1-dars. Kirish\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "dars 2")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("fron_2.mp4")
    await message.answer_video(video=mek, caption="Frontend. 2-dars. Fayllar, html, htmldagi kodni brauzerda ochish, teglar, H1 tegi\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "dars 3")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("fron_3.mp4")
    await message.answer_video(video=mek, caption="Frontend. 3-dars. Rasm, link, list, sarlavha, paragraf va kichik teglar\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "dars 4")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("fron_4.mp4")
    await message.answer_video(video=mek, caption="Frontend. 4-dars. Table, form, video, audio, block elementlari\n\n\n👉https://t.me/Kurs577_bot") 
          
    
    
#fronted rus    
@dp.message(F.text == "Урок 1")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("fron_1.mp4")
    await message.answer_video(video=mek, caption="Внешний интерфейс. Урок 1. Входить\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "Урок 2")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("fron_2.mp4")
    await message.answer_video(video=mek, caption="Внешний интерфейс. Урок 2. Файлы, html, открытый код в html в браузере, теги, тег H1\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "Урок 3")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("fron_3.mp4")
    await message.answer_video(video=mek, caption="Внешний интерфейс. Урок 3. Изображение, ссылка, список, заголовок, абзац и небольшие теги\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "Урок 4")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("fron_4.mp4")
    await message.answer_video(video=mek, caption="Внешний интерфейс. Урок 4. Таблица, форма, видео, аудио, блочные элементы\n\n\n👉https://t.me/Kurs577_bot") 
    
    
    
#html and css   
@dp.message(F.text == "1-dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("html_1.mp4")
    await message.answer_video(video=mek, caption="1 Soatda HTMLni o'rganamiz\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "2-dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("html.2.mp4")
    await message.answer_video(video=mek, caption="CSS ni o'rganamiz 1-qism\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "3-dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("html_3.mp4")
    await message.answer_video(video=mek, caption="CSS ni o'rganamiz 2-Dars\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "4-dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("html_4.mp4")
    await message.answer_video(video=mek, caption="CSS ni o'rganamiz 3-Dars\n\n\n👉https://t.me/Kurs577_bot") 
         
@dp.message(F.text == "5-dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("html_5.mp4")
    await message.answer_video(video=mek, caption="CSS Cheatsheet\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "6-dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("html_6.mp4")
    await message.answer_video(video=mek, caption="3 Sahifali website yaratamiz\n\n\n👉https://t.me/Kurs577_bot")           
    
    
#html and css rus    
@dp.message(F.text == "1-Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("html_1.mp4")
    await message.answer_video(video=mek, caption="Выучим HTML за 1 час\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "2-Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("html.2.mp4")
    await message.answer_video(video=mek, caption="Давайте изучим CSS, часть 1.\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "3-Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("html_3.mp4")
    await message.answer_video(video=mek, caption="Давайте изучим урок CSS 2.\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "4-Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("html_4.mp4")
    await message.answer_video(video=mek, caption="Давайте изучим урок CSS 3.\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "5-Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("html_5.mp4")
    await message.answer_video(video=mek, caption="Шпаргалка по CSS\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "6-Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("html_6.mp4")
    await message.answer_video(video=mek, caption="Создадим 3-страничный сайт\n\n\n👉https://t.me/Kurs577_bot")  
                 



                 
#javascript
@dp.message(F.text == "#1_Dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("javas_1.mp4")
    await message.answer_video(video=mek, caption="Javascript - 1 qism. JS haqida ma`lumot, 'var' kalit so`zi\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "#2_dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("javas_2.mp4")
    await message.answer_video(video=mek, caption="Javascript - 2 qism. String, Number, Boolean. Matematik hisoblash\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "#3_Dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("javas_3.mp4")
    await message.answer_video(video=mek, caption="Javascript - 3 qism. Javascript yordamida BMI (body mass index) hisoblash\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "#4_dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("javas_4.mp4")
    await message.answer_video(video=mek, caption="Javascript - 4 qism. If Else tushunchasi\n\n\n👉https://t.me/Kurs577_bot") 
         
@dp.message(F.text == "#5_Dars")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("javas_5.mp4")
    await message.answer_video(video=mek, caption="JavaScript va ES6 1 soatda - Boshlang`ich ko`nikmalar\n\n\n👉https://t.me/Kurs577_bot") 
    
         
    
    
#javascript rus    
@dp.message(F.text == "#1-Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("javas_1.mp4")
    await message.answer_video(video=mek, caption="Javascript. Часть 1. Информация JS, ключевое слово «var»\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "#2-Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("javas.2.mp4")
    await message.answer_video(video=mek, caption="Javascript - Часть 2. Строка, Число, Логическое значение. Математический расчет\n\n\n👉https://t.me/Kurs577_bot")
    
@dp.message(F.text == "#3-Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("javas_3.mp4")
    await message.answer_video(video=mek, caption="Javascript - 3 части. Рассчитать ИМТ (индекс массы тела) c помощью JavaScript\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "#4-Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("javas_4.mp4")
    await message.answer_video(video=mek, caption="Javascript - 4 части. Концепция «Если бы еще»\n\n\n👉https://t.me/Kurs577_bot") 
    
@dp.message(F.text == "#5-Урок")
async def Samar_Badriddinov(message: types.Message):
    mek = FSInputFile("javas_5.mp4")
    await message.answer_video(video=mek, caption="JavaScript и ES6 за 1 час — Базовые навыки\n\n\n👉https://t.me/Kurs577_bot") 
 
                                  