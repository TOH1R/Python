from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_button_lang = [
    [KeyboardButton(text="uzbek tili"), KeyboardButton(text="rus tili")]
]
main_button_lang = ReplyKeyboardMarkup(keyboard=main_button_lang, resize_keyboard=True)

# yesno
main_button_yesno_shirinliklar = [
    [InlineKeyboardButton(text="Sotib olish", callback_data="olish"),
     InlineKeyboardButton(text="Bekor qilish", callback_data="bekor")]
]

yesno_uzbek_shirinlikar = InlineKeyboardMarkup(inline_keyboard=main_button_yesno_shirinliklar)

main_button_yesno_FastFood = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="Olish"),
     InlineKeyboardButton(text="Bekor Qilish", callback_data="Bekor")]
]

yesno_uzbek_FastFood = InlineKeyboardMarkup(inline_keyboard=main_button_yesno_FastFood)

main_button_yesno_Ichimliklar = [
    [InlineKeyboardButton(text="sotib olish", callback_data="sotib"),
     InlineKeyboardButton(text="bekor qilish", callback_data="bekor")]
]

yesno_uzbek_Ichimlikar = InlineKeyboardMarkup(inline_keyboard=main_button_yesno_Ichimliklar)

# menu_uzbek
main_menu_uzbek = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Menyu")],
    [KeyboardButton(text="Company Information"), KeyboardButton(text="Korzinka"),],
    [KeyboardButton(text="Info"), KeyboardButton(text="Tillar"), KeyboardButton(text="Loyiha")],
])

menu_uzbek = [
    [KeyboardButton(text="FastFood"), KeyboardButton(text="Ichimliklar"), KeyboardButton(text="Shirinliklar")],
    [KeyboardButton(text="Orqaga qaytish")]
]

menu_uzbek = ReplyKeyboardMarkup(keyboard=menu_uzbek, resize_keyboard=True)


# Karta
card_ru = [
    [KeyboardButton(text="УзКард"), KeyboardButton(text="Хумо")]
]

card_ru = ReplyKeyboardMarkup(keyboard=card_ru, resize_keyboard=True)

card_uz = [
    [KeyboardButton(text="UzCard"), KeyboardButton(text="Humo")]
]

card_uz = ReplyKeyboardMarkup(keyboard=card_uz, resize_keyboard=True)

# menu_rus
main_menu_rus = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Меню")],
    [KeyboardButton(text="Информация компании"), KeyboardButton(text="Корзина")],
    [KeyboardButton(text="Информация"), KeyboardButton(text="Язык")],

])

menu_rus = [
    [KeyboardButton(text="Быстрое питание"), KeyboardButton(text="Напитки"), KeyboardButton(text="Сладости")]
]

menu_rus = ReplyKeyboardMarkup(keyboard=menu_rus, resize_keyboard=True)

# menu_FastFood
menu_uzbek_FastFood = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Hamburger 🍔"), KeyboardButton(text="Lavash 🌯")],
    [KeyboardButton(text="SandWich 🥪"), KeyboardButton(text="Pizza 🍕")],
    [KeyboardButton(text="Hot-Dog 🌭"), KeyboardButton(text="Donar 🌮")],
    [KeyboardButton(text="Orqaga qaytish")]
])

menu_uzbek_Gamburger = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Gamburger"), KeyboardButton(text="CheesBurger")],
    [KeyboardButton(text="Big Gamburger"), KeyboardButton(text="Big CheesBurger")],
    [KeyboardButton(text="orqaga qaytish")]
])

menu_uzbek_Lavash = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Lavash"), KeyboardButton(text="Mini Lavash")],
    [KeyboardButton(text="Sirli Lavash"), KeyboardButton(text="Mini sirli Lavash")],
    [KeyboardButton(text="Tandir Lavash"), KeyboardButton(text="Tandir sirli Lavash")],
    [KeyboardButton(text="orqaga qaytish")]
])

menu_uzbek_Pizza = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Sirli Pizza"), KeyboardButton(text="Barbeku Pizza"),
     KeyboardButton(text="Tovuqli Pizza")],
    [KeyboardButton(text="Meksikancha Pizza"), KeyboardButton(text="Alfredo Pizza"),
     KeyboardButton(text="Peperoni Pizza")],
    [KeyboardButton(text="Donar Pizza"), KeyboardButton(text="Goshtli miks Pizza")],
    [KeyboardButton(text="orqaga qaytish")]
])

menu_uzbek_Hod_Dog = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="koraleviski Hod-Dog"), KeyboardButton(text="Barbeku Hod-Dog")],
    [KeyboardButton(text="Sirli Hod-Dog"), KeyboardButton(text="Hot-Dog")],
    [KeyboardButton(text="orqaga qaytish")]
])

menu_uzbek_Donar = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Mini Donar"), KeyboardButton(text="Big Donar")],
    [KeyboardButton(text="Shaurma"), KeyboardButton(text="Xaggi")],
    [KeyboardButton(text="orqaga qaytish")]
])

