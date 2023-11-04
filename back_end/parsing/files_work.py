import os.path
from .driver_work import get_site_code


def save_code_to_file(code, fileName):
    with open(fileName + ".html", "w", encoding="utf-8") as f:
        f.write(code)


def read_data_from_file(fileName):
    with open(fileName + ".html", "r", encoding="utf-8") as f:
        response = f.read()
    return response

def return_response(url, fileName):
    """Возвращает ответ(код сайта) двумя способами:
    1) чтение из файла
    2) парсинг из интернета"""

    if not(os.path.isfile(f'back_end/parsing/files/{fileName}.html')):
        response = get_site_code(url)
        save_code_to_file(response, "back_end/parsing/files/" + fileName)
    else:
        response = read_data_from_file("back_end/parsing/files/" + fileName)

    return response