import numpy as np

# Функція для інтегрування
def f(x):
    return x**2

# Межі інтегрування
a = 0
b = 2

# Метод Монте-Карло
N = 100000  # Кількість випадкових точок
x_rand = np.random.uniform(a, b, N)
y_rand = f(x_rand)
integral_mc = (b - a) * np.mean(y_rand)


# Вивід результатів
print(f"Інтеграл (Монте-Карло): {integral_mc}")

