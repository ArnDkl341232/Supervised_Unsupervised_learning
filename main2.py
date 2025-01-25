import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def main():
    #1. Лінійна регресія: Прогноз доходу кафе
    # Генеруємо дані.

    np.random.seed(42)

    visitors = np.random.randint(1,30, 100)
    revenue = 10 * visitors + np.random.randint(0, 1500, 100)

    data = {
        'Visitors': visitors,
        'Revenue': revenue,
    }

    df = pd.DataFrame(data)

    # Поділ даних.

    X = df[["Visitors"]]
    Y = df["Revenue"]

    # Модель.
    model = LinearRegression()
    model.fit(X, Y)

    print("Weight (W):", model.coef_)
    print("bias (b):", model.intercept_)

    # Візуалізація.
    plt.scatter(df["Visitors"], df["Revenue"], color="blue")
    plt.title("Дохід кафе")
    plt.xlabel("Visitors")
    plt.ylabel("Revenue")
    plt.show()


    # Прогноз.
    Y_pred = model.predict(X)

    plt.scatter(X, Y, color="blue")
    plt.plot(X, Y_pred, color="red")
    plt.title("Regretion line")
    plt.xlabel("Days")
    plt.ylabel("Candies")
    plt.show()

    # new_value = [[1000]]
    # predicted_revenue = model.predict(new_value)
    # print(f"Prediction for {new_value[0][0]}:", predicted_revenue[[0]])

    # 2. Кластеризація: Розподіл гравців за здібностями
    # Генеруємо дані.


    # Поділ даних.

    # Модель.

    # Візуалізація.


if __name__ == '__main__':
    main()