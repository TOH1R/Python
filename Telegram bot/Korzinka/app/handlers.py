from aiogram import Router, filters, types, F
from aiogram.filters import state
from aiogram.types import CallbackQuery

from states import Card, Registration
from aiogram.fsm.context import FSMContext
from app.keyboard import (main_button_lang, main_menu_uzbek,
                          menu_uzbek_AlpenGold, menu_uzbek_Donar, menu_uzbek_lipton, menu_uzbek_M_MS, menu_uzbek_Oreo,
                          menu_uzbek_Lavash,
                          menu_uzbek_Pizza, menu_uzbek_pepsi, menu_uzbek_Fanta, menu_uzbek_Gamburger, menu_uzbek_sprite,
                          menu_uzbek_tropic,
                          menu_uzbek_Nestle, menu_uzbek_CocaCola, menu_uzbek_MilkyWay, menu_uzbek_Hod_Dog,
                          menu_uzbek_FastFood,
                          menu_uzbek_ichimlik, menu_uzbek_shirinlikar,
                          main_menu_rus,
                          yesno_uzbek_FastFood, yesno_uzbek_shirinlikar, yesno_uzbek_Ichimlikar, card_ru, card_uz, menu_uzbek, menu_rus)
from Rus.keyboard_rus import (menu_rus_AlpenGold, menu_rus_Donar, menu_rus_lipton, menu_rus_M_MS, menu_rus_Oreo,
                              menu_rus_Lavash,
                              menu_rus_Pizza, menu_rus_pepsi, menu_rus_Fanta, menu_rus_Gamburger, menu_rus_sprite,
                              menu_rus_tropic,
                              menu_rus_Nestle, menu_rus_CocaCola, menu_rus_MilkyWay, menu_rus_Hod_Dog,
                              menu_rus_FastFood,
                              menu_rus_ichimlik, menu_rus_shirinlikar, yesno_rus_shirinlikar,
                              yesno_rus_ichimliklar, yesno_rus_FastFood)

dp = Router()
orders = []
order = []
lst = []
list = []





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






#Menu
@dp.message(F.text == "Menyu")
async def fast(message: types.Message):
    await message.answer(text="Menyu Bolimiga Xush Kelibsiz", reply_markup=menu_uzbek)


@dp.message(F.text == "Меню")
async def fast(message: types.Message):
    await message.answer(text="Добро пожаловать в раздел меню", reply_markup=menu_rus)

# menu_FastFood
@dp.message(F.text == "FastFood")
async def fast(message: types.Message):
    await message.answer(text="FastFood bolimiga xush kelibsiz", reply_markup=menu_uzbek_FastFood)


@dp.message(F.text == "Hamburger 🍔")
async def gam(message: types.Message):
    await message.answer(text="Gamburgerlar bolimiga xush kelibsiz", reply_markup=menu_uzbek_Gamburger)


@dp.message(F.text == "Lavash 🌯")
async def lav(message: types.Message):
    await message.answer(text="Lavashlar bolimiga xush kelibsiz", reply_markup=menu_uzbek_Lavash)


@dp.message(F.text == "Pizza 🍕")
async def hot(message: types.Message):
    await message.answer(text="Hod-Dog bolimiga xush kelibsiz", reply_markup=menu_uzbek_Pizza)


@dp.message(F.text == "Donar 🌮")
async def donar(message: types.Message):
    await message.answer(text="Donarlar bolimiga xush kelibsiz", reply_markup=menu_uzbek_Donar)


@dp.message(F.text == "Hot-Dog 🌭")
async def hot(message: types.Message):
    await message.answer(text="Hot-Dog bolimiga xush kelibsiz", reply_markup=menu_uzbek_Hod_Dog)


# menu_shirinlik
@dp.message(F.text == "Shirinliklar")
async def ichimlik(message: types.Message):
    await message.answer(text="Shirinliklar bolimiga xush kelibsiz", reply_markup=menu_uzbek_shirinlikar)


@dp.message(F.text == "Alpen Gold 🍫")
async def alpen(message: types.Message):
    await message.answer(text="AlpenGold bolimiga xush kelibsiz", reply_markup=menu_uzbek_AlpenGold)


@dp.message(F.text == "Nestle 🍫")
async def Nestle(message: types.Message):
    await message.answer(text="Nestle bolimiga xush kelibsiz", reply_markup=menu_uzbek_Nestle)


@dp.message(F.text == "Milky Way 🍫")
async def milky(message: types.Message):
    await message.answer(text="Milky Way bolimiga xush kelibsiz", reply_markup=menu_uzbek_MilkyWay)


@dp.message(F.text == "Oreo 🍫")
async def oreo(message: types.Message):
    await message.answer(text="Oreo bolimiga xush kelibsiz", reply_markup=menu_uzbek_Oreo)


@dp.message(F.text == "M_MS 🍫")
async def m_ms(message: types.Message):
    await message.answer(text="Ememdes bolimiga xush kelibsiz", reply_markup=menu_uzbek_M_MS)


# menu_ichimliklar
@dp.message(F.text == "Ichimliklar")
async def ichimlik(message: types.Message):
    await message.answer(text="Ichimliklar bolimiga xush kelibsiz", reply_markup=menu_uzbek_ichimlik)


@dp.message(F.text == "Pepsi 🥤")
async def pepsi(message: types.Message):
    await message.answer(text="Pepsi bolimiga xush kelibsiz.", reply_markup=menu_uzbek_pepsi)


@dp.message(F.text == "Coca Cola 🥤")
async def cola(message: types.Message):
    await message.answer(text="Coca Cola bolimiga xush kelibsiz.", reply_markup=menu_uzbek_CocaCola)


@dp.message(F.text == "Fanta 🥤")
async def fanta(message: types.Message):
    await message.answer(text="Fanta bolimiga xush kelibsiz.", reply_markup=menu_uzbek_Fanta)


@dp.message(F.text == "Tropic 🥤")
async def tropic(message: types.Message):
    await message.answer(text="Tropic bolimiga xush kelibsiz.", reply_markup=menu_uzbek_tropic)


@dp.message(F.text == "Sprite 🥤")
async def sprite(message: types.Message):
    await message.answer(text="Sprite bolimiga xush kelibsiz.", reply_markup=menu_uzbek_sprite)


@dp.message(F.text == "Lipton 🥤")
async def lipton(message: types.Message):
    await message.answer(text="Lipton bolimiga xush kelibsiz.", reply_markup=menu_uzbek_lipton)


# yes_no_shirinliklar
@dp.callback_query(F.data == "olish")
async def sotib(callback: CallbackQuery):
    orders.append(lst[-1])
    await callback.answer(text=f"{callback.from_user.full_name} Sizni buyurtmangiz qabul qilindi.",
                          reply_markup=menu_uzbek_shirinlikar)


@dp.callback_query(F.data == "bekor")
async def bekor(callbaack: CallbackQuery):
    await callbaack.answer(text="Siz buyurtmani bekor qildingiz",
                           reply_markup=menu_uzbek_shirinlikar)


# yes_no_FastFood
@dp.callback_query(F.data == "Olish")
async def sotib(callback: CallbackQuery):
    orders.append(lst[-1])
    await callback.answer(text=f"{callback.from_user.full_name} Sizni buyurtmangiz qabul qilindi.",
                          reply_markup=menu_uzbek_FastFood)


@dp.callback_query(F.data == "Bekor")
async def bekor(callbaack: CallbackQuery):
    await callbaack.answer(text="Siz buyurtmani bekor qildingiz",
                           reply_markup=menu_uzbek_FastFood)


# yes_no_Ichimliklar
@dp.callback_query(F.data == "sotib")
async def sotib(callback: CallbackQuery):
    orders.append(lst[-1])
    await callback.answer(text=f"{callback.from_user.full_name} Sizni buyurtmangiz qabul qilindi.",
                          reply_markup=menu_uzbek_ichimlik)


@dp.callback_query(F.data == "bekor")
async def bekor(callbaack: CallbackQuery):
    await callbaack.answer(text="Siz buyurtmani bekor qildingiz",
                           reply_markup=menu_uzbek_ichimlik)


# uzbek tili
@dp.message(F.text == "uzbek tili")
async def uz_language(mesagge: types.Message):
    await mesagge.answer("Siz Uzbek tilini tanladingiz", reply_markup=main_menu_uzbek)


# rus tili
@dp.message(F.text == "rus tili")
async def fast(message: types.Message):
    await message.answer(text="Вы выбрали русский", reply_markup=main_menu_rus)


# back
@dp.message(F.text == "Orqaga qaytish")
async def back(mesagge: types.Message):
    await mesagge.answer(text="Siz Menyuga qaytiz", reply_markup=main_menu_uzbek)


@dp.message(F.text == "Orqaga Qaytish")
async def back(mesagge: types.Message):
    await mesagge.answer(text="Siz ichimlikar bolimiga qaytiz", reply_markup=menu_uzbek_ichimlik)


@dp.message(F.text == "Orqaga qaaytish")
async def back(mesagge: types.Message):
    await mesagge.answer(text="Siz shirinliklar bolimiga qaytiz", reply_markup=menu_uzbek_shirinlikar)


@dp.message(F.text == "orqaga qaytish")
async def back(mesagge: types.Message):
    await mesagge.answer(text="Siz FastFood bolimiga qaytiz", reply_markup=menu_uzbek_FastFood)



# rus tili
# menu_FastFood
@dp.message(F.text == "Быстрое питание")
async def fast(message: types.Message):
    await message.answer(text="Добро пожаловать в раздел Фастфуд", reply_markup=menu_rus_FastFood)


@dp.message(F.text == "Гамбургер 🍔")
async def gam(message: types.Message):
    await message.answer(text="Добро пожаловать в раздел гамбургеров", reply_markup=menu_rus_Gamburger)


@dp.message(F.text == "Лаваш 🌯")
async def lav(message: types.Message):
    await message.answer(text="Добро пожаловать в раздел Лаваш", reply_markup=menu_rus_Lavash)


@dp.message(F.text == "Пицца 🍕")
async def hot(message: types.Message):
    await message.answer(text="Добро пожаловать в раздел пицца", reply_markup=menu_rus_Pizza)


@dp.message(F.text == "Донор 🌮")
async def donar(message: types.Message):
    await message.answer(text="Добро пожаловать в раздел Доноры", reply_markup=menu_rus_Donar)


@dp.message(F.text == "Хот-дог 🌭")
async def hot(message: types.Message):
    await message.answer(text="Добро пожаловать в раздел хот-догов", reply_markup=menu_rus_Hod_Dog)


# menu_shirinlik
@dp.message(F.text == "Сладости")
async def ichimlik(message: types.Message):
    await message.answer(text="Добро пожаловать в раздел сладостей", reply_markup=menu_rus_shirinlikar)


