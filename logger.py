from datetime import datetime
from pathlib import Path


def log_decorator(directory, filename):
    """Декоратор создает файл с логом для функции, переданной в него.В directory нужно указать папку или путь к папке,
    в которой срохраниться файл с логом (по умаолчанию путь в домашнюю директорию пользователя)"""
    path = Path.home() / directory  # Указываем папку/путь для файла с логом
    path.mkdir(parents=True, exist_ok=True)  # Создаем папку, если ее нет в каталоге
    f = path / filename  # Указываем файл с логом в директории
    f.touch()  # Создать пустой файла с логом

    def wrapper(func):
        def inner(*args, **kwargs):
            start_time = datetime.now()
            result = func(*args, **kwargs)
            with open(f, 'a') as file:
                file.write(
                    f"Start app: {func.__name__}\n"
                    f"Start time: {start_time}\n"
                    f"arg: {args, kwargs}\n"
                    f"result: {result}\n"
                    f"--------------------------\n"
                )
            # p = Path('log.txt')
            # p.write_text(f"Start app: {func.__name__}\nStart time: {start_time}\narg: {args, kwargs}\nresult: {result}\n--------------------------")
            return result

        return inner

    return wrapper
