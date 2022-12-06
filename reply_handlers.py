from keyboards import *
import parser
import variables


def weather(message):
    if message.text != 'Назад':
        if message.text == 'Пермь':
            variables.Weather.location = 'lat=58.01045227&lon=56.2294426'
        elif message.text == 'Тюмень':
            variables.Weather.location = 'lat=57.15298462&lon=65.54122925'
        else:
            variables.Weather.location = f'lat={message.location.latitude}&lon={message.location.longitude}'
            bot.delete_message(message.chat.id, message.id)
        bot.send_message(message.chat.id, parser.weather(variables.Weather.location), reply_markup=keyboard_main)
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


def currency_code(message):
    if message.text != 'Назад' and message.text != 'Справочник кодов валют':
        if message.text.upper() in variables.Currency.currency_codes.keys():
            variables.Currency.currency = message.text.upper()
            msg = bot.send_message(message.chat.id, 'Введите количество', reply_markup=keyboard_currency)
            bot.register_next_step_handler(msg, currency_amount)
        else:
            msg = bot.send_message(message.chat.id, 'Валюты с таким кодом нет, попробуйте еще раз',
                                   reply_markup=keyboard_currency_ids)
            bot.register_next_step_handler(msg, currency_code)
    elif message.text == 'Справочник кодов валют':
        msg = bot.send_message(message.chat.id, variables.print_currency_codes(), reply_markup=keyboard_currency_ids)
        bot.register_next_step_handler(msg, currency_code)
    else:
        bot.send_message(message.chat.id, 'Чем я еще могу помочь?', reply_markup=keyboard_main)


def currency_amount(message):
    if message.text != 'Назад':
        variables.Currency.amount = message.text.replace(',', '.')
        if variables.Currency.amount.replace('.', '', 1).isdigit():
            variables.Currency.amount = float(variables.Currency.amount)
            bot.send_message(message.chat.id, parser.currency_converter(variables.Currency.amount, variables.Currency.currency),
                             reply_markup=keyboard_main)
        else:
            msg = bot.send_message(message.chat.id, 'Количество введено некорректно, попробуйте еще раз',
                                   reply_markup=keyboard_currency)
            bot.register_next_step_handler(msg, currency_amount)
    else:
        bot.send_message(message.chat.id, 'Чем я еще могу помочь?', reply_markup=keyboard_main)
