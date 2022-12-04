from keyboards import *
import reply_handlers
import logger


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Чем могу помочь?', reply_markup=keyboard_main)
    logger.log(message.from_user.first_name)


@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text == 'Погода':
        msg = bot.send_message(message.chat.id, 'Где?', reply_markup=keyboard_weather_location)
        bot.register_next_step_handler(msg, reply_handlers.weather_where)
    if message.text == 'Гороскоп':
        msg = bot.send_message(message.chat.id, 'Какой?', reply_markup=keyboard_horo_zodiac)
        bot.register_next_step_handler(msg, reply_handlers.horo_zodiac)
    if message.text == 'Курсы валют':
        msg = bot.send_message(message.chat.id, 'Выберите валюту', reply_markup=keyboard_currency)
        bot.register_next_step_handler(msg, reply_handlers.currency)

    if message.text == 'Назад':
        bot.send_message(message.chat.id, 'Чем я еще могу помочь?', reply_markup=keyboard_main)


bot.polling()
# https://www.youtube.com/results?search_query=minecraft
# https://www.youtube.com/results?search_query=minecraft&sp=CAE%253D
# https://www.youtube.com/results?search_query=geekbrains&sp=CAE%253D
# https://www.youtube.com/results?search_query=geekbrains&sp=CAM%253D