import os 
from dotenv import load_dotenv
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
import keyboard
import emoji

load_dotenv()
TOKEN = os.getenv("TELEGRAM_API_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Что умеет этот бот?\n\nЯ бот караоке YARD\nС моей помощью Вы сможете:\n\
        - Получить бонусы и скидки\n\
        - Ознакомиться с нашим меню\n\
        - Узнать про ближайшие события\n\
        и  многое другое...')

@dp.message(Command('help'))
async def cmd_help(message: types.Message):
    await message.answer('Для получения необходимой информации используйте меню!')

@dp.message(Command('menu'))
async def cmd_menu(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Посмотреть меню",
        url="https://yardkaraoke.ru/wp-content/themes/yard_theme/assets/menu.pdf"
    ))
    await message.answer(emoji.emojize('Ознакомиться с меню можно на нашем сайте :backhand_index_pointing_down:') ,
    reply_markup=builder.as_markup())
    document = FSInputFile('menu.pdf')
    await message.answer_document(document)

@dp.message(Command('events'))
async def cmd_events(message: types.Message):
    poster = FSInputFile('poster.jpeg')
    await message.answer_photo(poster)
    await message.answer(emoji.emojize("<b>:black_medium_square:Halloween в караоке-баре YARD:black_medium_square:</b>\n:spiral_calendar: 27, 28, 29 октября\n:alarm_clock:  20:00\n:round_pushpin:  г. Москва, ул. Наметкина, д. 3\n\nHalloween» — это возможность повеселиться в компании друзей, перевоплотиться в своего кумира или облачиться в костюм нечисти. Готовы развлекаться и заряжаться позитивом? Тогда встречайте один из главных праздников осени в караоке-баре Yard"), parse_mode="HTML")
    #await message.answer(emoji.emojize("<b>:white_medium_square:All White Party:white_medium_square:</b>\n:spiral_calendar: 07 июля\n:alarm_clock:  20:00\n:round_pushpin:  г. Москва, ул. Наметкина, д. 3\n\nCамое элегантый вечер этого года в караоке YARD. Шоу программа под хиты на все времена\n\nВ программе:\n:microphone:  The Toy Band\n:microphone:  Monterra\n\n:man_dancing:  Ведущий вечера <b>Лео</b>\n\n:red_exclamation_mark:  Dress Code: в белом  :red_exclamation_mark:"), parse_mode="HTML")

@dp.message(Command('contacts'))
async def cmd_contacts(message: types.Message):
    await message.answer(emoji.emojize("Контактные данные:\n:telephone_receiver: +7 977 697 77 07\n:desktop_computer: yardkaraoke.ru\n\nНаш адрес и время работы:\n:round_pushpin:  г. Москва, ул. Наметкина, д. 3\n:alarm_clock:  20:00 - 06:00"), parse_mode="HTML")

@dp.message(Command('rules'))
async def cmd_rules(message: types.Message):
    rules = FSInputFile('rules.jpeg')
    await message.answer_photo(rules)

@dp.message(Command('catalogue'))
async def cmd_catalogue(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Посмотреть каталог",
        url="https://www.art-system.ru/servis-i-podderzhka/programmnoe-obespechenie/ast-catalog-elektronnyy-katalog-pesen/"
    ))
    await message.answer(emoji.emojize("Ознакомится с полным каталогом песен Вы можете по ссылке :backhand_index_pointing_down:"),
    reply_markup=builder.as_markup())

@dp.message(Command('reserve'))
async def cmd_contacts(message: types.Message):
    await message.answer(emoji.emojize("Забронировать стол можно по телефону или на нашем сайте:\n:telephone_receiver: +7 977 697 77 07\n:desktop_computer: yardkaraoke.ru\n\nНаш адрес и время работы:\n:round_pushpin:  г. Москва, ул. Наметкина, д. 3\n:alarm_clock:  20:00 - 06:00"), parse_mode="HTML")


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
