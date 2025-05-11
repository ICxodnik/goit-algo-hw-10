import numpy as np
import matplotlib.pyplot as plt
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

# Обчислення точного значення інтегралу
integral_true, _ = quad(f, a, b)

# Масиви для збереження результатів
Ns = [100, 1000, 10000, 100000]
trial_counts = [1, 10, 100, 1000]

results = {}

# Обчислення усереднених інтегралів методом Монте-Карло
for trials in trial_counts:
    errors = []
    for N in Ns:
        integral_sum = 0
        for _ in range(trials):
            integral_sum += monte_carlo_integral(f, a, b, N)
        integral_avg = integral_sum / trials
        abs_error = abs(integral_avg - integral_true)
        errors.append(abs_error)
    results[trials] = errors

# Побудова графіка
plt.figure(figsize=(10, 6))
for trials, errors in results.items():
    plt.plot(Ns, errors, marker='o', label=f'{trials} спроб')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Кількість точок N (лог. шкала)')
plt.ylabel('Абсолютна похибка (лог. шкала)')
plt.title('Залежність похибки Монте-Карло від N і кількості спроб')
plt.legend()
plt.grid(True, which="both", ls="--", lw=0.5)
plt.tight_layout()
plt.show()
