import telebot
from key import token_bot
from telebot import types
import variables

bot = telebot.TeleBot(token_bot)

keyboard_main = types.ReplyKeyboardMarkup(True)
keyboard_main.row('Погода', 'Гороскоп')
keyboard_main.row('Конвертация валюты', 'Астрономическое фото дня')

keyboard_weather_location = types.ReplyKeyboardMarkup(True)
key_location = types.KeyboardButton(text='Мое местоположение', request_location=True)
keyboard_weather_location.row('Тюмень', 'Пермь')
keyboard_weather_location.row(key_location)
keyboard_weather_location.row('Назад')

keyboard_weather_when = types.ReplyKeyboardMarkup(True)
keyboard_weather_when.row('Погода сейчас', 'Погода на завтра')
keyboard_weather_when.row('Назад')

keyboard_horo_zodiac = types.InlineKeyboardMarkup()
for k in variables.Horo.keys:
    key = types.InlineKeyboardButton(variables.Horo.keys[k], callback_data=k)
    keyboard_horo_zodiac.add(key)

keyboard_horo_period = types.ReplyKeyboardMarkup(True)
keyboard_horo_period.row('Сегодня', 'Завтра')
keyboard_horo_period.row('Неделя', 'Месяц')
keyboard_horo_period.row('Назад')

keyboard_currency = types.ReplyKeyboardMarkup(True)
keyboard_currency.row('Назад')

keyboard_currency_ids = types.ReplyKeyboardMarkup(True)
keyboard_currency_ids.row('Справочник кодов валют')
keyboard_currency_ids.row('Назад')
