from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton




# yesno
main_button_yesno_rus_shirinliklar = [
    [InlineKeyboardButton(text="Покупка", callback_data="Покупка"), InlineKeyboardButton(text="Отмена", callback_data="Отмена")]
]

yesno_rus_shirinlikar = InlineKeyboardMarkup(inline_keyboard=main_button_yesno_rus_shirinliklar)


main_button_yesno_rus_FastFood = [
    [InlineKeyboardButton(text="ПОКУПКА", callback_data="ПОКУПКА"), InlineKeyboardButton(text="ОТМЕНА", callback_data="ОТМЕНА")]
]

yesno_rus_FastFood = InlineKeyboardMarkup(inline_keyboard=main_button_yesno_rus_FastFood)


main_button_yesno_rus_Ichimliklar = [
    [InlineKeyboardButton(text="покупка", callback_data="покупка"), InlineKeyboardButton(text="отмена", callback_data="отмена")]
]

yesno_rus_ichimliklar = InlineKeyboardMarkup(inline_keyboard=main_button_yesno_rus_Ichimliklar)




# menu_FastFood
menu_rus_FastFood = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Гамбургер 🍔"), KeyboardButton(text="Лаваш 🌯")],
    [KeyboardButton(text="Сэндвич 🥪"), KeyboardButton(text="Пицца 🍕")],
    [KeyboardButton(text="Хот-дог 🌭"), KeyboardButton(text="Донор 🌮")],
    [KeyboardButton(text="Возвращаться")]
])

menu_rus_Gamburger = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Гамбургер"), KeyboardButton(text="ЧизБургер")],
    [KeyboardButton(text="Большой Гамбургер"), KeyboardButton(text="Большой Чизбургер")],
    [KeyboardButton(text="возвращаться")]
])

menu_rus_Lavash = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Лаваш"), KeyboardButton(text="Мини Лаваш")],
    [KeyboardButton(text="Cырли лаваш"), KeyboardButton(text="Мини cырли лаваш")],
    [KeyboardButton(text="Тандыр Лаваш"), KeyboardButton(text="Cырли Тандыр Лаваш")],
    [KeyboardButton(text="возвращаться")]
])

menu_rus_Pizza = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Тайная Пицца"), KeyboardButton(text="Пицца Барбекю"),
     KeyboardButton(text="Куриная Пицца")],
    [KeyboardButton(text="Мексиканская пицца"), KeyboardButton(text="Альфредо Пицца"),
     KeyboardButton(text="Пицца пепперони")],
    [KeyboardButton(text="Донер Пицца"), KeyboardButton(text="Пицца-микс с мясом")],
    [KeyboardButton(text="возвращаться")]
])

menu_rus_Hod_Dog = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Коралевский Ход-Дог"), KeyboardButton(text="Хот-дог барбекю")],
    [KeyboardButton(text="Сирни Ход-Дог"), KeyboardButton(text="Хот-дог")],
    [KeyboardButton(text="возвращаться")]
])

menu_rus_Donar = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Мини Донар"), KeyboardButton(text="Большой донор")],
    [KeyboardButton(text="Шаурма"), KeyboardButton(text="Хагги")],
    [KeyboardButton(text="возвращаться")]
])

# menu_shirinlikar
menu_rus_shirinlikar = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Альпен Голд 🍫"), KeyboardButton(text="Нестле 🍫")],
    [KeyboardButton(text="Млечный Путь 🍫"), KeyboardButton(text="Сникерс 🍫")],
    [KeyboardButton(text="Орео 🍫"), KeyboardButton(text="М_МС 🍫")],
    [KeyboardButton(text="Возвращаться")]
])

menu_rus_AlpenGold = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="АльпенГолд\nЧокнутый"), KeyboardButton(text="АльпенГолд\nКакос"),
     KeyboardButton(text="АльпенГолд\nКапучино")],
    [KeyboardButton(text="АльпенГолд\nКлубника"), KeyboardButton(text="АльпенГолд\nМолоко"),
     KeyboardButton(text="АльпенГолд\nОрео")],
    [KeyboardButton(text="Возвраащаться")]
])

