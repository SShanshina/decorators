import os
import requests
from datetime import datetime
from typing import Callable


def fabric_log_decorator(log_path):

    def log_decorator(old_function: Callable):

        def new_function(*args):
            result = old_function(*args)
            with open(log_path, 'w', encoding='utf-8') as f:
                f.write(f'Вызвана функция {old_function.__name__}\n'
                        f'С аргументами {args}\n'
                        f'Получен результат: {result}\n'
                        f'Дата и время вызова функции: {datetime.now()}\n')
            return result
        return new_function

    return log_decorator


@fabric_log_decorator(os.path.join('D:\\', 'Sofya', 'log_file2.txt'))
def get_heroes_data(*args):

    response_list = list()

    for hero in args:
        response = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{hero}')

        for results in response.json()['results']:
            response_list.append(results)

            character_list = list()
            for data in response_list:
                name = data['name']
                intelligence = int(data['powerstats']['intelligence'])
                character_list.append([name, intelligence])

    sort_el_index = 1

    def sort_by_el(i):
        return i[sort_el_index]

    max_int_char = max(character_list, key=sort_by_el)

    return f"{max_int_char[0]} is the most intelligent one, his/her intelligence is {max_int_char[1]}"


print(get_heroes_data('Hulk', 'Captain America', 'Thanos'))
