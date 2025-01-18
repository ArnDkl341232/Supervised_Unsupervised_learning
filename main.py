'''
Проєкт "Аналіз спортивної команди"
Опис проєкту:
Проєкт допомагає зрозуміти, як тренування впливають на результати гри команди, а також розподілити гравців за їхніми здібностями, щоб оптимізувати тренувальний процес.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def main():
    # 1. Лінійна регресія: Прогноз очок у грі
    # Генеруємо дані.

    np.random.seed(42)

    training_hours = np.random.randint(1, 8, 30)
    game_points = 10 * training_hours + np.random.randint(0, 30, 30)

    data = {
        'Training Hours': training_hours,
        'Game Points': game_points,
    }

    df = pd.DataFrame(data)

    # Поділ даних.


    # Модель.


    # Візуалізація.


    # Прогноз.

    # 2. Кластеризація: Розподіл гравців за здібностями
    # Генеруємо дані.


    # Поділ даних.

    # Модель.

    # Візуалізація.


if __name__ == '__main__':
    main()