import parser
from keyboards import *
import reply_handlers
import logger
import variables


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! Чем могу помочь?', reply_markup=keyboard_main)
    logger.log(message.from_user.first_name, message.chat.id)


@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text == 'Погода':
        msg = bot.send_message(message.chat.id, 'Где?', reply_markup=keyboard_weather_location)
        bot.register_next_step_handler(msg, reply_handlers.weather)
    if message.text == 'Гороскоп':
        bot.send_message(message.chat.id, 'Какой?', reply_markup=keyboard_horo_zodiac)
    if message.text == 'Конвертация валюты':
        msg = bot.send_message(message.chat.id, 'Введите код валюты', reply_markup=keyboard_currency_ids)
        bot.register_next_step_handler(msg, reply_handlers.currency_code)
    if message.text == 'Астрономическое фото дня':
        if parser.apods()['media_type'] == 'video':
            bot.send_video(message.chat.id, parser.apods()['url'], reply_markup=keyboard_main)
        elif parser.apods()['media_type'] == 'image':
            bot.send_photo(message.chat.id, parser.apods()['url'], parser.apods()['explanation'][:parser.apods()['explanation'].rfind('.')+1], reply_markup=keyboard_main)
    if message.text == 'Назад':
        bot.send_message(message.chat.id, 'Чем я еще могу помочь?', reply_markup=keyboard_main)


@bot.callback_query_handler(func=lambda callback: callback.data)
def callback_query(callback):
    if callback.data != 'Назад':
        variables.Horo.zodiac = callback.data
        msg = bot.send_message(callback.message.chat.id, 'На какой период?', reply_markup=keyboard_horo_period)
        bot.register_next_step_handler(msg, reply_handlers.horo_period)
    else:
        bot.send_message(callback.message.chat.id, 'Чем я еще могу помочь?', reply_markup=keyboard_main)


bot.polling(none_stop=True)
