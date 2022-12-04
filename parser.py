from bs4 import BeautifulSoup
import requests


def weather(location, when):
    url = 'https://yandex.com.am/weather/?' + location
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    if when == 'Погода сейчас':
        return (bs.find('h1', 'title title_level_1 header-title__title').text + '\n' +
                bs.find('span', 'temp__value temp__value_with-unit').text + '°C, ' +
                bs.find('div', 'link__condition day-anchor i-bem').text + '\nВетер: ' +
                bs.find('span', 'wind-speed').text + ' ' + bs.find('span', 'fact__unit').text + '\n' +
                bs.find('div', 'term term_orient_h fact__feels-like').text + '°C')
    elif when == 'Погода на завтра':
        return bs.find('div', 'title-icon__text').text.replace('· ', '')


def horoscope(zodiac, period):
    url = 'https://horo.mail.ru/prediction/' + zodiac + period
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'lxml')
    return (bs.find('h1', 'hdr__inner').text + '\n\n' +
            bs.find('div', 'article__item article__item_alignment_left article__item_html').text)


def currency(message):
    url = 'https://cbr.ru/'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    result = 'Курс ЦБРФ на ' + bs.find_all('div', 'col-md-2 col-xs-7 _right')[1].get_text() + '\n'
    if 'Доллар США' in message:
        result += '1$ = ' + bs.find_all('div', 'col-md-2 col-xs-9 _right mono-num')[1].get_text()
    elif 'Евро' in message:
        result += '1€ = ' + bs.find_all('div', 'col-md-2 col-xs-9 _right mono-num')[3].get_text()
    return result
