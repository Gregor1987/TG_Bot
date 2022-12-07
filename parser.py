from bs4 import BeautifulSoup
import xml.etree.ElementTree
import requests
import key
import variables
import json


def weather(location):
    response = json.loads(
        requests.get(f'https://api.weather.yandex.ru/v2/forecast?{location}&ru_RU&limit=2&hours=false',
                     headers={'X-Yandex-API-Key': key.token_yandex}).text)
    return (f"По данным сервиса Яндекс.Погода\n"
            f"{response['geo_object']['locality']['name']}, {response['geo_object']['province']['name']}, "
            f"{response['geo_object']['country']['name']}\n{response['fact']['temp']}°C, "
            f"{variables.Weather.conditions[response['fact']['condition']]}\nВетер "
            f"{variables.Weather.wind_dir[response['fact']['wind_dir']]} {response['fact']['wind_speed']} м/с\n"
            f"Влажность {response['fact']['humidity']}%, давление {response['fact']['pressure_mm']} мм рт.ст.\n"
            f"Ощущается как {response['fact']['feels_like']}°C")


def horoscope(zodiac, period):
    response = requests.get('https://horo.mail.ru/prediction/' + zodiac + period)
    bs = BeautifulSoup(response.text, 'lxml')
    return (bs.find('h1', 'hdr__inner').text + '\n\n' +
            bs.find('div', 'article__item article__item_alignment_left article__item_html').text)


def currency_converter(amount, currency):
    root = xml.etree.ElementTree.fromstring(requests.get('https://cbr.ru/scripts/XML_daily.asp?').text)
    for currency_ID in root.findall('Valute'):
        if currency_ID.find('CharCode').text == currency:
            return(f"По курсу ЦБ РФ на {root.get('Date')}\n{currency_ID.find('Nominal').text} "
                   f"{currency_ID.find('Name').text} = {currency_ID.find('Value').text} ₽\n\n"
                   f"{amount} {variables.Currency.currency_codes[currency][:variables.Currency.currency_codes[currency].find(' ')]} = "
                   f"{round(amount * float(currency_ID.find('Value').text.replace(',', '.')) / float(currency_ID.find('Nominal').text), 2)} ₽\n"
                   f"{amount} ₽ = {round(amount / float(currency_ID.find('Value').text.replace(',', '.')) * float(currency_ID.find('Nominal').text), 2)} "
                   f"{variables.Currency.currency_codes[currency][:variables.Currency.currency_codes[currency].find(' ')]}")


def apods():
    return json.loads(requests.get(f'https://api.nasa.gov/planetary/apod?api_key'
                                   f'={key.token_nasa}').text)
