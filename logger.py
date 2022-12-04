import datetime


def log(user):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{user} at {datetime.datetime.now()}\n')
    print(user)
