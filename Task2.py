from datetime import datetime


def dec_with_path(path):
    def decorator(old_function):
        def new_function(*args, **kwargs):
            with open(path, 'a', encoding='utf-8') as f:
                result = old_function(*args, **kwargs)
                f.write(f'{datetime.now().strftime(("%d/%m/%Y %H:%M:%S"))} Вызвана функция {old_function.__name__}\n'
                        f'позиционные - {args} именнованные - {kwargs}\n'
                        f'возвращаемое значение - {result}\n')
            return result
        return new_function
    return decorator


@dec_with_path('task2.txt')
def simple_sum(a, b):
    return a + b


@dec_with_path('task2.txt')
def simple_sub(numb1=456, numb2=123):
    return numb1 - numb2

simple_sum(124, 148)
simple_sub(numb1=654, numb2=221)

