from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_button_lang = [
    [KeyboardButton(text="uzbek tili"), KeyboardButton(text="rus tili")]
]
main_button_lang = ReplyKeyboardMarkup(keyboard=main_button_lang, resize_keyboard=True)


#chatgpt
chat_gpt = [
    [KeyboardButton(text="Chiqish")],
    
]
chat_gpt_rus = [
    [KeyboardButton(text="Chiqish")],
    
]

chat_gpt = ReplyKeyboardMarkup(keyboard=chat_gpt, resize_keyboard=True)

chat_gpt_rus = ReplyKeyboardMarkup(keyboard=chat_gpt_rus, resize_keyboard=True)


# menu_uzbek
main_menu_uzbek = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Kurs")],
    [KeyboardButton(text="Information")],
    [KeyboardButton(text="Yordam"), KeyboardButton(text="Tillar")],
])


kurs_menu_uzbek = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Fronted"), KeyboardButton(text="Backend")],
    [KeyboardButton(text="Mobile dasturlash")],
    [KeyboardButton(text="Orqaga")]
])


# menu_rus
main_menu_rus = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Курсы")],
    [KeyboardButton(text="Информация")],
    [KeyboardButton(text="Помощь"), KeyboardButton(text="Язык")],
    

])


kurs_menu_rus = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Фронтенд"), KeyboardButton(text="Бэкэнд")],
    [KeyboardButton(text="Мобильное программирование")],
    [KeyboardButton(text="Назад")]
])



#sait
mars_itschool = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Saitga otish", url="https://marsit.uz/"), InlineKeyboardButton(text="YouTube", url="https://www.youtube.com/@marsitschool7823")],
    [InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/mars_it_school/")]
])

mars_itschool_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Киньте на сайт", url="https://marsit.uz/"), InlineKeyboardButton(text="YouTube", url="https://www.youtube.com/@marsitschool7823")],
    [InlineKeyboardButton(text="Инстаграм", url="https://www.instagram.com/mars_it_school/")]
])



# #karta
# card_ru = [
#     [KeyboardButton(text="УзКард"), KeyboardButton(text="Хумо")]
# ]

# card_ru = ReplyKeyboardMarkup(keyboard=card_ru, resize_keyboard=True)

# card_uz = [
#     [KeyboardButton(text="UzCard"), KeyboardButton(text="Humo")]
# ]

# card_uz = ReplyKeyboardMarkup(keyboard=card_uz, resize_keyboard=True)





#Fronted
Fronted = [
    [KeyboardButton(text="Frontend (Saud Abdulwahed)"), KeyboardButton(text="HTML va CSS")],
    [KeyboardButton(text="JavaScript (Saidbek Arislonov)")],
    [KeyboardButton(text="Orqaga qaytish"), KeyboardButton(text="Asosiy Menyuga qaytish")],
]

Fronted = ReplyKeyboardMarkup(keyboard=Fronted, resize_keyboard=True)


Fronted_rus = [
    [KeyboardButton(text="Фронтенд (Сауд Абдулвахед)"), KeyboardButton(text="HTML и CSS")],
    [KeyboardButton(text="JavaScript (Саидбек Арислонов)")],
    [KeyboardButton(text="Возвращаться"), KeyboardButton(text="Вернуться в главное меню")],
]

Fronted_rus = ReplyKeyboardMarkup(keyboard=Fronted_rus, resize_keyboard=True)



#Backend
Backend = [
    [KeyboardButton(text="Python"), KeyboardButton(text="C++")],
    [KeyboardButton(text="PHP"), KeyboardButton(text="Java")],
    [KeyboardButton(text="Orqaga qaytish"), KeyboardButton(text="Asosiy Menyuga qaytish")],
]

Backend = ReplyKeyboardMarkup(keyboard=Backend, resize_keyboard=True)


Backend_rus = [
    [KeyboardButton(text="Питон"), KeyboardButton(text="С++")],
    [KeyboardButton(text="PHP"), KeyboardButton(text="Джава")],
    [KeyboardButton(text="Возвращаться"), KeyboardButton(text="Вернуться в главное меню")],
]

Backend_rus = ReplyKeyboardMarkup(keyboard=Backend_rus, resize_keyboard=True)






#Mobile_dasturlash
Mobile_dasturlash = [
    [KeyboardButton(text="Flutter 0 dan PRO gacha")],
    [KeyboardButton(text="Orqaga qaytish"), KeyboardButton(text="Asosiy Menyuga qaytish")],
]

Mobile_dasturlash = ReplyKeyboardMarkup(keyboard=Mobile_dasturlash, resize_keyboard=True)


Mobile_dasturlash_rus = [
    [KeyboardButton(text="Флаттер от 0 до PRO")],
    [KeyboardButton(text="Возвращаться"), KeyboardButton(text="Вернуться в главное меню")],
]

Mobile_dasturlash_rus = ReplyKeyboardMarkup(keyboard=Mobile_dasturlash_rus, resize_keyboard=True)




