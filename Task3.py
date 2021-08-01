from datetime import datetime
from WebScrapping.scrap import HabrScrapp

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


@dec_with_path('task3.txt')
def main():
    scrap = HabrScrapp('Scrap')
    return scrap.scrap()


if __name__ == '__main__':
        main()