menu_rus_Nestle = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Нестле\nКарамель"), KeyboardButton(text="Нестле\nМолоко"),
     KeyboardButton(text="Нестле\nЧокнутый")],
    [KeyboardButton(text="Нестле\nГрейпфрут"), KeyboardButton(text="Нестле\nВафлями")],
    [KeyboardButton(text="Возвраащаться")]
])

menu_rus_MilkyWay = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Млечный Путь\nмолочный"), KeyboardButton(text="Млечный Путь\nШколойт")],
    [KeyboardButton(text="Возвраащаться")]
])

menu_rus_Oreo = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Орео\nШколойт"), KeyboardButton(text="Орео\nКрасный вельвет")],
    [KeyboardButton(text="Орео\nмолочный"), KeyboardButton(text="Орео\nКлубника")],
    [KeyboardButton(text="Возвраащаться")]
])

menu_rus_M_MS = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="М_МС\nАрахисом"), KeyboardButton(text="М_МС\nШколойт"),
     KeyboardButton(text="М_МС\nМиндаль")],
    [KeyboardButton(text="М_МС\nЗеленый Хрящ"), KeyboardButton(text="М_МС\nCиний Хрящ")],
    [KeyboardButton(text="Возвраащаться")]
])

# menu_ichimlikar
menu_rus_ichimlik = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Пепси 🥤"), KeyboardButton(text="Кока-Кола 🥤")],
    [KeyboardButton(text="Фанта 🥤"), KeyboardButton(text="Тропик 🥤")],
    [KeyboardButton(text="Спрайт 🥤"), KeyboardButton(text="Липтон 🥤")],
    [KeyboardButton(text="Возвращаться")]
])

menu_rus_pepsi = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Пепси 2л"), KeyboardButton(text="Пепси 1,5л"), KeyboardButton(text="Пепси 1л")],
    [KeyboardButton(text="Пепси 0,5л"), KeyboardButton(text="Пепси без сахара")],
    [KeyboardButton(text="Возвращщаться")]
])

menu_rus_CocaCola = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Кока-Кола 1,5л"), KeyboardButton(text="Кока-Кола 1л"), KeyboardButton(text="Кока-Кола 0.5л")],
    [KeyboardButton(text="Миллий кола"), KeyboardButton(text="Кока-Кола без сахара")],
    [KeyboardButton(text="Возвращщаться")]
])

menu_rus_Fanta = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Фанта 1,5л"), KeyboardButton(text="Фанта 1л"), KeyboardButton(text="Фанта 0.5л")],
    [KeyboardButton(text="Возвращщаться")]
])

menu_rus_tropic = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Тропик 1л"), KeyboardButton(text="Тропик 0.5л Манголи"),
     KeyboardButton(text="Тропик 0.5л Гуавали")],
    [KeyboardButton(text="Возвращщаться")]
])

menu_rus_sprite = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Спрайт 1.5л"), KeyboardButton(text="Спрайт 1л"), KeyboardButton(text="Спрайт 0.5л")],
    [KeyboardButton(text="Возвращщаться")]
])

menu_rus_lipton = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Липтон 1.5л\nОрик"), KeyboardButton(text="Липтон 1л\nОрик"),
     KeyboardButton(text="Липтон 0.5л\nОрик")],
    [KeyboardButton(text="Липтон 1,5л\nЗеленый"), KeyboardButton(text="Липтон 1л\nЗеленый"),
     KeyboardButton(text="Липтон 0.5л\nЗеленый")],
    [KeyboardButton(text="Липтон 1,5л\nЛимон"), KeyboardButton(text="Липтон 1л\nЛимон"),
     KeyboardButton(text="Липтон 0.5л\nЛимон")],
    [KeyboardButton(text="Возвращщаться")]
])
