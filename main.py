'''
Проєкт "Аналіз спортивної команди"
Опис проєкту:
Проєкт допомагає зрозуміти, як тренування впливають на результати гри команди, а також розподілити гравців за їхніми здібностями, щоб оптимізувати тренувальний процес.
'''
from random import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


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
    X = df[["Training Hours"]]
    y = df["Game Points"]
    X_train,  X_test, y_train,y_test = train_test_split(X, y, train_size=0.8,random_state=42)


    # Модель.
    model = LinearRegression()
    model.fit(X_train, y_train)
    Y_pred = model.predict(X_test)

    # Візуалізація.
    plt.scatter(X, y, color="blue", label="Data")
    plt.plot(X_test, Y_pred, color="red", label="Prediction")
    plt.title("Finale Points Amount")
    plt.xlabel("Training Hours")
    plt.ylabel("Game Points")
    plt.legend()
    plt.show()

    # Прогноз.

    # 2. Кластеризація: Розподіл гравців за здібностями
    # Генеруємо дані.


    # Поділ даних.

    # Модель.

    # Візуалізація.


if __name__ == '__main__':
    main()