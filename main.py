import random

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from config import bot, dp

@dp.message_handler(commands=['quiz'])
async def s1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)
    question = "Независимость Америки(год)?"
    answers = [
        "1756 лет",
        "1804 лет",
        "1776 лет",
        "1805 лет",
        "1769 лет",
    ]

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="неправильно!",
        reply_markup=markup
    )

@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def s2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_2)
    question = "В чем смысл жизни?"
    answers = [
        "нету смысла",
        "для продолжения рода",
        "развития себя ",
        "сам определяеш смысл",
        "просто жить без смысла",
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="неправильно!",
        reply_markup=markup
    )


@dp.message_handler(commands=['Mem'])
async def echo(message: types.Message):
    ff = random.randint(1, 2)
    if ff == 1:
        photo = open('madia/memy1.jpg', 'rb')
        await bot.send_photo(message.from_user.id, photo)
    elif ff == 2:
        photo = open('madia/memy2.jpg', 'rb')
        await bot.send_photo(message.from_user.id, photo)


@dp.message_handler()
async def echo(message: types.Message):
    sms = (message.text == type(int))
    sas = message.text
    daff = int(sas) * int(sas)

    if sms == False:
        await bot.send_message(message.from_user.id, daff)
    elif sms == True:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



# ХОМЕ ВОРК:
# 1. Создать своего бота .
# 2. Проделать все настройки (включая
# скрытия токен ключа бота)
# 3. Придумайте любую викторину из
# двух вопросов.
# 4. Написать hendler который
# принимает команду mem и
# отправляет любое мем или
# прикольную картинку.
# 5. В случае если пустой message
# hendler принимает число, он должен
# отправлять ее же возведенную в
# квадрат. Иначе отправляет тоже
# самое (эхо).





