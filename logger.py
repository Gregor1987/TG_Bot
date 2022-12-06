import datetime


def log(user_name, chat_id):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{user_name} started chat at {datetime.datetime.now().strftime("%H:%M %m.%d.%Y")}, chat ID {chat_id}\n')
