from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class Form(StatesGroup):
    set_bg_color =State()
    set_background = State()
