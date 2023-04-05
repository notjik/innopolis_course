"""
Написать регулярное выражение, для проверки правильности введенного ip адреса.
Диапазон ip адресов от 0.0.0.0 до 255.255.255.255.

Программа должна выводит верен или нет ip адрес.
"""
import re

if re.fullmatch(r'^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.'
                r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.'
                r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.'
                r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$',
                input('Введите IP адрес для проверки на корректность: ')):
    print('IP адрес корректный')
else:
    print('IP адрес некорректный')