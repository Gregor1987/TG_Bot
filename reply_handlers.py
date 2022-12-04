from keyboards import *
import parser
import variables


def weather_where(message):
    variables.Weather.location = message.text
    if variables.Weather.location != 'Назад':
        if variables.Weather.location == 'Тюмень':
            variables.Weather.location = 'lat=57.15298462&lon=65.54122925'
        elif variables.Weather.location == 'Пермь':
            variables.Weather.location = 'lat=58.01045227&lon=56.2294426'
        msg = bot.send_message(message.chat.id, 'Когда?', reply_markup=keyboard_weather_when)
        bot.register_next_step_handler(msg, weather_when)
    else:
        bot.send_message(message.chat.id, 'Чем я еще могу помочь?', reply_markup=keyboard_main)


def weather_when(message):
    variables.Weather.when = message.text
    if variables.Weather.when != 'Назад':
        bot.send_message(message.chat.id, parser.weather(variables.Weather.location, variables.Weather.when),
                         reply_markup=keyboard_main)
    else:
        bot.send_message(message.chat.id, 'Чем я еще могу помочь?', reply_markup=keyboard_main)


def horo_zodiac(message):
    variables.Horo.zodiac = message.text
    if variables.Horo.zodiac != 'Назад':
        if 'Овен' in variables.Horo.zodiac:
            variables.Horo.zodiac = 'aries'
        elif 'Телец' in variables.Horo.zodiac:
            variables.Horo.zodiac = 'taurus'
        elif 'Близнецы' in variables.Horo.zodiac:
            variables.Horo.zodiac = 'gemini'
        elif 'Рак' in variables.Horo.zodiac:
            variables.Horo.zodiac = 'cancer'
        elif 'Лев' in variables.Horo.zodiac:
            variables.Horo.zodiac = 'leo'
        elif 'Дева' in variables.Horo.zodiac:
            variables.Horo.zodiac = 'virgo'
        elif 'Весы' in variables.Horo.zodiac:
            variables.Horo.zodiac = 'libra'
        elif 'Скорпион' in variables.Horo.zodiac:
            variables.Horo.zodiac = 'scorpius'
        elif 'Стрелец' in variables.Horo.zodiac:
            variables.Horo.zodiac = 'sagittarius'
        elif 'Козерог' in variables.Horo.zodiac:
            variables.Horo.zodiac = 'capricorn'
        elif 'Водолей' in variables.Horo.zodiac:
            variables.Horo.zodiac = 'aquarius'
        elif 'Рыбы' in variables.Horo.zodiac:
            variables.Horo.zodiac = 'pisces'
        msg = bot.send_message(message.chat.id, 'На какой период?', reply_markup=keyboard_horo_period)
        bot.register_next_step_handler(msg, horo_period)
    else:
        bot.send_message(message.chat.id, 'Чем я еще могу помочь?', reply_markup=keyboard_main)


def horo_period(message):
    variables.Horo.period = message.text
    if variables.Horo.period != 'Назад':
        if variables.Horo.period == 'Сегодня':
            variables.Horo.period = '/today/'
        elif variables.Horo.period == 'Завтра':
            variables.Horo.period = '/tomorrow/'
        elif variables.Horo.period == 'Неделя':
            variables.Horo.period = '/week/'
        elif variables.Horo.period == 'Месяц':
            variables.Horo.period = '/month/'
        bot.send_message(message.chat.id, parser.horoscope(variables.Horo.zodiac, variables.Horo.period),
                         reply_markup=keyboard_main)
    else:
        bot.send_message(message.chat.id, 'Чем я еще могу помочь?', reply_markup=keyboard_main)


def currency(message):
    curr = message.text
    if curr != 'Назад':
        bot.send_message(message.chat.id, parser.currency(curr), reply_markup=keyboard_main)
    else:
        bot.send_message(message.chat.id, 'Чем я еще могу помочь?', reply_markup=keyboard_main)