@dp.message(F.text == "Альпен Голд 🍫")
async def alpen(message: types.Message):
    await message.answer(text="Добро пожаловать в раздел АльпенГолд", reply_markup=menu_rus_AlpenGold)


@dp.message(F.text == "Нестле 🍫")
async def Nestle(message: types.Message):
    await message.answer(text="Добро пожаловать в Нестле", reply_markup=menu_rus_Nestle)


@dp.message(F.text == "Млечный Путь 🍫")
async def milky(message: types.Message):
    await message.answer(text="Добро пожаловать в раздел Млечный Путь", reply_markup=menu_rus_MilkyWay)


@dp.message(F.text == "Орео 🍫")
async def oreo(message: types.Message):
    await message.answer(text="Добро пожаловать в раздел Орео", reply_markup=menu_rus_Oreo)


@dp.message(F.text == "М_МС 🍫")
async def m_ms(message: types.Message):
    await message.answer(text="Добро пожаловать в раздел Эмемдес", reply_markup=menu_rus_M_MS)


# menu_ichimliklar
@dp.message(F.text == "Напитки")
async def ichimlik(message: types.Message):
    await message.answer(text="Добро пожаловать в раздел напитков", reply_markup=menu_rus_ichimlik)


@dp.message(F.text == "Пепси 🥤")
async def pepsi(message: types.Message):
    await message.answer(text="Добро пожаловать в раздел Пепси", reply_markup=menu_rus_pepsi)


@dp.message(F.text == "Кока-Кола 🥤")
async def cola(message: types.Message):
    await message.answer(text="Добро пожаловать в раздел Кока-Колы", reply_markup=menu_rus_CocaCola)


@dp.message(F.text == "Фанта 🥤")
async def fanta(message: types.Message):
    await message.answer(text="Добро пожаловать в раздел Фанта", reply_markup=menu_rus_Fanta)


@dp.message(F.text == "Тропик 🥤")
async def tropic(message: types.Message):
    await message.answer(text="Добро пожаловать в Тропик", reply_markup=menu_rus_tropic)


@dp.message(F.text == "Спрайт 🥤")
async def sprite(message: types.Message):
    await message.answer(text="Добро пожаловать в раздел Спрайтов", reply_markup=menu_rus_sprite)


@dp.message(F.text == "Липтон 🥤")
async def lipton(message: types.Message):
    await message.answer(text="Lipton bolimiga xush kelibsiz.", reply_markup=menu_rus_lipton)


# yes_no_shirinliklar
@dp.callback_query(F.data == "Отмена")
async def cancel(callbcck: CallbackQuery):
    await callbcck.answer(text="Вы отменили свой заказ.",
                          reply_markup=menu_rus_shirinlikar)


@dp.callback_query(F.data == "Покупка")
async def cancel(callback: CallbackQuery):
    order.append(list[-1])
    await callback.answer(text=f"{callback.from_user.full_name} Ваш заказ принят.",
                          reply_markup=menu_rus_shirinlikar)


# yes_no_FastFood
@dp.callback_query(F.data == "ОТМЕНА")
async def cancel(callbcck: CallbackQuery):
    await callbcck.answer(text="Вы отменили свой заказ.",
                          reply_markup=menu_rus_FastFood)


@dp.callback_query(F.data == "ПОКУПКА")
async def cancel(callback: CallbackQuery):
    order.append(list[-1])
    await callback.answer(text=f"{callback.from_user.full_name} Ваш заказ принят.",
                          reply_markup=menu_rus_FastFood)


# yes_no_Ichimliklar
@dp.callback_query(F.data == "отмена")
async def cancel(callback: CallbackQuery):
    await callback.answer(text="Вы отменили свой заказ.",
                          reply_markup=menu_rus_ichimlik)


@dp.callback_query(F.data == "покупка")
async def cancel(callback: CallbackQuery):
    order.append(list[-1])
    await callback.answer(text=f"{callback.from_user.full_name} Ваш заказ принят.",
                          reply_markup=menu_rus_ichimlik)


# back
@dp.message(F.text == "Возвращаться")
async def back(mesagge: types.Message):
    await mesagge.answer(text="Вы возвращаетесь в Меню", reply_markup=main_menu_rus)


@dp.message(F.text == "Возвращщаться")
async def back(mesagge: types.Message):
    await mesagge.answer(text="Вы возвращаетесь в отдел напитков", reply_markup=menu_rus_ichimlik)


@dp.message(F.text == "Возвраащаться")
async def back(mesagge: types.Message):
    await mesagge.answer(text="Вы возвращаетесь в раздел десертов", reply_markup=menu_rus_shirinlikar)


@dp.message(F.text == "возвращаться")
async def back(mesagge: types.Message):
    await mesagge.answer(text="Вы возвращаетесь в раздел ФастФуд", reply_markup=menu_rus_FastFood)



# Uzbek_menu




# Info
@dp.message(F.text == "Info")
async def info(message: types.Message):
    await message.answer(
        f"Ism: {message.from_user.full_name}\nUsername: {message.from_user.username}\nID: {message.from_user.id}")


# Language
@dp.message(F.text == "Tillar")
async def lang_function(message: types.Message):
    await message.answer(text="Вы вернулись, чтобы изменить язык", reply_markup=main_button_lang)


# Commany Info
@dp.message(F.text == "Company Information")
async def lang_function(message: types.Message):
    await message.answer(
        text="Online Shop Magaziniga Xush Kelibsiz, Biz Online ishlimiz bizda xali filiallarimiz yoq, Chunki biz yaqinda Ish faoliyatimiz boshlaganmiz\n"
             "\n"
             "\n"
             "Murojat uchun: +998974000000\n"
             "telegram: @Dark_577", )


# Rus_menu

# Info
@dp.message(F.text == "Информация")
async def info(message: types.Message):
    await message.answer(
        f"Имя: {message.from_user.full_name}\nИмя пользователя: {message.from_user.username}\nидентификатор: {message.from_user.id}")


# Language
@dp.message(F.text == "Язык")
async def lang_function(message: types.Message):
    await message.answer(text="Вы вернулись, чтобы изменить язык", reply_markup=main_button_lang)


# Commany Info
@dp.message(F.text == "Информация компании")
async def lang_function(message: types.Message):
    await message.answer(
        text="Добро пожаловать в Интернет-магазин, Мы работаем онлайн, у нас еще есть филиалы, так как мы начали свой бизнес недавно\n"
             "\н"
             "\н"
             "Если вам нужна помощь\n"
             "Для связи: +998974000000\n"
             "телеграмма: @Dark_577", )


# info
@dp.message(filters.Command("info"))
async def info(message: types.Message):
    await message.answer(
        f"Ism: {message.from_user.full_name}\nUsername: {message.from_user.username}\nID: {message.from_user.id}")


# language
@dp.message(filters.Command("lang"))
async def lang_function(message: types.Message):
    await message.answer(text="Siz til ozgartirishga qaytingiz", reply_markup=main_button_lang)


# Commany info
@dp.message(filters.Command("information"))
async def lang_function(message: types.Message):
    await message.answer(
        text="Online Shop Magaziniga Xush Kelibsiz, Biz Online ishlimiz bizda xali filiallarimiz yoq, Chunki biz yaqinda Ish faoliyatimiz boshlaganmiz\n"
             "\n"
             "\n"
             "Yordam kerak bolsa\n"
             "Murojat uchun: +998974000000\n"
             "telegram: @Dark_577", )


#Korzinka

@dp.message(F.text == "Korzinka")
async def orders_function(message: types.Message):
    if orders:
        await message.answer(f"Sizni buyurtmalaringiz: {', '.join(orders)}", reply_markup=card_uz)
    else:
        await message.answer("Sizda hali buyurtma yo'q.")



@dp.message(filters.Command("menyu"))
async def lang_function(message: types.Message):
    await message.answer(text="Menyudasiz", reply_markup=main_menu_uzbek)


@dp.message(filters.Command("uz_card"))
async def lang_function(message: types.Message):
    await message.answer(text="Siz karta bolimidasiz", reply_markup=card_uz)

@dp.message(F.text == "UzCard")
async def pey_function(message: types.Message, state: FSMContext):
    await state.set_state(Card.card_number)
    await message.answer("Karta raqamini kiriting 💳")

@dp.message(F.text == "Humo")
async def pey_function(message: types.Message, state: FSMContext):
    await state.set_state(Card.card_number)
    await message.answer("Karta raqamini kiriting 💳")



@dp.message(Card.card_number)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit() and len(text) == 16:
        await state.update_data(card_number=message.text)
        await message.answer("Haridingiz uchun rahmat!", reply_markup=main_button_lang)
    else:
        await message.answer("Boshidan urinib ko'ring !\nKartangizni raqami 16 sondan iborat bolishi kerak")
    await state.clear()


