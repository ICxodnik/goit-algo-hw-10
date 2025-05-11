import numpy as np
from scipy.integrate import quad

# Параметри
a = 0
b = 2

# Функція для інтегрування
def f(x):
    return x**2

# Функція для обчислення інтегралу методом Монте-Карло
def monte_carlo_integral(func, a, b, N):
    x_rand = np.random.uniform(a, b, N)
    y_rand = func(x_rand)
    return (b - a) * np.mean(y_rand)

# Функція для перевірки коректності меж
def check_limits(a, b):
    if a >= b:
        raise ValueError("Нижня межа повинна бути меншою за верхню.")

if __name__ == "__main__":
    check_limits(a, b)

    # Обчислення точного значення інтегралу
    integral_true, error = quad(f, a, b)
    print(f"Інтеграл (Метод quad): {integral_true:.6f} (похибка: {error:.6e})\n")

    # Обчислення методом Монте-Карло з різною кількістю точок
    for N in [100, 1000, 10000, 100000, 1000000, 10000000]:
        integral_mc = monte_carlo_integral(f, a, b, N)
        abs_error = abs(integral_mc - integral_true)
        print(f"Кількість точок: {N}")
        print(f"Інтеграл (Метод Монте-Карло): {integral_mc:.6f}")
        print(f"Абсолютна похибка: {abs_error:.6f}\n")

