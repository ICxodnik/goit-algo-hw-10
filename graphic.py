import matplotlib.pyplot as plt
import numpy as np

# Створюємо сітку значень
x_vals = np.linspace(0, 60, 400)
y_vals = np.linspace(0, 60, 400)
X, Y = np.meshgrid(x_vals, y_vals)

# Обмеження
water = 2 * X + Y <= 100
sugar = X <= 50
lemon_juice = X <= 30
fruit_puree = 2 * Y <= 40

# Об'єднання всіх обмежень
feasible_region = water & sugar & lemon_juice & fruit_puree

# Побудова графіка
plt.figure(figsize=(10, 8))
plt.contourf(X, Y, feasible_region, levels=[0, 1], colors=['#d0f0d0'], alpha=0.5)

# Побудова ліній обмежень
plt.plot(x_vals, 100 - 2 * x_vals, label='2x + y ≤ 100 (Вода)', color='blue')
plt.axvline(50, label='x ≤ 50 (Цукор)', color='orange')
plt.axvline(30, label='x ≤ 30 (Лимонний сік)', color='green')
plt.plot(x_vals, 20 * np.ones_like(x_vals), label='2y ≤ 40 (Фруктове пюре)', color='red')

# Оптимальна точка
opt_x = 30  # Лимонад
opt_y = 20  # Фруктовий сік
plt.plot(opt_x, opt_y, 'ko', label='Оптимальна точка (30, 20)', markersize=10)

# Підписи та легенда
plt.xlabel('Кількість Лимонаду (x)')
plt.ylabel('Кількість Фруктового соку (y)')
plt.title('Допустима область і оптимальне рішення')
plt.xlim(0, 60)
plt.ylim(0, 60)
plt.grid(True)
plt.legend()
plt.show()
