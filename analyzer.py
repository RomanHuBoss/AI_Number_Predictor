"""
Анализ среднего числа попыток угадывания компьютером числа в интервале от 1 до 100 с использованием дихотомии
"""

from random import sample
import numpy as np
import time 

class Analyzer:
    __min_limit = None
    __max_limit = None
    
    def __init__(self, min_limit = 1, max_limit = 101) -> None:
        """Конструктор класса-анализатора

        Args:       
            min_limit (int, optional): минимальное число в интервале
            max_limit (int, optional): максимальное число в интервале + 1

        Returns:
            None
        """        
        
        Analyzer.__min_limit = min_limit
        Analyzer.__max_limit = max_limit + 1
        

    def __predict(hidden_number) -> int:
        """Предсказание дихотомией

        Args:       
            hidden_number (int): Загаданное число

        Returns:
            int: число попыток угадывания конкретного числа
        """        
        min_limit = Analyzer.__min_limit
        max_limit = Analyzer.__max_limit
        num_tries = 0
        
        while (True):              
            num_tries += 1
            predicted_number = int((max_limit + min_limit)/2)
            
            if (predicted_number == hidden_number):
                return num_tries
            elif predicted_number > hidden_number:
                max_limit = predicted_number
            elif predicted_number < hidden_number:
               min_limit = predicted_number
                
    def collect_stat(self, sample_size = 20) -> int:        
        """За какое количество попыток в среднем алгоритм угадывает число в заданном интервале для выборки из случайных чисел размера sample_size

        Args:
            stat ([type]): функция угадывания

        Returns:
            int: среднее количество попыток
        """
 
        count_ls = []
                
        np.random.seed(int(time.time()))  # фиксируем сид для воспроизводимости    
        random_array = np.random.randint(Analyzer.__min_limit, Analyzer.__max_limit, sample_size)  # загадали список чисел

        for number in random_array:
            count_ls.append(Analyzer.__predict(number))

        return int(np.mean(count_ls))

