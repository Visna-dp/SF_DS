"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Поиск числа идет путем сокращения диапозона поиска вдвое на
    каждом шаге. 
    Функция принимает загаданное число и возвращает число попыток.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # счетчик числа попыток
    first_number = 1 # начало диапазона поиска
    last_number = 100 # окончание диапазона поиска

    while True:
        count += 1
        # предполагаемое число
        predict_number = int(first_number + (last_number-first_number)/2)
        
        if number == predict_number:
            break # выход из цикла, если угадали
        
        if number > predict_number:
            first_number = predict_number + 1 # начало диапазона поиска
        elif number < predict_number:
            last_number = predict_number - 1 # окончание диапазона поиска
    
    return(count)

