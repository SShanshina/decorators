from datetime import datetime
from typing import Callable


def log_decorator(old_function: Callable):

    def new_function(*args):
        result = old_function(*args)
        with open('log_file.txt', 'w', encoding='utf-8') as f:
            f.write(f'Вызвана функция {old_function.__name__}\n'
                    f'С аргументами {args}\n'
                    f'Получен результат {result}\n'
                    f'Дата и время вызова функции: {datetime.now()}\n')
        return result

    return new_function


@log_decorator
def addition(*args):
    return sum(args)


addition(2, 5, 3, 6, 9, 11)
