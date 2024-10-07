import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Параметры
mass1 = 1.0  # Масса тела 1
mass2 = 0.5  # Масса тела 2
v1 = np.array([2.0, 1.0])  # Начальная скорость тела 1 (vx, vy)
v2 = np.array([-1.0, -1.0])  # Начальная скорость тела 2 (vx, vy)
position1 = np.array([2.0, 2.0])  # Начальная позиция тела 1 (x, y)
position2 = np.array([5.0, 5.0])  # Начальная позиция тела 2 (x, y)
shell_width = 10.0  # Ширина оболочки
shell_height = 10.0  # Высота оболочки
dt = 0.05  # Шаг времени
frames = 300  # Количество кадров

# Функция для обновления позиций и скоростей
def update_positions(position1, position2, v1, v2):
    position1 += v1 * dt
    position2 += v2 * dt

    # Проверка на столкновения с оболочкой
    if position1[0] <= 0 or position1[0] >= shell_width:
        v1[0] = -v1[0]  # Развернуть скорость по оси x
    if position1[1] <= 0 or position1[1] >= shell_height:
        v1[1] = -v1[1]  # Развернуть скорость по оси y

    if position2[0] <= 0 or position2[0] >= shell_width:
        v2[0] = -v2[0]  # Развернуть скорость по оси x
    if position2[1] <= 0 or position2[1] >= shell_height:
        v2[1] = -v2[1]  # Развернуть скорость по оси y

    # Проверка на столкновения между телами
    dist = np.linalg.norm(position1 - position2)
    if dist < 1:  # Предполагая небольшую радиус для каждого тела
        # Рассчитать новые скорости после столкновения
        total_mass = mass1 + mass2
        new_v1 = (mass1 - mass2) / total_mass * v1 + (2 * mass2 / total_mass) * v2
        new_v2 = (2 * mass1 / total_mass) * v1 + (mass2 - mass1) / total_mass * v2
        return new_v1, new_v2
    return v1, v2

# Инициализация фигуры и оси
fig, ax = plt.subplots()
ax.set_xlim(0, shell_width)
ax.set_ylim(0, shell_height)
body1_plot, = ax.plot([], [], 'ro', markersize=80)  # Красный для тела 1
body2_plot, = ax.plot([], [], 'bo', markersize=10)  # Синий для тела 2

# Установка начальных позиций (исправлено для использования списков)
body1_plot.set_data([position1[0]], [position1[1]])
body2_plot.set_data([position2[0]], [position2[1]])

# Функция анимации
def animate(frame):
    global position1, position2, v1, v2
    v1, v2 = update_positions(position1, position2, v1, v2)
    body1_plot.set_data([position1[0]], [position1[1]])  # Использовать списки для одиночных значений
    body2_plot.set_data([position2[0]], [position2[1]])  # Использовать списки для одиночных значений
    return body1_plot, body2_plot

# Создание анимации
ani = FuncAnimation(fig, animate, frames=frames, interval=dt*1000)

# Отображение графика
plt.title('Упругое столкновение двух тел в прямоугольной оболочке')
plt.xlabel('Ширина')
plt.ylabel('Высота')
plt.grid()
plt.show()
