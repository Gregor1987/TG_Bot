import telebot
from key import token

bot = telebot.TeleBot(token)

keyboard_main = telebot.types.ReplyKeyboardMarkup(True)
keyboard_main.row('Погода', 'Гороскоп')
keyboard_main.row('Курсы валют', 'Идиотский тест')

keyboard_weather_location = telebot.types.ReplyKeyboardMarkup(True)
keyboard_weather_location.row('Тюмень', 'Пермь')
keyboard_weather_location.row('Назад')

keyboard_weather_when = telebot.types.ReplyKeyboardMarkup(True)
keyboard_weather_when.row('Погода сейчас', 'Погода на завтра')
keyboard_weather_when.row('Назад')

keyboard_horo_zodiac = telebot.types.ReplyKeyboardMarkup(True)
keyboard_horo_zodiac.row('♈ Овен', '♉ Телец', '♊ Близнецы')
keyboard_horo_zodiac.row('♋ Рак', '♌ Лев', '♍ Дева')
keyboard_horo_zodiac.row('♎ Весы', '♏ Скорпион', '♐ Стрелец')
keyboard_horo_zodiac.row('♐ Козерог', '♒ Водолей', '♒ Рыбы')
keyboard_horo_zodiac.row('Назад')

keyboard_horo_period = telebot.types.ReplyKeyboardMarkup(True)
keyboard_horo_period.row('Сегодня', 'Завтра')
keyboard_horo_period.row('Неделя', 'Месяц')
keyboard_horo_period.row('Назад')

keyboard_currency = telebot.types.ReplyKeyboardMarkup(True)
keyboard_currency.row('$ Доллар США', '€ Евро')
keyboard_currency.row('Назад')

