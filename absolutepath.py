"""Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
 Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""


def absolute_path(path: str) -> tuple:
    """Функция принимает на вход авбсолютный путь до файла в виде строки и возвращает кортеж:
    путь, имя файла, расширение файла"""
    last_slash_index = 0
    lats_dot_index = 0
    for i in range(0, len(path)):
        if path[i] == ".":
            lats_dot_index = i
        if path[i] == "\\":
            last_slash_index = i

    path_name_ext = path[0:last_slash_index], path[last_slash_index+1:lats_dot_index], path[lats_dot_index+1::]
    return path_name_ext


path = r"C:\Users\gusev\OneDrive\JAVA_GEEK_BRAINS\python углубление\Лекция 1. Погружение в Python. Основы Python (1).pdf"
print(absolute_path(path))
