class Weather:
    location = ''
    conditions = {'clear': 'ясно', 'partly-cloudy': 'малооблачно', 'cloudy': 'облачно с прояснениями',
                  'overcast': 'пасмурно', 'drizzle': 'морось', 'light-rain': 'небольшой дождь', 'rain': 'дождь',
                  'moderate-rain': 'умеренно сильный дождь', 'heavy-rain': 'сильный дождь',
                  'continuous-heavy-rain': 'длительный сильный дождь', 'showers': 'ливень',
                  'wet-snow': 'дождь со снегом', 'light-snow': 'небольшой снег', 'snow': 'снег',
                  'snow-showers': 'снегопад', 'hail': 'град', 'thunderstorm': 'гроза',
                  'thunderstorm-with-rain': 'дождь с грозой', 'thunderstorm-with-hail': 'гроза с градом'}
    wind_dir = {'nw': 'северо-западный', 'n': 'северный', 'ne': 'северо-восточный', 'e': 'восточный',
                'se': 'юго-восточный', 's': 'южный', 'sw': 'юго-западный', 'w': 'западный', 'c': 'штиль'}


class Horo:
    zodiac = ''
    period = ''
    keys = {'aries': '♈ Овен', 'taurus': '♉ Телец', 'gemini': '♊ Близнецы', 'cancer': '♋ Рак', 'leo':  '♌ Лев',
            'virgo': '♍ Дева', 'libra': '♎ Весы', 'scorpio': '♏ Скорпион', 'sagittarius': '♐ Стрелец',
            'capricorn': '♐ Козерог', 'aquarius': '♒ Водолей', 'pisces': '♒ Рыбы'}


class Currency:
    currency = ''
    amount = 0
    currency_codes = {'AUD': 'A$ Австралийский доллар', 'AZN': '₼ Азербайджанский манат', 'GBP': '£ Фунт стерлингов',
                      'AMD': 'Դ Армянский драм', 'BYN': 'Br Белорусский рубль', 'BGN': 'лв Болгарский лев',
                      'BRL': 'R$ Бразильский реал', 'HUF': 'ƒ Венгерский форинт', 'KRW': '₩ Вона Республики Корея',
                      'HKD': 'HK$ Гонконгскй доллар', 'DKK': 'kr Датская крона', 'USD': '$ Доллар США', 'EUR': '€ Евро',
                      'INR': '₹ Индийская рупия', 'KZT': '₸ Казахстанский тенге', 'CAD': 'C$ Канадский доллар',
                      'KGS': 'с Киргизский сом', 'CNY': '¥ Китайский юань', 'MDL': 'L Молдавский лей',
                      'TMT': 'TMT Новый туркменский манат', 'NOK': 'kr Норвежская крона', 'PLN': 'zł Польский злотый',
                      'RON': 'lei Румынский лей', 'SGD': 'S$ Сингапурский доллар', 'TJS': 'SM Таджикский сомони',
                      'TRY': '₺ Турецкая лира', 'UZS': 'Soʻm Узбекский сум', 'UAH': '₴ Украинская гривна',
                      'CZK': 'Kč Чешская крона', 'SEK': 'kr Шведская крона', 'CHF': 'Fr. Швейцарский франк',
                      'ZAR': 'R Южноафриканский рэнд', 'JPY': '¥ Японская иена'}


def print_currency_codes():
    currency_codes = ''
    for k in Currency.currency_codes.keys():
        currency_codes += k + ': ' + Currency.currency_codes[k][Currency.currency_codes[k].find(' '):] + '\n'
    return currency_codes