#Sun'iy Intellekt
Suniy_Intellekt = [
    [KeyboardButton(text="Samar Badriddinov")],
    [KeyboardButton(text="Orqaga qaytish"), KeyboardButton(text="Asosiy Menyuga qaytish")],
]

Suniy_Intellekt  = ReplyKeyboardMarkup(keyboard=Suniy_Intellekt, resize_keyboard=True)


Suniy_Intellekt_rus = [
    [KeyboardButton(text="Самар Бадриддинов")],
    [KeyboardButton(text="Возвращаться"), KeyboardButton(text="Вернуться в главное меню")],
]

Suniy_Intellekt_rus = ReplyKeyboardMarkup(keyboard=Suniy_Intellekt_rus, resize_keyboard=True)









#Kurs_darslari

#Sun'iy Intellekt
Samar_Badriddinov2 = [
    [KeyboardButton(text="1-Dars"), KeyboardButton(text="2-Dars")],
    [KeyboardButton(text="3-Dars"), KeyboardButton(text="4-Dars")],
    [KeyboardButton(text="5-Dars")],
    [KeyboardButton(text="Orrqaga Qaytish"), KeyboardButton(text="Asosiy Menyuga qaytish")],
]

Samar_Badriddinov1 = ReplyKeyboardMarkup(keyboard=Samar_Badriddinov2, resize_keyboard=True)


Samar_Badriddinov_rus = [
    [KeyboardButton(text="1 урок"), KeyboardButton(text="2 урок")],
    [KeyboardButton(text="3 урок"), KeyboardButton(text="4 урок")],
    [KeyboardButton(text="5 урок")],
    [KeyboardButton(text="Воозвращаться"), KeyboardButton(text="Вернуться в главное меню")],
]

Samar_Badriddinov_rus = ReplyKeyboardMarkup(keyboard=Samar_Badriddinov_rus, resize_keyboard=True)




#Mobile_dasturlash
Flutter_gacha = [
    [KeyboardButton(text="1-modul"), KeyboardButton(text="2-modul")],
    [KeyboardButton(text="orqaga Qaytish"), KeyboardButton(text="Asosiy Menyuga qaytish")],
]

Flutter_gacha = ReplyKeyboardMarkup(keyboard=Flutter_gacha, resize_keyboard=True)







Flutter_gacha_rus = [
    [KeyboardButton(text="1-модуль"), KeyboardButton(text="2-модуль")],
    [KeyboardButton(text="ВозвращатьсЯ"), KeyboardButton(text="Вернуться в главное меню")],
]

Flutter_gacha_rus = ReplyKeyboardMarkup(keyboard=Flutter_gacha_rus, resize_keyboard=True)



Kotlin_dasturlash_rus = [
    [KeyboardButton(text="1-урок"), KeyboardButton(text="2-урок")],
    [KeyboardButton(text="3-урок"), KeyboardButton(text="4-урок")],
    [KeyboardButton(text="5-урок"), KeyboardButton(text="6-урок")],
    [KeyboardButton(text="ВозвращатьсЯ"), KeyboardButton(text="Вернуться в главное меню")],
]

Kotlin_dasturlash_rus = ReplyKeyboardMarkup(keyboard=Kotlin_dasturlash_rus, resize_keyboard=True)




#Backend
Python = [
    [KeyboardButton(text="1 dars"), KeyboardButton(text="2 dars")],
    [KeyboardButton(text="3 dars"), KeyboardButton(text="4 dars")],
    [KeyboardButton(text="5 dars"), KeyboardButton(text="6 dars")],
    [KeyboardButton(text="orqaga qaytish"), KeyboardButton(text="Asosiy Menyuga qaytish")],
]

Python = ReplyKeyboardMarkup(keyboard=Python, resize_keyboard=True)


Python_rus = [
    [KeyboardButton(text="1 Урок"), KeyboardButton(text="2 Урок")],
    [KeyboardButton(text="3 Урок"), KeyboardButton(text="4 Урок")],
    [KeyboardButton(text="5 Урок"), KeyboardButton(text="5 Урок")],
    [KeyboardButton(text="назад"), KeyboardButton(text="Вернуться в главное меню")],
]
Python_rus = ReplyKeyboardMarkup(keyboard=Python_rus, resize_keyboard=True)



C = [
    [KeyboardButton(text="#1 dars"), KeyboardButton(text="#2 dars")],
    [KeyboardButton(text="#3 dars"), KeyboardButton(text="#4 dars")],
    [KeyboardButton(text="#5 dars"), KeyboardButton(text="#6 dars")],
    [KeyboardButton(text="orqaga qaytish"), KeyboardButton(text="Asosiy Menyuga qaytish")],
]

C = ReplyKeyboardMarkup(keyboard=C, resize_keyboard=True)


C_rus = [
    [KeyboardButton(text="#1 Урок"), KeyboardButton(text="#2 Урок")],
    [KeyboardButton(text="#3 Урок"), KeyboardButton(text="#4 Урок")],
    [KeyboardButton(text="#5 Урок"), KeyboardButton(text="#6 Урок")],
    [KeyboardButton(text="назад"), KeyboardButton(text="Вернуться в главное меню")],
]

