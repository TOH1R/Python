from aiogram.fsm.state import State, StatesGroup


class Card(StatesGroup):
    card_number = State()
    card_number_1 = State()


class Registration(StatesGroup):
    first_name = State()
    last_name = State()
    phone_number = State()
    location = State()

class Karta(StatesGroup):
    card_number = State()
    update_data = State()
    
class Chatgpt(StatesGroup):
    text = State()   