#Gamburger
@dp.message(F.text == "Gamburger")
async def gam(message: types.Message):
    gam = "http://cc.oqtepalavash.uz/api/image/d9d553d9-ddb0-41cd-9523-ad67057beb4c.png"

    lst.append("Gamburger")
    list.append("Гамбургер")
    await message.answer_photo(photo=gam, caption="Gamburger\nNarxi: 27.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


@dp.message(F.text == "CheesBurger")
async def ches(message: types.Message):
    ches = "http://cc.oqtepalavash.uz/api/image/2c5b49c7-ed11-4219-a3f3-3725b1ddbf8d.png"
    lst.append("CheesBurger")
    list.append("ЧизБургер")
    await message.answer_photo(photo=ches, caption="CheesBurger\nNarxi: 29.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


@dp.message(F.text == "Big Gamburger")
async def big(message: types.Message):
    big = "http://cc.oqtepalavash.uz/api/image/51cbea60-9599-46b4-817b-a0583c7a303b.png"
    lst.append("Big Gamburger")
    list.append("Большой Гамбургер")
    await message.answer_photo(photo=big, caption="Big Gamburger\nNarxi: 37.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


@dp.message(F.text == "Big CheesBurger")
async def big(message: types.Message):
    big = "http://cc.oqtepalavash.uz/api/image/b045b8b3-6e32-46f3-bad0-0ad539c56937.png"
    lst.append("Big CheesBurger")
    list.append("Большой Чизбургер")
    await message.answer_photo(photo=big, caption="Big CheesBurger\nNarxi: 41.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


# Lavash
@dp.message(F.text == "Lavash")
async def Lavash(message: types.Message):
    Lavash = "http://cc.oqtepalavash.uz/api/image/43be6508-dff0-4823-90ff-b3b0d3973743.png"
    lst.append("Lavash")
    list.append("Лаваш")
    await message.answer_photo(photo=Lavash, caption="Lavash\nNarxi: 32.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


@dp.message(F.text == "Mini Lavash")
async def mini(message: types.Message):
    mini = "http://cc.oqtepalavash.uz/api/image/37d593ff-6092-43bb-9a62-09cc8c3e0b8b.png"
    lst.append("Mini Lavash")
    list.append("Мини Лаваш")
    await message.answer_photo(photo=mini, caption="Mini Lavash\nNarxi: 27.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


@dp.message(F.text == "Sirli Lavash")
async def sirli(message: types.Message):
    sirli = "http://cc.oqtepalavash.uz/api/image/51cbea60-9599-46b4-817b-a0583c7a303b.png"
    lst.append("Sirli Lavash")
    list.append("Cырли лаваш")
    await message.answer_photo(photo=sirli, caption="Sirli Lavash\nNarxi: 35.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


@dp.message(F.text == "Mini sirli Lavash")
async def mini(message: types.Message):
    mini = "http://cc.oqtepalavash.uz/api/image/041f54ac-e0ff-4afd-bb30-26c7ebec7564.png"
    lst.append("Mini sirli Lavash")
    list.append("Мини cырли лаваш")
    await message.answer_photo(photo=mini, caption="Mini sirli lavash\nNarxi: 30.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


@dp.message(F.text == "Tandir Lavash")
async def tandir(message: types.Message):
    tandir = "http://cc.oqtepalavash.uz/api/image/3ae07ce8-dbf7-4420-986b-571c25ad424e.png"
    lst.append("Tandir Lavash")
    list.append("Тандыр Лаваш")
    await message.answer_photo(photo=tandir, caption="Tandir Lavash\nNarxi: 34.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


@dp.message(F.text == "Tandir sirli Lavash")
async def tandir(message: types.Message):
    tandir = "http://cc.oqtepalavash.uz/api/image/a87d3ca3-531e-47ae-95b2-86d14c0ec7a9.png"
    lst.append("Tandir sirli Lavash")
    list.append("Cырли Тандыр Лаваш")
    await message.answer_photo(photo=tandir, caption="Tandir sirli Lavash\nNarxi: 37.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


# SandWich
@dp.message(F.text == "SandWich🥪")
async def sand(message: types.Message):
    sand = "http://cc.oqtepalavash.uz/api/image/83753fef-a9f9-4295-b059-1e42391bc209.png"
    lst.append("SandWich")
    list.append("Сэндвич")
    await message.answer_photo(photo=sand, caption="Sand Wich\nNarxi: 38.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


# pizza
@dp.message(F.text == "Sirli Pizza")
async def sirli(message: types.Message):
    sirli = "https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2Ffd253a59-c094-468e-bb31-bda637aa9dcd.jpg&w=1920&q=100"
    lst.append("Sirli Pizza")
    list.append("Cырли лаваш")
    await message.answer_photo(photo=sirli, caption="Sirli Pizza\nNarxi: 30.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


@dp.message(F.text == "Barbeku Pizza")
async def bar(message: types.Message):
    bar = "https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F18dcffd2-c192-4811-8698-68c8a51cdb34.jpg&w=1920&q=100"
    lst.append("Barbeku Pizza")
    list.append("Пицца Барбекю")
    await message.answer_photo(photo=bar, caption="Barbeku Pizza\nNarxi: 53.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


@dp.message(F.text == "Tovuqli Pizza")
async def tovuq(message: types.Message):
    tovuq = "https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F15f8411b-947d-405b-9c78-016711ba8da1.jpg&w=1920&q=100"
    lst.append("Tovuqli Pizza")
    list.append("Куриная Пицца")
    await message.answer_photo(photo=tovuq, caption="Tovuqli va qoziqorinli Pizza\nNarxi: 47.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


@dp.message(F.text == "Meksikancha Pizza")
async def mek(message: types.Message):
    mek = "https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F07b2af79-95e0-48ae-8962-3b29fdfcb6d4.jpg&w=1920&q=100"
    lst.append("Meksikancha Pizza")
    list.append("Мексиканская пицца")
    await message.answer_photo(photo=mek, caption="Meksikancha Pizza\nNarxi: 57.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


@dp.message(F.text == "Alfredo Pizza")
async def alfredo(message: types.Message):
    alfredo = "https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F01fce38e-ec3b-461e-a33c-31d4d9f8106f.jpg&w=1920&q=100"
    lst.append("Alfredo Pizza")
    list.append("Альфредо Пицца")
    await message.answer_photo(photo=alfredo, caption="Alfredo Pizza\nNarxi: 47.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


@dp.message(F.text == "Peperoni Pizza")
async def peperoni(message: types.Message):
    peperoni = "https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F601282db-7274-43e4-ac74-e8987d53dd6e.jpg&w=1920&q=100"
    lst.append("Peperoni Pizza")
    list.append("Пицца пепперони")
    await message.answer_photo(photo=peperoni, caption="Peperoni Pizza\nNarxi: 37.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


@dp.message(F.text == "Donar Pizza")
async def donar(message: types.Message):
    donar = "https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F405e4be1-3493-49d2-ab92-4eb256200ac5.jpg&w=1920&q=100"
    lst.append("Donar Pizza")
    list.append("Донер Пицца")
    await message.answer_photo(photo=donar, caption="Donar Pizza\nNarxi: 63.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


@dp.message(F.text == "Goshtli miks Pizza")
async def miks(message: types.Message):
    miks = "https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2Fc14e362c-57a5-49fd-9a80-b14ce099b777.jpg&w=1920&q=100"
    lst.append("Goshtli miks Pizza")
    list.append("Пицца-микс с мясом")
    await message.answer_photo(photo=miks, caption="Goshtli miks Pizza\nNarxi: 92.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


# Hot_Dog
@dp.message(F.text == "koraleviski Hod-Dog")
async def karol(message: types.Message):
    karol = "http://cc.oqtepalavash.uz/api/image/10b4be39-022f-4076-a563-ea3f23cefedb.png"
    lst.append("koraleviski Hod-Dog")
    list.append("Коралевский Ход Дог")
    await message.answer_photo(photo=karol, caption="koraleviski Hod-Dog\nNarxi: 25.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


@dp.message(F.text == "Barbeku Hod-Dog")
async def bar(message: types.Message):
    bar = "https://w7.pngwing.com/pngs/194/388/png-transparent-hotdog-on-bun-with-cheese-illustration-hot-dog-sausage-chili-dog-bratwurst-fast-food-hot-dog-food-american-food-hamburger.png"
    lst.append("Barbeku Hod-Dog")
    list.append("Хот-дог барбекю")
    await message.answer_photo(photo=bar, caption="Barbeku Hod-Dog\nNarxi: 26.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


@dp.message(F.text == "Sirli Hod-Dog")
async def sir(message: types.Message):
    sir = "http://cc.oqtepalavash.uz/api/image/818b8a47-fd7f-4164-8859-e7b9b4fb2fc3.png"
    lst.append("Sirli Hod-Dog")
    list.append("Сирни Ход-Дог")
    await message.answer_photo(photo=sir, caption="Sirli Hod-Dog\nNarxi: 17.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


@dp.message(F.text == "Hot-Dog")
async def hot(message: types.Message):
    hot = "http://cc.oqtepalavash.uz/api/image/4ba84e47-e14f-475b-b1fc-ead298cfa2e3.png"
    lst.append("Hot-Dog")
    list.append("Хот-дог")
    await message.answer_photo(photo=hot, caption="Hot-Dog\nNarxi: 15.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


# donar
@dp.message(F.text == "Mini Donar")
async def mini(message: types.Message):
    mini = "http://cc.oqtepalavash.uz/api/image/d87470f7-a2f5-469e-8ceb-41167015ade1.png"
    lst.append("Mini Donar")
    list.append("Мини Донар")
    await message.answer_photo(photo=mini, caption="Mini Donar\nNarxi: 30.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


@dp.message(F.text == "Big Donar")
async def big(message: types.Message):
    big = "http://cc.oqtepalavash.uz/api/image/5eb594bd-979f-46c0-aaa6-ff6d126a25bb.png"
    lst.append("Big Donar")
    list.append("Большой донор")
    await message.answer_photo(photo=big, caption="Big Donar\nNarxi: 35.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


@dp.message(F.text == "Shaurma")
async def shaurma(message: types.Message):
    shaurma = "http://cc.oqtepalavash.uz/api/image/ba94cc51-7a3f-4b25-b10b-509c64ad624f.png"
    lst.append("Shaurma")
    list.append("Шаурма")
    await message.answer_photo(photo=shaurma, caption="Shaurma\nNarxi: 26.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


@dp.message(F.text == "Xaggi")
async def xaggi(message: types.Message):
    xaggi = "http://cc.oqtepalavash.uz/api/image/e18f6bee-0790-4f5e-a23d-8ba258f12a2d.png"
    lst.append("Xaggi")
    list.append("Хагги")
    await message.answer_photo(photo=xaggi, caption="Xaggi\nNarxi: 36.000 ming",
                               reply_markup=yesno_uzbek_FastFood)


# Shirinliklar

# AlpenGold
@dp.message(F.text == "AlpenGold\nYong'oqlik")
async def alpen(message: types.Message):
    alpen = "https://alpengold.me/img/catalog/alpengold/product/5.png"
    lst.append("AlpenGold\nYong'oqlik")
    list.append("АльпенГолд\nЧокнутый")
    await message.answer_photo(photo=alpen, caption="AlpenGold Yong'oqlik\nNarxi: 10.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


@dp.message(F.text == "AlpenGold\nKakosli")
async def alpen(message: types.Message):
    alpen = "https://alpengold.me/img/catalog/alpengold/product/7.png"
    lst.append("AlpenGold\nKakosli")
    list.append("АльпенГолд\nКакос")
    await message.answer_photo(photo=alpen, caption="AlpenGold Kakosli\nNarxi: 10.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


@dp.message(F.text == "AlpenGold\nKapuchinoli")
async def alpen(message: types.Message):
    alpen = "https://alpengold.me/img/catalog/alpengold/product/10.png"
    lst.append("AlpenGold\nKapuchinoli")
    list.append("АльпенГолд\nКапучино")
    await message.answer_photo(photo=alpen, caption="AlpenGold Kapuchinoli\nNarxi: 10.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


@dp.message(F.text == "AlpenGold\nQulupnayli")
async def alpen(message: types.Message):
    alpen = "https://alpengold.me/img/catalog/alpengold/product/4.png"
    lst.append("AlpenGold\nQulupnayli")
    list.append("АльпенГолд\nКлубника")
    await message.answer_photo(photo=alpen, caption="AlpenGold Qulubnayli\nNarxi: 10.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


@dp.message(F.text == "AlpenGold\nSutli")
async def alpen(message: types.Message):
    alpen = "https://alpengold.me/img/catalog/alpengold/product/3.png"
    lst.append("AlpenGold\nSutli")
    list.append("АльпенГолд\nМолоко")
    await message.answer_photo(photo=alpen, caption="AlpenGold Sutli\nNarxi: 10.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


@dp.message(F.text == "AlpenGold\nOreoli")
async def alpen(message: types.Message):
    alpen = "https://alpengold.me/img/catalog/oreo/product/1.png"
    lst.append("AlpenGold\nOreoli")
    list.append("АльпенГолд\nОрео")
    await message.answer_photo(photo=alpen, caption="AlpenGold Oreoli\nNarxi: 10.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


# Nestle
@dp.message(F.text == "Nestle\nKarameli")
async def nest(message: types.Message):
    nest = "https://sun9-54.userapi.com/impg/prrZKSHWmCaJUcB6Q67o5zAr5GG2-btOXjKa5w/Hh72pEmtqhE.jpg?size=542x604&quality=96&sign=cb6ff25d5dac3c0df2527b66c180db10&c_uniq_tag=NZwgDXKdCKm75BZOZv91lj-oLtfQPnrmZZw86l9XDvI&type=album"
    lst.append("Nestle\nKarameli")
    list.append("Нестле\nКарамель")
    await message.answer_photo(photo=nest, caption="Nestle Karameli\nNarxi: 9.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


@dp.message(F.text == "Nestle\nSutli")
async def nest(message: types.Message):
    nest = "https://avatars.mds.yandex.net/get-mpic/6277643/img_id5231020731460371794.jpeg/orig"
    lst.append("Nestle\nSutli")
    list.append("Нестле\nМолоко")
    await message.answer_photo(photo=nest, caption="Nestle Sutli\nNarxi: 9.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


@dp.message(F.text == "Nestle\nYong'oqli")
async def nest(message: types.Message):
    nest = "https://www.sladkiymarket.ru/upload/iblock/4fd/4fddcabff4d82b6e4da3b7eb1f9d1609.jpeg"
    lst.append("Nestle\nYong'oqli")
    list.append("Нестле\nЧокнутый")
    await message.answer_photo(photo=nest, caption="Nestle Yong'oqli\nNarxi: 9.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


@dp.message(F.text == "Nestle\nUzumli")
async def nest(message: types.Message):
    nest = "https://nesipetsin.com:7070/images/product/2020/09/24/15/b874caa8-4b0b-49c7-9a0f-a7134b7d53f8.jpg"
    lst.append("Nestle\nUzumli")
    list.append("Нестле\nГрейпфрут")
    await message.answer_photo(photo=nest, caption="Nestle Uzumli\nNarxi: 9.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


@dp.message(F.text == "Nestle\nVaflili")
async def nest(message: types.Message):
    nest = "https://gipermix.ru/upload/iblock/a13/a1386cad4f519ad7ffaf8548302b5ba0.jpg"
    lst.append("Nestle\nVaflili")
    list.append("Нестле\nВафлями")
    await message.answer_photo(photo=nest, caption="Nestle Vaflili \nNarxi: 9.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


# Snikers
@dp.message(F.text == "Snikers")
async def snikers(message: types.Message):
    snikers = "https://o-manager.ru/foto/1205-0551.jpg"
    lst.append("Snikers")
    list.append("Сникерс")
    await message.answer_photo(photo=snikers, caption="Snikers\nNarxi: 7.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


# MilkyWay
@dp.message(F.text == "MilkyWay\nsutli")
async def milky(message: types.Message):
    milky = "https://mykaleidoscope.ru/uploads/posts/2022-07/1657292432_26-mykaleidoscope-ru-p-shokoladka-milki-vei-vkusnyashki-krasivo-f-46.jpg"
    lst.append("MilkyWay\nsutli")
    list.append("Млечный Путь\nмолочный")
    await message.answer_photo(photo=milky, caption="MilkyWay Sutli \nNarxi: 6.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


@dp.message(F.text == "MilkyWay\nshkoladli")
async def milky(message: types.Message):
    milky = "https://imgproxy.sbermarket.ru/imgproxy/size-680-680/czM6Ly9jb250ZW50LWltYWdlcy1wcm9kL3Byb2R1Y3RzLzIzMDMwOTY3L29yaWdpbmFsLzEvMjAyMy0wMy0yNFQxMSUzQTQyJTNBNDcuNjY4MDAwJTJCMDAlM0EwMC8yMzAzMDk2N18xLmpwZw==.jpg"
    lst.append("MilkyWay\nshkoladli")
    list.append("Млечный Путь\nШколойт")
    await message.answer_photo(photo=milky, caption="MilkyWay Shkoladli\nNarxi: 6.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


# Oreo
@dp.message(F.text == "Oreo\nShkaladli")
async def oreo(message: types.Message):
    oreo = "https://mosnapitki.ru/upload/iblock/628/geg012xznduh965osxv1f7m6x949b8pa.jpg"
    lst.append("Oreo\nShkaladli")
    list.append("Орео\nВ масштабе")
    await message.answer_photo(photo=oreo, caption="Oreo Shkaladli \nNarxi: 10.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


@dp.message(F.text == "Oreo\nQizil Velvet")
async def oreo(message: types.Message):
    oreo = "https://eurotrade24.ru/d/123.jpg"
    lst.append("Oreo\nQizil Velvet")
    list.append("Орео\nКрасный бархат")
    await message.answer_photo(photo=oreo, caption="Oreo Qizil Velvet\nNarxi: 9.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


@dp.message(F.text == "Oreo\nSutli")
async def oreo(message: types.Message):
    oreo = "https://produktoff.kz/pictures/product/big/13652_big.png"
    lst.append("Oreo\nSutli")
    list.append("Орео\nМолоко")
    await message.answer_photo(photo=oreo, caption="Oreo Sutli \nNarxi: 11.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


@dp.message(F.text == "Oreo\nQulubnayli")
async def oreo(message: types.Message):
    oreo = "https://aws.kiiiosk.store/uploads/shop/9065/uploads/product_image/image/775624/4d21c418fdbf186a93b6ad15b5bdb5b820221203-555999-1hy0cg.jpg"
    lst.append("Oreo\nQulubnayli")
    list.append("Oreo\nQulubnayli")
    await message.answer_photo(photo=oreo, caption="Oreo Qulubnayli\nNarxi: 11.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


# M_MS
@dp.message(F.text == "M_MS\nYeryong'oqli")
async def ememdes(message: types.Message):
    ememdes = "https://colodu.club/uploads/posts/2022-10/1666333528_17-colodu-club-p-shokolad-mmdems-plitka-dizain-vkontakte-18.jpg"
    lst.append("M_MS\nYeryong'oqli")
    list.append("M_MS\nАрахис")
    await message.answer_photo(photo=ememdes, caption="Ememdes Yeryong'oqli \nNarxi: 18.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


@dp.message(F.text == "M_MS\nShkoladli")
async def ememdes(message: types.Message):
    ememdes = "https://cdn.shopify.com/s/files/1/0258/7626/7092/products/s-l1600_215d5183-339a-4331-9102-123ee4bc9e1a_1200x1200.jpg"
    lst.append("M_MS\nShkoladli")
    list.append("М_МС\nШколойт")
    await message.answer_photo(photo=ememdes, caption="Ememdes Shkoladli\nNarxi: 18.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


@dp.message(F.text == "M_MS\nBodomli")
async def ememdes(message: types.Message):
    ememdes = "https://gas-kvas.com/uploads/posts/2023-08/1693461350_gas-kvas-com-p-risunki-na-prazdnik-den-shokoladnogo-drazh-38.jpg"
    lst.append("M_MS\nBodomli")
    list.append("M_MS\nМиндаль")
    await message.answer_photo(photo=ememdes, caption="Ememdes Bodomli\nNarxi: 18.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


@dp.message(F.text == "M_MS\nYashil Qarsildoqli")
async def ememdes(message: types.Message):
    ememdes = "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1547831808-m-ms-milk-chocolate-bar-crispy-mint-1547831737.jpg?crop=1xw:1xh;center,top&resize=980:*"
    lst.append("M_MS\nYashil Qarsildoqli")
    list.append("M_MS\nЗеленая сова")
    await message.answer_photo(photo=ememdes, caption="Ememdes yashil Qarsildoqli \nNarxi: 18.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)


@dp.message(F.text == "M_MS\nKok Qarsildoqli")
async def ememdes(message: types.Message):
    ememdes = "https://i5.walmartimages.com/asr/ba2e7d18-97fe-4fc1-8c0d-c6db030dac63_1.fb012aee8ef94804c22e6f99df993d8b.jpeg"
    lst.append("M_MS\nKok Qarsildoqli")
    list.append("M_MS\nКок Каргильдокли")
    await message.answer_photo(photo=ememdes, caption="Ememdes kok Qarsildoqli\nNarxi: 18.000 ming",
                               reply_markup=yesno_uzbek_shirinlikar)



# Ichimliklar

# Pepsi
@dp.message(F.text == "Pepsi 2L")
async def pepsi(message: types.Message):
    pepsi = "https://nnjfood.ru/upload/iblock/1ac/2hfb9fdkd116ymdkxyattpyarm7vx8r1.jpg"
    lst.append("Pepsi 2L")
    list.append("Пепси 2л")
    await message.answer_photo(photo=pepsi, caption="Pepsi 2L\nNarxi: 18.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Pepsi 1.5L")
async def pepsi(message: types.Message):
    pepsi = "https://cdn1.ozone.ru/s3/multimedia-j/6467676559.jpg"
    lst.append("Pepsi 1.5L")
    list.append("Пепси 1,5л")
    await message.answer_photo(photo=pepsi, caption="Pepsi 1.5L\nNarxi: 14.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Pepsi 1L")
async def pepsi(message: types.Message):
    pepsi = "https://mastfood.ru/upload/iblock/963/96351b2eaba516210ad78f1682a89e19.jpg"
    lst.append("Pepsi 1L")
    list.append("Пепси 1л")
    await message.answer_photo(photo=pepsi, caption="Pepsi 1L\nNarxi: 11.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Pepsi 0.5L")
async def pepsi(message: types.Message):
    pepsi = "https://mastfood.ru/upload/iblock/d98/d9808dad997dc328021c7675c9ca375e.jpg"
    lst.append("Pepsi 0.5L")
    list.append("Пепси 0,5л")
    await message.answer_photo(photo=pepsi, caption="Pepsi 0.5L\nNarxi: 6.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Shakarsiz Pepsi")
async def pepsi(message: types.Message):
    pepsi = "https://ekipazh-service.com.ua/wp-content/uploads/2020/01/pepsiblack300x230-1600x1056-1-1536x1014.png"
    lst.append("Shakarsiz Pepsi")
    list.append("Пепси без сахара")
    await message.answer_photo(photo=pepsi, caption="Shakarsiz Pepsi\nNarxi: 6.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


# Coca Cola
@dp.message(F.text == "Coca Cola 1.5L")
async def cola(message: types.Message):
    Cola = "https://clipart-library.com/image_gallery2/Coca-Cola-PNG-Clipart.png"
    lst.append("Coca-Cola 1.5L")
    list.append("Кока-Кола 1,5л")
    await message.answer_photo(photo=Cola, caption="Coca cola 1.5L\nNarxi: 15.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Coca Cola 1L")
async def cola(message: types.Message):
    Cola = "https://bonsai.asia/d/hwg8hwyp30td0jr_9289fb4a.jpg"
    lst.append("Coca-Cola 1L")
    list.append("Кока-Кола 1л")
    await message.answer_photo(photo=Cola, caption="Coca Cola 1L\nNarxi: 11.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Coca Cola 0.5L")
async def cola(message: types.Message):
    Cola = "https://pacopizza.ru/wp-content/uploads/2022/09/cola-2.png"
    lst.append("Coca Cola 0.5L")
    list.append("Кока Кола 0.5л")
    await message.answer_photo(photo=Cola, caption="Coca Cola 0.5L\nNarxi: 7.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Milliy Cola")
async def cola(message: types.Message):
    Cola = "https://vendliga.ru/upload/resize_cache/iblock/73e/1200_1200_140cd750bba9870f18aada2478b24840a/aauf9xl6nwd6udmlpuuiy1r0zh86iyss.png"
    lst.append("Milliy Cola")
    list.append("Миллий кола")
    await message.answer_photo(photo=Cola, caption="Milliy Cola\nNarxi: 6.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Shakarsiz Coca Cola")
async def cola(message: types.Message):
    Cola = "https://images.uzum.uz/cegsalgv1htd23ajb1cg/original.jpg"
    lst.append("Shakarsiz Coca Cola")
    list.append("Кока-Кола без сахара")
    await message.answer_photo(photo=Cola, caption="Shakarsiz Cola\nNarxi: 7.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


# Fanta
@dp.message(F.text == "Fanta 1.5L")
async def Fanta(message: types.Message):
    Fanta = "https://puddostavka.ru/upload/iblock/69d/cydg6wcjv09y042cgtme7mife195oljb.jpg"
    lst.append("Fanta 1.5L")
    list.append("Фанта 1,5л")
    await message.answer_photo(photo=Fanta, caption="Fanta 1.5L\nNarxi: 12.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Fanta 1L")
async def Fanta(message: types.Message):
    Fanta = "https://pirogi-osetia.ru/upload/iblock/4d1/l7g3oppicw4u0l12ixy7hxdlo7cdrthq.png"
    lst.append("Fanta 1L")
    list.append("Фанта 1л")
    await message.answer_photo(photo=Fanta, caption="Fanta 1L\nNarxi: 10.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Fanta 0.5L")
async def Fanta(message: types.Message):
    Fanta = "https://korzina.su/upload/iblock/0cb/0cb34bf1bf860155f84e66a2619494a3.jpg"
    lst.append("Fanta 0.5L")
    list.append("Фанта 0.5л")
    await message.answer_photo(photo=Fanta, caption="Fanta 0.5L\nNarxi: 6.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


# Tropic
@dp.message(F.text == "Tropic 1L")
async def tropic(message: types.Message):
    tropic = "https://images.uzum.uz/cfdu5i2g84cfbutu83ag/original.jpg"
    lst.append("Tropic 1L")
    list.append("Тропик 1л")
    await message.answer_photo(photo=tropic, caption="Tropic 1L\nNarxi: 15.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Tropic 0.5L Mangoli")
async def tropic(message: types.Message):
    tropic = "https://yukber.uz/image/cache/catalog/product/YK0184/YK0184_1-700x700.jpg"
    lst.append("Tropic 0.5L Mangoli")
    list.append("Тропик 0.5л Манголи")
    await message.answer_photo(photo=tropic, caption="Tropic Mangoli\nNarxi: 5.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Tropic 0.5L Guavali")
async def tropic(message: types.Message):
    tropic = "https://yukber.uz/image/cache/catalog/product/YK0182/YK0182_1-700x700.jpg"
    lst.append("Tropic 0.5L Guavali")
    list.append("Тропик 0.5л Гуавали")
    await message.answer_photo(photo=tropic, caption="Tropic Guavali\nNarxi: 5.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


# Sprite
@dp.message(F.text == "Sprite 1.5L")
async def sprite(message: types.Message):
    sprite = "https://www.okeydostavka.ru/wcsstore/OKMarketCAS/cat_entries/35207/35207_fullimage.jpg"
    lst.append("Sprite 1.5L")
    list.append("Спрайт 1,5л")
    await message.answer_photo(photo=sprite, caption="Sprite 1.5L\nNarxi: 13.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Sprite 1L")
async def sprite(message: types.Message):
    sprite = "https://static.insales-cdn.com/r/BggRp8mShS8/rs:fit:1000:1000:1/plain/images/products/1/7022/642235246/спрайт_в_бутылке_1_л.jpg@jpg"
    lst.append("Sprite 1L")
    list.append("Спрайт 1л")
    await message.answer_photo(photo=sprite, caption="Sprite 1L\nNarxi: 10.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Sprite 0.5L")
async def sprite(message: types.Message):
    sprite = "https://cdn.b-catalog.ru/bcbucket/public/a/845/2020/8/4/7c3dd77f-e754-4f27-9c7e-548599503654"
    lst.append("Sprite 0.5L")
    list.append("Спрайт 0.5л")
    await message.answer_photo(photo=sprite, caption="Sprite 0.5Lx\nNarxi: 6.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


# Lipton
@dp.message(F.text == "Lipton 1.5L\nOrik")
async def Lipton(message: types.Message):
    Lipton = "https://palladi.ru/upload/iblock/47a/47a14aefd80abbf92a35d8f5648469e1.jpg"
    lst.append("Lipton 1.5L\nOrik")
    list.append("Липтон 1.5л\nОрик")
    await message.answer_photo(photo=Lipton, caption="Lipton Orik 1.5L\nNarxi: 10.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Lipton 1L\nOrik")
async def Lipton(message: types.Message):
    Lipton = "https://planetavkysov.ru/image/cache/resize/s/1200x630/catalog/napitki/4600494600531.jpg"
    lst.append("Lipton 1L\nOrik")
    list.append("Липтон 1л\nОрик")
    await message.answer_photo(photo=Lipton, caption="Lipton Orik 1L\nNarxi: 7.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Lipton 0.5L\nOrik")
async def Lipton(message: types.Message):
    Lipton = "https://tornado.shop/images/detailed/25/P1342254.jpg"
    lst.append("Lipton 0.5L\nOrik")
    list.append("Липтон 0.5л\nОрик")
    await message.answer_photo(photo=Lipton, caption="Lipton Orik 0.5L\nNarxi: 5.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Lipton 1.5L\nYashil")
async def lipton(message: types.Message):
    lipton = "https://dobrodusha.ru/image/cache/catalog/liptonicetea/zel1.5-800x800.jpg"
    lst.append("Lipton 1.5L\nYashil")
    list.append("Липтон 1,5л\nЗеленый")
    await message.answer_photo(photo=lipton, caption="Lipton Yashil 1.5L\nNarxi: 10.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Lipton 1L\nYashil")
async def lipton(message: types.Message):
    lipton = "https://losossir.ru/uploads/catalog/napitki/zelenyjchajlipton.png"
    lst.append("Lipton 1L\nYashil")
    list.append("Липтон 1л\nЗеленый")
    await message.answer_photo(photo=lipton, caption="Lipton Yashil 1L\nNarxi: 7.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Lipton 0.5L\nYashil")
async def lipton(message: types.Message):
    lipton = "https://cdn-ru5.foodpicasso.com/assets/2024/02/20/892a919ecd6964bf2cd42403199b5cda---jpg_1000x_103c0_convert.jpg"
    lst.append("Lipton 0.5L\nYashil")
    list.append("Липтон 0,5л\nЗеленый")
    await message.answer_photo(photo=lipton, caption="Lipton Yashil 0.5L\nNarxi: 5.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Lipton 1.5L\nLimon")
async def lipton(message: types.Message):
    lipton = "https://ccm76.ru/wp-content/uploads/2022/06/lipton-2-scaled.jpg"
    lst.append("Lipton 1.5L\nLimon")
    list.append("Липтон 1,5л\nЛимон")
    await message.answer_photo(photo=lipton, caption="Lipton Limonli 1.5L\nNarxi: 10.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Lipton 1L\nLimon")
async def lipton(message: types.Message):
    lipton = "https://www.meme-arsenal.com/memes/16ec18cab6e6cbd93b50ec5e029c6a76.jpg"
    lst.append("Lipton 1L\nLimon")
    list.append("Липтон 1л\nЛимон")
    await message.answer_photo(photo=lipton, caption="Lipton Limonli 1L\nNarxi: 7.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


@dp.message(F.text == "Lipton 0.5L\nLimon")
async def lipton(message: types.Message):
    lipton = "https://globusgurme.ru/upload/preview/iblock/fa4/pvjsntobhhedag4xs9d9qd02g2sapb25800_800_thumb_v2_0.jpg"
    lst.append("Lipton 0.5L\nLimon")
    list.append("Липтон 0,5л\nЛимон")
    await message.answer_photo(photo=lipton, caption="Lipton Limonli 0.5L\nNarxi: 5.000 ming",
                               reply_markup=yesno_uzbek_Ichimlikar)


# Rus_tili_menu

#Korzinka
@dp.message(F.text == "Корзина")
async def orders_function(message: types.Message):
    if order:
        await message.answer(f"Ваши заказы: {', '.join(order)}", reply_markup=card_ru)
    else:
        await message.answer("У вас пока нет заказов.")

@dp.message(filters.Command("menyu_rus"))
async def lang_function(message: types.Message):
    await message.answer(text="Вы находитесь в меню", reply_markup=main_menu_rus)

@dp.message(filters.Command("ru_card"))
async def lang_function(message: types.Message):
    await message.answer(text="Вы находитесь в разделе карты", reply_markup=card_ru)


@dp.message(F.text == "УзКард")
async def pey_function(message: types.Message, state: FSMContext):
    await state.set_state(Card.card_number)
    await message.answer("Введите номер карты 💳")

@dp.message(F.text == "Хумо")
async def pey_function(message: types.Message, state: FSMContext):
    await state.set_state(Card.card_number)
    await message.answer("Введите номер карты 💳")

@dp.message(Card.card_number)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit() and len(text) == 16:
        await state.update_data(card_number=message.text)
        await message.answer("Спасибо за покупку", reply_markup=main_button_lang)
    else:
        await message.answer("Попробуйте еще раз!\n Номер вашей карты должен состоять из 16 цифр.")



@dp.message(F.text == "Гамбургер")
async def gam(message: types.Message):
    gam = "http://cc.oqtepalavash.uz/api/image/d9d553d9-ddb0-41cd-9523-ad67057beb4c.png"
    list.append("Гамбургер")
    lst.append("Gamburger")
    await message.answer_photo(photo=gam, caption="Гамбургер\nЦена: 27.000 тысяч",
                               reply_markup=yesno_rus_FastFood)



@dp.message(F.text == "ЧизБургер")
async def ches(message: types.Message):
    ches = "http://cc.oqtepalavash.uz/api/image/2c5b49c7-ed11-4219-a3f3-3725b1ddbf8d.png"
    list.append("ЧизБургер")
    lst.append("Chizburger")
    await message.answer_photo(photo=ches, caption="ЧизБургер\nЦена: 29.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


@dp.message(F.text == "Большой Гамбургер")
async def big(message: types.Message):
    big = "http://cc.oqtepalavash.uz/api/image/51cbea60-9599-46b4-817b-a0583c7a303b.png"
    list.append("Большой Гамбургер")
    lst.append("Big Gamburger")
    await message.answer_photo(photo=big, caption="Большой Гамбургер\nЦена: 37.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


@dp.message(F.text == "Большой Чизбургер")
async def big(message: types.Message):
    big = "http://cc.oqtepalavash.uz/api/image/b045b8b3-6e32-46f3-bad0-0ad539c56937.png"
    list.append("Большой Чизбургер")
    lst.append("Big Cheesburger")
    await message.answer_photo(photo=big, caption="Большой Чизбургер\nЦена: 41.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


# Lavash
@dp.message(F.text == "Лаваш")
async def Lavash(message: types.Message):
    Lavash = "http://cc.oqtepalavash.uz/api/image/43be6508-dff0-4823-90ff-b3b0d3973743.png"
    list.append("Лаваш")
    lst.append("Lavash")
    await message.answer_photo(photo=Lavash, caption="Лаваш\nЦена: 32.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


@dp.message(F.text == "Мини Лаваш")
async def mini(message: types.Message):
    mini = "http://cc.oqtepalavash.uz/api/image/37d593ff-6092-43bb-9a62-09cc8c3e0b8b.png"
    list.append("Мини Лаваш")
    lst.append("Mini lavash")
    await message.answer_photo(photo=mini, caption="Мини Лаваш\nЦена: 27.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


@dp.message(F.text == "Cырли лаваш")
async def sirli(message: types.Message):
    sirli = "http://cc.oqtepalavash.uz/api/image/4c496127-076b-4e18-91ee-48ab962fb21a.png"
    list.append("Cырли лаваш")
    lst.append("Sirli lavash")
    await message.answer_photo(photo=sirli, caption="Cырли лаваш\nЦена: 35.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


@dp.message(F.text == "Мини cырли лаваш")
async def mini(message: types.Message):
    mini = "http://cc.oqtepalavash.uz/api/image/041f54ac-e0ff-4afd-bb30-26c7ebec7564.png"
    list.append("Мини cырли лаваш")
    lst.append("Mini sirli lavash")
    await message.answer_photo(photo=mini, caption="Мини cырли лаваш\nЦена: 30.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


@dp.message(F.text == "Тандыр Лаваш")
async def tandir(message: types.Message):
    tandir = "http://cc.oqtepalavash.uz/api/image/3ae07ce8-dbf7-4420-986b-571c25ad424e.png"
    list.append("Тандыр Лаваш")
    lst.append("Tandir lavash")
    await message.answer_photo(photo=tandir, caption="Тандыр Лаваш\nЦена: 34.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


@dp.message(F.text == "Cырли Тандыр Лаваш")
async def tandir(message: types.Message):
    tandir = "http://cc.oqtepalavash.uz/api/image/a87d3ca3-531e-47ae-95b2-86d14c0ec7a9.png"
    list.append("Cырли Тандыр Лаваш")
    lst.append("Tandir sirli lavash")
    await message.answer_photo(photo=tandir, caption="Cырли Тандыр Лаваш\nЦена: 37.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


# SandWich
@dp.message(F.text == "Сэндвич🥪")
async def sand(message: types.Message):
    sand = "http://cc.oqtepalavash.uz/api/image/83753fef-a9f9-4295-b059-1e42391bc209.png"
    list.append("Сэндвич")
    lst.append("Sandwich")
    await message.answer_photo(photo=sand, caption="Сэндвич\nЦена: 38.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


# pizza
@dp.message(F.text == "Тайная Пицца")
async def sirli(message: types.Message):
    sirli = "https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2Ffd253a59-c094-468e-bb31-bda637aa9dcd.jpg&w=1920&q=100"
    list.append("Тайная Пицца")
    lst.append("Sirli pizza")
    await message.answer_photo(photo=sirli, caption="Тайная Пицца\nЦена: 30.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


@dp.message(F.text == "Пицца Барбекю")
async def bar(message: types.Message):
    bar = "https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F18dcffd2-c192-4811-8698-68c8a51cdb34.jpg&w=1920&q=100"
    list.append("Пицца Барбекю")
    lst.append("Pizza barbeku")
    await message.answer_photo(photo=bar, caption="Пицца Барбекю\nЦена: 53.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


@dp.message(F.text == "Куриная Пицца")
async def tovuq(message: types.Message):
    tovuq = "https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F15f8411b-947d-405b-9c78-016711ba8da1.jpg&w=1920&q=100"
    list.append("Куриная Пицца")
    lst.append("Tovuqli Pizza")
    await message.answer_photo(photo=tovuq, caption="Пицца с курицей и грибами\nЦена: 47.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


@dp.message(F.text == "Мексиканская пицца")
async def mek(message: types.Message):
    mek = "https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F07b2af79-95e0-48ae-8962-3b29fdfcb6d4.jpg&w=1920&q=100"
    list.append("Мексиканская пицца")
    lst.append("Meksikanski pizza")
    await message.answer_photo(photo=mek, caption="Мексиканская пицца\nЦена: 57.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


@dp.message(F.text == "Альфредо Пицца")
async def alfredo(message: types.Message):
    alfredo = "https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F01fce38e-ec3b-461e-a33c-31d4d9f8106f.jpg&w=1920&q=100"
    list.append("Альфредо Пицца")
    lst.append("Alfredo Pizza")
    await message.answer_photo(photo=alfredo, caption="Альфредо Пицца\nЦена: 47.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


@dp.message(F.text == "Пицца пепперони")
async def peperoni(message: types.Message):
    peperoni = "https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F601282db-7274-43e4-ac74-e8987d53dd6e.jpg&w=1920&q=100"
    list.append("Пицца пепперони")
    lst.append("Pizza Peperoni")
    await message.answer_photo(photo=peperoni, caption="Пицца пепперони\nЦена: 37.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


@dp.message(F.text == "Донер Пицца")
async def donar(message: types.Message):
    donar = "https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F405e4be1-3493-49d2-ab92-4eb256200ac5.jpg&w=1920&q=100"
    list.append("Донер Пицца")
    lst.append("Donar pizza")
    await message.answer_photo(photo=donar, caption="Донер Пицца\nЦена: 63.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


@dp.message(F.text == "Пицца-микс с мясом")
async def miks(message: types.Message):
    miks = "https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2Fc14e362c-57a5-49fd-9a80-b14ce099b777.jpg&w=1920&q=100"
    list.append("Пицца-микс с мясом")
    lst.append("Goshtli-miks pizza")
    await message.answer_photo(photo=miks, caption="Пицца-микс с мясом\nЦена: 92.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


# Hot_Dog
@dp.message(F.text == "Коралевский Ход-Дог")
async def karol(message: types.Message):
    karol = "http://cc.oqtepalavash.uz/api/image/10b4be39-022f-4076-a563-ea3f23cefedb.png"
    list.append("Коралевский Ход-Дог")
    lst.append("Koralevsky Hot_dog")
    await message.answer_photo(photo=karol, caption="Коралевский Ход Дог\nЦена: 25.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


@dp.message(F.text == "Хот-дог барбекю")
async def bar(message: types.Message):
    bar = "https://w7.pngwing.com/pngs/194/388/png-transparent-hotdog-on-bun-with-cheese-illustration-hot-dog-sausage-chili-dog-bratwurst-fast-food-hot-dog-food-american-food-hamburger.png"
    list.append("Хот-дог барбекю")
    lst.append("Hod-dog barbeku")
    await message.answer_photo(photo=bar, caption="Хот-дог барбекю\nЦена: 26.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


@dp.message(F.text == "Сирни Ход-Дог")
async def sir(message: types.Message):
    sir = "http://cc.oqtepalavash.uz/api/image/818b8a47-fd7f-4164-8859-e7b9b4fb2fc3.png"
    list.append("Сирни Ход-Дог")
    lst.append("Sirli Hod-Dog")
    await message.answer_photo(photo=sir, caption="Сирни Ход-Дог\nЦена: 17.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


@dp.message(F.text == "Хот-дог")
async def hot(message: types.Message):
    hot = "http://cc.oqtepalavash.uz/api/image/4ba84e47-e14f-475b-b1fc-ead298cfa2e3.png"
    list.append("Хот-дог")
    lst.append("Hod-dog")
    await message.answer_photo(photo=hot, caption="Хот-дог\nЦена: 15.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


# donar
@dp.message(F.text == "Мини Донар")
async def mini(message: types.Message):
    mini = "http://cc.oqtepalavash.uz/api/image/d87470f7-a2f5-469e-8ceb-41167015ade1.png"
    list.append("Мини Донар")
    lst.append("Mini donar")
    await message.answer_photo(photo=mini, caption="Мини Донар\nЦена: 30.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


@dp.message(F.text == "Большой донор")
async def big(message: types.Message):
    big = "http://cc.oqtepalavash.uz/api/image/5eb594bd-979f-46c0-aaa6-ff6d126a25bb.png"
    list.append("Большой донор")
    lst.append("Big donar")
    await message.answer_photo(photo=big, caption="Большой донор\nЦена: 35.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


@dp.message(F.text == "Шаурма")
async def shaurma(message: types.Message):
    shaurma = "http://cc.oqtepalavash.uz/api/image/ba94cc51-7a3f-4b25-b10b-509c64ad624f.png"
    list.append("Шаурма")
    lst.append("shaurma")
    await message.answer_photo(photo=shaurma, caption="Шаурма\nЦена: 26.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


@dp.message(F.text == "Хагги")
async def xaggi(message: types.Message):
    xaggi = "http://cc.oqtepalavash.uz/api/image/e18f6bee-0790-4f5e-a23d-8ba258f12a2d.png"
    list.append("Хагги")
    lst.append("Xaggi")
    await message.answer_photo(photo=xaggi, caption="Xaggi\nЦена: 36.000 тысяч",
                               reply_markup=yesno_rus_FastFood)


# Shirinliklar

# AlpenGold
@dp.message(F.text == "АльпенГолд\nЧокнутый")
async def alpen(message: types.Message):
    alpen = "https://alpengold.me/img/catalog/alpengold/product/5.png"
    list.append("АльпенГолд\nЧокнутый")
    lst.append("AlpenGold\nYong'oq")
    await message.answer_photo(photo=alpen, caption="АльпенГолд Чокнутый\nЦена: 10.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


@dp.message(F.text == "АльпенГолд\nКакос")
async def alpen(message: types.Message):
    alpen = "https://alpengold.me/img/catalog/alpengold/product/7.png"
    list.append("АльпенГолд\nКакос")
    lst.append("AlpenGold\nKakos")
    await message.answer_photo(photo=alpen, caption="АльпенГолд Какос\nЦена: 10.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


@dp.message(F.text == "АльпенГолд\nКапучино")
async def alpen(message: types.Message):
    alpen = "https://alpengold.me/img/catalog/alpengold/product/10.png"
    list.append("АльпенГолд\nКапучино")
    lst.append("AlpenGold\nKapuchino")
    await message.answer_photo(photo=alpen, caption="АльпенГолд Капучино\nЦена: 10.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


@dp.message(F.text == "АльпенГолд\nКлубника")
async def alpen(message: types.Message):
    alpen = "https://alpengold.me/img/catalog/alpengold/product/4.png"
    list.append("АльпенГолд\nКлубника")
    lst.append("AlpenGold\nQulubnay")
    await message.answer_photo(photo=alpen, caption="АльпенГолд Клубника\nЦена: 10.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


@dp.message(F.text == "АльпенГолд\nМолоко")
async def alpen(message: types.Message):
    alpen = "https://alpengold.me/img/catalog/alpengold/product/3.png"
    list.append("АльпенГолд\nМолоко")
    lst.append("AlpenGold\nSutli")
    await message.answer_photo(photo=alpen, caption="АльпенГолд Молоко\nЦена: 10.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


@dp.message(F.text == "АльпенГолд\nОрео")
async def alpen(message: types.Message):
    alpen = "https://alpengold.me/img/catalog/oreo/product/1.png"
    list.append("АльпенГолд\nОрео")
    lst.append("AlpenGold\nOreo")
    await message.answer_photo(photo=alpen, caption="АльпенГолд Орео\nЦена: 10.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


# Nestle
@dp.message(F.text == "Нестле\nКарамель")
async def nest(message: types.Message):
    nest = "https://sun9-54.userapi.com/impg/prrZKSHWmCaJUcB6Q67o5zAr5GG2-btOXjKa5w/Hh72pEmtqhE.jpg?size=542x604&quality=96&sign=cb6ff25d5dac3c0df2527b66c180db10&c_uniq_tag=NZwgDXKdCKm75BZOZv91lj-oLtfQPnrmZZw86l9XDvI&type=album"
    list.append("Нестле\nКарамель")
    lst.append("Nestle\nKaramel")
    await message.answer_photo(photo=nest, caption="Нестле Карамель\nЦена: 9.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


@dp.message(F.text == "Нестле\nМолоко")
async def nest(message: types.Message):
    nest = "https://avatars.mds.yandex.net/get-mpic/6277643/img_id5231020731460371794.jpeg/orig"
    list.append("Нестле\nМолоко")
    lst.append("Nestle\nSutli")
    await message.answer_photo(photo=nest, caption="Нестле Молоко\nЦена: 9.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


@dp.message(F.text == "Нестле\nЧокнутый")
async def nest(message: types.Message):
    nest = "https://www.sladkiymarket.ru/upload/iblock/4fd/4fddcabff4d82b6e4da3b7eb1f9d1609.jpeg"
    list.append("Нестле\nЧокнутый")
    lst.append("Nestle\nYong'oq")
    await message.answer_photo(photo=nest, caption="Нестле Чокнутый\nЦена: 9.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


@dp.message(F.text == "Нестле\nГрейпфрут")
async def nest(message: types.Message):
    nest = "https://nesipetsin.com:7070/images/product/2020/09/24/15/b874caa8-4b0b-49c7-9a0f-a7134b7d53f8.jpg"
    list.append("Нестле\nГрейпфрут")
    lst.append("Nestle\nUzumli")
    await message.answer_photo(photo=nest, caption="Нестле Грейпфрут\nЦена: 9.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


@dp.message(F.text == "Нестле\nВафлями")
async def nest(message: types.Message):
    nest = "https://gipermix.ru/upload/iblock/a13/a1386cad4f519ad7ffaf8548302b5ba0.jpg"
    list.append("Нестле\nВафлями")
    lst.append("Nestle\nVafli")
    await message.answer_photo(photo=nest, caption="Нестле Вафлями\nЦена: 9.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


# Snikers
@dp.message(F.text == "Сникерс🍫")
async def snikers(message: types.Message):
    snikers = "https://o-manager.ru/foto/1205-0551.jpg"
    list.append("Сникерс")
    lst.append("Snickers")
    await message.answer_photo(photo=snikers, caption="Сникерс\nЦена: 8.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


# MilkyWay
@dp.message(F.text == "Млечный Путь\nмолочный")
async def milky(message: types.Message):
    milky = "https://mykaleidoscope.ru/uploads/posts/2022-07/1657292432_26-mykaleidoscope-ru-p-shokoladka-milki-vei-vkusnyashki-krasivo-f-46.jpg"
    list.append("Млечный Путь\nмолочный")
    lst.append("MilkyWay\nsutli")
    await message.answer_photo(photo=milky, caption="Млечный Путь молочный \nЦена: 6.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


@dp.message(F.text == "Млечный Путь\nШколойт")
async def milky(message: types.Message):
    milky = "https://imgproxy.sbermarket.ru/imgproxy/size-680-680/czM6Ly9jb250ZW50LWltYWdlcy1wcm9kL3Byb2R1Y3RzLzIzMDMwOTY3L29yaWdpbmFsLzEvMjAyMy0wMy0yNFQxMSUzQTQyJTNBNDcuNjY4MDAwJTJCMDAlM0EwMC8yMzAzMDk2N18xLmpwZw==.jpg"
    list.append("Млечный Путь\nШколойт")
    lst.append("MilkyWay\nshkoladli")
    await message.answer_photo(photo=milky, caption="Млечный Путь Школойт\nЦена: 6.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


# Oreo
@dp.message(F.text == "Орео\nШколойт")
async def oreo(message: types.Message):
    oreo = "https://mosnapitki.ru/upload/iblock/628/geg012xznduh965osxv1f7m6x949b8pa.jpg"
    list.append("Орео\nШколойт")
    lst.append("Oreo\nShkaladli")
    await message.answer_photo(photo=oreo, caption="Орео Школойт\nЦена: 10.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


@dp.message(F.text == "Орео\nКрасный вельвет")
async def oreo(message: types.Message):
    oreo = "https://eurotrade24.ru/d/123.jpg"
    list.append("Орео\nКрасный вельвет")
    lst.append("Oreo\nQizil Velvet")
    await message.answer_photo(photo=oreo, caption="Орео Красный вельвет\nЦена: 9.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


@dp.message(F.text == "Орео\nмолочный")
async def oreo(message: types.Message):
    oreo = "https://produktoff.kz/pictures/product/big/13652_big.png"
    list.append("Орео\nмолочный")
    lst.append("Oreo\nSutli")
    await message.answer_photo(photo=oreo, caption="Орео молочный\nЦена: 11.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


@dp.message(F.text == "Орео\nКлубника")
async def oreo(message: types.Message):
    oreo = "https://aws.kiiiosk.store/uploads/shop/9065/uploads/product_image/image/775624/4d21c418fdbf186a93b6ad15b5bdb5b820221203-555999-1hy0cg.jpg"
    list.append("Орео\nКлубника")
    lst.append("Oreo\nQulubnayli")
    await message.answer_photo(photo=oreo, caption="Орео Клубника\nЦена: 11.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


# M_MS
@dp.message(F.text == "М_МС\nАрахисом")
async def ememdes(message: types.Message):
    ememdes = "https://colodu.club/uploads/posts/2022-10/1666333528_17-colodu-club-p-shokolad-mmdems-plitka-dizain-vkontakte-18.jpg"
    list.append("М_МС\nАрахисом")
    lst.append("M_MS\nYeryong'oqli")
    await message.answer_photo(photo=ememdes, caption="Эмемдес Арахис \nЦена: 18.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


@dp.message(F.text == "М_МС\nШколойт")
async def ememdes(message: types.Message):
    ememdes = "https://cdn.shopify.com/s/files/1/0258/7626/7092/products/s-l1600_215d5183-339a-4331-9102-123ee4bc9e1a_1200x1200.jpg"
    list.append("М_МС\nШколойт")
    lst.append("M_MS\nShkoladli")
    await message.answer_photo(photo=ememdes, caption="Эмемдес Школадли\nЦена: 18.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


@dp.message(F.text == "М_МС\nМиндаль")
async def ememdes(message: types.Message):
    ememdes = "https://gas-kvas.com/uploads/posts/2023-08/1693461350_gas-kvas-com-p-risunki-na-prazdnik-den-shokoladnogo-drazh-38.jpg"
    list.append("М_МС\nМиндаль")
    lst.append("M_MS\nBodomli")
    await message.answer_photo(photo=ememdes, caption="Эмемдес Миндаль\nЦена: 18.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


@dp.message(F.text == "М_МС\nЗеленый Хрящ")
async def ememdes(message: types.Message):
    ememdes = "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1547831808-m-ms-milk-chocolate-bar-crispy-mint-1547831737.jpg?crop=1xw:1xh;center,top&resize=980:*"
    list.append("М_МС\nЗеленый Хрящ")
    lst.append("M_MS\nYashil Qarsildoqli")
    await message.answer_photo(photo=ememdes, caption="Эмемдеса зеленый шарф. \nЦена: 18.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


@dp.message(F.text == "М_МС\nCиний Хрящ")
async def ememdes(message: types.Message):
    ememdes = "https://i5.walmartimages.com/asr/ba2e7d18-97fe-4fc1-8c0d-c6db030dac63_1.fb012aee8ef94804c22e6f99df993d8b.jpeg"
    list.append("М_МС\nCиний Хрящ")
    lst.append("M_MS\nKok Qarsildoqli")
    await message.answer_photo(photo=ememdes, caption="Эмемдеса синий шарф\nЦена: 18.000 тысяч",
                               reply_markup=yesno_rus_shirinlikar)


#
#
#


# Ichimliklar

# Pepsi
@dp.message(F.text == "Пепси 2л")
async def pepsi(message: types.Message):
    pepsi = "https://nnjfood.ru/upload/iblock/1ac/2hfb9fdkd116ymdkxyattpyarm7vx8r1.jpg"
    list.append("Пепси 2л")
    lst.append("Pepsi 2L")
    await message.answer_photo(photo=pepsi, caption="Пепси 2л\nЦена: 18.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Пепси 1,5л")
async def pepsi(message: types.Message):
    pepsi = "https://cdn1.ozone.ru/s3/multimedia-j/6467676559.jpg"
    list.append("Пепси 1,5л")
    lst.append("Pepsi 1.5L")
    await message.answer_photo(photo=pepsi, caption="Пепси 1.5л\nЦена: 14.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Пепси 1л")
async def pepsi(message: types.Message):
    pepsi = "https://mastfood.ru/upload/iblock/963/96351b2eaba516210ad78f1682a89e19.jpg"
    list.append("Пепси 1л")
    lst.append("Pepsi 1L")
    await message.answer_photo(photo=pepsi, caption="Пепси 1л\nЦена: 11.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Пепси 0,5л")
async def pepsi(message: types.Message):
    pepsi = "https://mastfood.ru/upload/iblock/d98/d9808dad997dc328021c7675c9ca375e.jpg"
    list.append("Пепси 0,5л")
    lst.append("Pepsi 0.5L")
    await message.answer_photo(photo=pepsi, caption="Пепси 0,5л\nЦена: 6.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Пепси без сахара")
async def pepsi(message: types.Message):
    pepsi = "https://ekipazh-service.com.ua/wp-content/uploads/2020/01/pepsiblack300x230-1600x1056-1-1536x1014.png"
    list.append("Пепси без сахара")
    lst.append("Shakarsiz Pepsi")
    await message.answer_photo(photo=pepsi, caption="Пепси без сахара\nЦена: 6.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


# Coca Cola
@dp.message(F.text == "Кока-Кола 1,5л")
async def cola(message: types.Message):
    Cola = "https://clipart-library.com/image_gallery2/Coca-Cola-PNG-Clipart.png"
    list.append("Кока-Кола 1,5л")
    lst.append("Coca Cola 1.5L")
    await message.answer_photo(photo=Cola, caption="Кока-Кола 1,5л\nЦена: 15.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Кока-Кола 1л")
async def cola(message: types.Message):
    Cola = "https://bonsai.asia/d/hwg8hwyp30td0jr_9289fb4a.jpg"
    list.append("Кока-Кола 1л")
    lst.append("Coca Cola 1L")
    await message.answer_photo(photo=Cola, caption="Кока-Кола 1л\nЦена: 11.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Кока-Кола 0.5л")
async def cola(message: types.Message):
    Cola = "https://pacopizza.ru/wp-content/uploads/2022/09/cola-2.png"
    list.append("Кока-Кола 0.5л")
    lst.append("Coca Cola 0.5L")
    await message.answer_photo(photo=Cola, caption="Кока-Кола 0.5л\nЦена: 7.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Миллий кола")
async def cola(message: types.Message):
    Cola = "https://vendliga.ru/upload/resize_cache/iblock/73e/1200_1200_140cd750bba9870f18aada2478b24840a/aauf9xl6nwd6udmlpuuiy1r0zh86iyss.png"
    list.append("Миллий кола")
    lst.append("Milliy Cola")
    await message.answer_photo(photo=Cola, caption="Миллий кола\nЦена: 6.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Кока-Кола без сахара")
async def cola(message: types.Message):
    Cola = "https://images.uzum.uz/cegsalgv1htd23ajb1cg/original.jpg"
    list.append("Кока-Кола без сахара")
    lst.append("Shakarsiz Coca Cola")
    await message.answer_photo(photo=Cola, caption="Кока-Кола без сахара\nЦена: 7.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


# Fanta
@dp.message(F.text == "Фанта 1,5л")
async def Fanta(message: types.Message):
    Fanta = "https://puddostavka.ru/upload/iblock/69d/cydg6wcjv09y042cgtme7mife195oljb.jpg"
    list.append("Фанта 1,5л")
    lst.append("Fanta 1.5L")
    await message.answer_photo(photo=Fanta, caption="Фанта 1,5л\nЦена: 12.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Фанта 1л")
async def Fanta(message: types.Message):
    Fanta = "https://pirogi-osetia.ru/upload/iblock/4d1/l7g3oppicw4u0l12ixy7hxdlo7cdrthq.png"
    list.append("Фанта 1л")
    lst.append("Fanta 1L")
    await message.answer_photo(photo=Fanta, caption="Фанта 1л\nЦена: 10.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Фанта 0.5л")
async def Fanta(message: types.Message):
    Fanta = "https://korzina.su/upload/iblock/0cb/0cb34bf1bf860155f84e66a2619494a3.jpg"
    list.append("Фанта 0.5л")
    lst.append("Fanta 0.5L")
    await message.answer_photo(photo=Fanta, caption="Фанта 0.5л \nЦена: 6.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


# Tropic
@dp.message(F.text == "Тропик 1л")
async def tropic(message: types.Message):
    tropic = "https://images.uzum.uz/cfdu5i2g84cfbutu83ag/original.jpg"
    list.append("Тропик 1л")
    lst.append("Tropic 1L")
    await message.answer_photo(photo=tropic, caption="Тропик 1л\nЦена: 15.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Тропик 0.5л Манголи")
async def tropic(message: types.Message):
    tropic = "https://yukber.uz/image/cache/catalog/product/YK0184/YK0184_1-700x700.jpg"
    list.append("Тропик 0.5л Манголи")
    lst.append("Tropic 0.5L Mangoli")
    await message.answer_photo(photo=tropic, caption="Тропик 0.5л Манголи\nЦена: 5.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Тропик 0.5л Гуавали")
async def tropic(message: types.Message):
    tropic = "https://yukber.uz/image/cache/catalog/product/YK0182/YK0182_1-700x700.jpg"
    list.append("Тропик 0.5л Гуавали")
    lst.append("Tropic 0.5L Guavali")
    await message.answer_photo(photo=tropic, caption="Тропик 0.5л Гуавали\nЦена: 5.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


# Sprite
@dp.message(F.text == "Спрайт 1.5л")
async def sprite(message: types.Message):
    sprite = "https://www.okeydostavka.ru/wcsstore/OKMarketCAS/cat_entries/35207/35207_fullimage.jpg"
    list.append("Спрайт 1.5л")
    lst.append("Sprite 1.5L")
    await message.answer_photo(photo=sprite, caption="Спрайт 1.5л\nЦена: 13.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Спрайт 1л")
async def sprite(message: types.Message):
    sprite = "https://static.insales-cdn.com/r/BggRp8mShS8/rs:fit:1000:1000:1/plain/images/products/1/7022/642235246/спрайт_в_бутылке_1_л.jpg@jpg"
    list.append("Спрайт 1л")
    lst.append("Sprite 1L")
    await message.answer_photo(photo=sprite, caption="Спрайт 1л\nЦена: 10.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Спрайт 0.5л")
async def sprite(message: types.Message):
    sprite = "https://cdn1.ozone.ru/s3/multimedia-1-8/6933372740.jpg"
    list.append("Спрайт 0.5л")
    lst.append("Sprite 0.5L")
    await message.answer_photo(photo=sprite, caption="Спрайт 0.5л\nЦена: 6.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


# Lipton
@dp.message(F.text == "Липтон 1.5л\nОрик")
async def Lipton(message: types.Message):
    Lipton = "https://palladi.ru/upload/iblock/47a/47a14aefd80abbf92a35d8f5648469e1.jpg"
    list.append("Липтон 1.5л\nОрик")
    lst.append("Lipton 1.5L\nOrik")
    await message.answer_photo(photo=Lipton, caption="Липтон 1.5л Орик\nЦена: 10.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Липтон 1л\nОрик")
async def Lipton(message: types.Message):
    Lipton = "https://planetavkysov.ru/image/cache/resize/s/1200x630/catalog/napitki/4600494600531.jpg"
    list.append("Липтон 1л\nОрик")
    lst.append("Lipton 1L\nOrik")
    await message.answer_photo(photo=Lipton, caption="Липтон 1л Орик\nЦена: 7.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Липтон 0.5л\nОрик")
async def Lipton(message: types.Message):
    Lipton = "https://tornado.shop/images/detailed/25/P1342254.jpg"
    list.append("Липтон 0.5л\nОрик")
    lst.append("Lipton 0.5L\nOrik")
    await message.answer_photo(photo=Lipton, caption="Липтон 0.5л Орик\nЦена: 5.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Липтон 1,5л\nЗеленый")
async def lipton(message: types.Message):
    lipton = "https://dobrodusha.ru/image/cache/catalog/liptonicetea/zel1.5-800x800.jpg"
    list.append("Липтон 1,5л\nЗеленый")
    lst.append("Lipton 1.5L\nYashil")
    await message.answer_photo(photo=lipton, caption="Липтон 1,5л Зеленый\nЦена: 10.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Липтон 1л\nЗеленый")
async def lipton(message: types.Message):
    lipton = "https://losossir.ru/uploads/catalog/napitki/zelenyjchajlipton.png"
    list.append("Липтон 1л\nЗеленый")
    lst.append("Lipton 1L\nYashil")
    await message.answer_photo(photo=lipton, caption="Липтон 1л Зеленый\nЦена: 7.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Липтон 0.5л\nЗеленый")
async def lipton(message: types.Message):
    lipton = "https://cdn-ru5.foodpicasso.com/assets/2024/02/20/892a919ecd6964bf2cd42403199b5cda---jpg_1000x_103c0_convert.jpg"
    list.append("Липтон 0.5л\nЗеленый")
    lst.append("Lipton 0.5L\nYashil")
    await message.answer_photo(photo=lipton, caption="Липтон 0.5л Зеленый\nЦена: 5.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Липтон 1,5л\nЛимон")
async def lipton(message: types.Message):
    lipton = "https://ccm76.ru/wp-content/uploads/2022/06/lipton-2-scaled.jpg"
    list.append("Липтон 1,5л\nЛимон")
    lst.append("Lipton 1.5L\nLimon")
    await message.answer_photo(photo=lipton, caption="Липтон 1,5л Лимон\nЦена: 10.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Липтон 1л\nЛимон")
async def lipton(message: types.Message):
    lipton = "https://www.meme-arsenal.com/memes/16ec18cab6e6cbd93b50ec5e029c6a76.jpg"
    list.append("Липтон 1л\nЛимон")
    lst.append("Lipton 1L\nLimon")
    await message.answer_photo(photo=lipton, caption="Липтон 1л Лимон\nЦена: 7.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)


@dp.message(F.text == "Липтон 0.5л\nЛимон")
async def lipton(message: types.Message):
    lipton = "https://globusgurme.ru/upload/preview/iblock/fa4/pvjsntobhhedag4xs9d9qd02g2sapb25800_800_thumb_v2_0.jpg"
    list.append("Липтон 0.5л\nЛимон")
    lst.append("Lipton 0.5L\nLimon")
    await message.answer_photo(photo=lipton, caption="Липтон 0.5л Лимон\nЦена: 5.000 тысяч",
                               reply_markup=yesno_rus_ichimliklar)