C_rus = ReplyKeyboardMarkup(keyboard=C_rus, resize_keyboard=True)


php = [
    [KeyboardButton(text="1 modul"), KeyboardButton(text="2 modul")],
    [KeyboardButton(text="orqaga qaytish"), KeyboardButton(text="Asosiy Menyuga qaytish")],
]

php = ReplyKeyboardMarkup(keyboard=php, resize_keyboard=True)



php_rus = [
    [KeyboardButton(text="1 модуль"), KeyboardButton(text="2 модуль")],
    [KeyboardButton(text="назад"), KeyboardButton(text="Вернуться в главное меню")],
]

php_rus = ReplyKeyboardMarkup(keyboard=php_rus, resize_keyboard=True)



Java = [
    [KeyboardButton(text="1_dars"), KeyboardButton(text="2_dars")],
    [KeyboardButton(text="3_dars"), KeyboardButton(text="4_dars")],
    [KeyboardButton(text="5_dars"), KeyboardButton(text="6_dars")],
    [KeyboardButton(text="orqaga qaytish"), KeyboardButton(text="Asosiy Menyuga qaytish")],
]

Java = ReplyKeyboardMarkup(keyboard=Java, resize_keyboard=True)


Java_rus = [
    [KeyboardButton(text="1-Урок"), KeyboardButton(text="2-Урок")],
    [KeyboardButton(text="3-Урок"), KeyboardButton(text="4-Урок")],
    [KeyboardButton(text="5-Урок"), KeyboardButton(text="6-Урок")],
    [KeyboardButton(text="назад"), KeyboardButton(text="Вернуться в главное меню")],
]

Java_rus = ReplyKeyboardMarkup(keyboard=Java_rus, resize_keyboard=True)



#Fronted
Frontend_Saud_Abdulwahed = [
    [KeyboardButton(text="dars 1"), KeyboardButton(text="dars 2")],
    [KeyboardButton(text="dars 3"), KeyboardButton(text="dars 4")],
    [KeyboardButton(text="Orqaga Qaytish"), KeyboardButton(text="Asosiy Menyuga qaytish")],
]

Frontend_Saud_Abdulwahed = ReplyKeyboardMarkup(keyboard=Frontend_Saud_Abdulwahed, resize_keyboard=True)


Frontend_Saud_Abdulwahed_rus = [
    [KeyboardButton(text="Урок 1"), KeyboardButton(text="Урок 2")],
    [KeyboardButton(text="Урок 3"), KeyboardButton(text="Урок 4")],
    [KeyboardButton(text="возвращаться"), KeyboardButton(text="Вернуться в главное меню")],
]

Frontend_Saud_Abdulwahed_rus = ReplyKeyboardMarkup(keyboard=Frontend_Saud_Abdulwahed_rus, resize_keyboard=True)



HTMLvaCSS = [
    [KeyboardButton(text="1-dars"), KeyboardButton(text="2-dars")],
    [KeyboardButton(text="3-dars"), KeyboardButton(text="4-dars")],
    [KeyboardButton(text="5-dars"), KeyboardButton(text="6-dars")],
    [KeyboardButton(text="Orqaga Qaytish"), KeyboardButton(text="Asosiy Menyuga qaytish")],
]

HTMLvaCSS = ReplyKeyboardMarkup(keyboard=HTMLvaCSS, resize_keyboard=True)


HTMLvaCSS_rus = [
    [KeyboardButton(text="1-Урок"), KeyboardButton(text="2-Урок")],
    [KeyboardButton(text="3-Урок"), KeyboardButton(text="4-Урок")],
    [KeyboardButton(text="5-Урок"), KeyboardButton(text="6-Урок")],
    [KeyboardButton(text="возвращаться"), KeyboardButton(text="Вернуться в главное меню")],
]

HTMLvaCSS_rus = ReplyKeyboardMarkup(keyboard=HTMLvaCSS_rus, resize_keyboard=True)



JavaScript_Saidbek_Arislonov = [
    [KeyboardButton(text="#1_Dars"), KeyboardButton(text="#2_dars")],
    [KeyboardButton(text="#3_Dars"), KeyboardButton(text="#4_dars")],
    [KeyboardButton(text="#5_Dars")],
    [KeyboardButton(text="Orqaga Qaytish"), KeyboardButton(text="Asosiy Menyuga qaytish")],
]

JavaScript_Saidbek_Arislonov = ReplyKeyboardMarkup(keyboard=JavaScript_Saidbek_Arislonov, resize_keyboard=True)


JavaScript_Saidbek_Arislonov_rus = [
    [KeyboardButton(text="#1-Урок"), KeyboardButton(text="#2-Урок")],
    [KeyboardButton(text="#3-Урок"), KeyboardButton(text="#4-Урок")],
    [KeyboardButton(text="#5-Урок")],
    [KeyboardButton(text="возвращаться"), KeyboardButton(text="Вернуться в главное меню")],
]

JavaScript_Saidbek_Arislonov_rus = ReplyKeyboardMarkup(keyboard=JavaScript_Saidbek_Arislonov_rus, resize_keyboard=True)