# menu_shirinlikar
menu_uzbek_shirinlikar = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Alpen Gold 🍫"), KeyboardButton(text="Nestle 🍫")],
    [KeyboardButton(text="Milky Way 🍫"), KeyboardButton(text="Snikers 🍫")],
    [KeyboardButton(text="Oreo 🍫"), KeyboardButton(text="M_MS 🍫")],
    [KeyboardButton(text="Orqaga qaytish")]
])

menu_uzbek_AlpenGold = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="AlpenGold\nYong'oqlik"), KeyboardButton(text="AlpenGold\nKakosli"),
     KeyboardButton(text="AlpenGold\nKapuchinoli")],
    [KeyboardButton(text="AlpenGold\nQulupnayli"), KeyboardButton(text="AlpenGold\nSutli"),
     KeyboardButton(text="AlpenGold\nOreoli")],
    [KeyboardButton(text="Orqaga qaaytish")]
])

menu_uzbek_Nestle = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Nestle\nKarameli"), KeyboardButton(text="Nestle\nSutli"),
     KeyboardButton(text="Nestle\nYong'oqli")],
    [KeyboardButton(text="Nestle\nUzumli"), KeyboardButton(text="Nestle\nVaflili")],
    [KeyboardButton(text="Orqaga qaaytish")]
])

menu_uzbek_MilkyWay = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="MilkyWay\nsutli"), KeyboardButton(text="MilkyWay\nshkoladli")],
    [KeyboardButton(text="Orqaga qaaytish")]
])

menu_uzbek_Oreo = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Oreo\nShkaladli"), KeyboardButton(text="Oreo\nQizil Velvet")],
    [KeyboardButton(text="Oreo\nSutli"), KeyboardButton(text="Oreo\nQulubnayli")],
    [KeyboardButton(text="Orqaga qaaytish")]
])

menu_uzbek_M_MS = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="M_MS\nYeryong'oqli"), KeyboardButton(text="M_MS\nShkoladli"),
     KeyboardButton(text="M_MS\nBodomli")],
    [KeyboardButton(text="M_MS\nYashil Qarsildoqli"), KeyboardButton(text="M_MS\nKok Qarsildoqli")],
    [KeyboardButton(text="Orqaga qaaytish")]
])

# menu_ichimlikar
menu_uzbek_ichimlik = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Pepsi 🥤"), KeyboardButton(text="Coca Cola 🥤")],
    [KeyboardButton(text="Fanta 🥤"), KeyboardButton(text="Tropic 🥤")],
    [KeyboardButton(text="Sprite 🥤"), KeyboardButton(text="Lipton 🥤")],
    [KeyboardButton(text="Orqaga qaytish")]
])

menu_uzbek_pepsi = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Pepsi 2L"), KeyboardButton(text="Pepsi 1.5L"), KeyboardButton(text="Pepsi 1L")],
    [KeyboardButton(text="Pepsi 0.5L"), KeyboardButton(text="Shakarsiz Pepsi")],
    [KeyboardButton(text="Orqaga Qaytish")]
])

menu_uzbek_CocaCola = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Coca Cola 1.5L"), KeyboardButton(text="Coca Cola 1L"), KeyboardButton(text="Coca Cola 0.5L")],
    [KeyboardButton(text="Milliy Cola"), KeyboardButton(text="Shakarsiz Coca Cola")],
    [KeyboardButton(text="Orqaga Qaytish")]
])

menu_uzbek_Fanta = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Fanta 1.5L"), KeyboardButton(text="Fanta 1L"), KeyboardButton(text="Fanta 0.5L")],
    [KeyboardButton(text="Orqaga Qaytish")]
])

menu_uzbek_tropic = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Tropic 1L"), KeyboardButton(text="Tropic 0.5L Mangoli"),
     KeyboardButton(text="Tropic 0.5L Guavali")],
    [KeyboardButton(text="Orqaga Qaytish")]
])

menu_uzbek_sprite = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Sprite 1.5L"), KeyboardButton(text="Sprite 1L"), KeyboardButton(text="Sprite 0.5L")],
    [KeyboardButton(text="Orqaga Qaytish")]
])

menu_uzbek_lipton = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Lipton 1.5L\nOrik"), KeyboardButton(text="Lipton 1L\nOrik"),
     KeyboardButton(text="Lipton 0.5L\nOrik")],
    [KeyboardButton(text="Lipton 1.5L\nYashil"), KeyboardButton(text="Lipton 1L\nYashil"),
     KeyboardButton(text="Lipton 0.5L\nYashil")],
    [KeyboardButton(text="Lipton 1.5L\nLimon"), KeyboardButton(text="Lipton 1L\nLimon"),
     KeyboardButton(text="Lipton 0.5L\nLimon")],
    [KeyboardButton(text="Orqaga Qaytish")]
])
