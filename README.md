# Elastic Collision Simulation

## Описание
Этот проект представляет собой симуляцию упругого столкновения двух тел с использованием библиотеки `tkinter` для создания графического интерфейса. Пользователь может настраивать параметры столкновения, такие как масса и скорость тел, а также размеры области симуляции.

## Используемые формулы и законы

1. **Закон сохранения импульса:**
   - m₁ * v₁_initial + m₂ * v₂_initial = m₁ * v₁_final + m₂ * v₂_final
     - где:
       - m₁, m₂ — массы тел,
       - v₁_initial, v₂_initial — начальные скорости тел,
       - v₁_final, v₂_final — конечные скорости тел после столкновения.

2. **Закон сохранения кинетической энергии:**
   - (1/2) * m₁ * v₁_initial² + (1/2) * m₂ * v₂_initial² = (1/2) * m₁ * v₁_final² + (1/2) * m₂ * v₂_final²

3. **Обработка столкновения:**
   - Для упругого столкновения используется формула импульса для вычисления новых скоростей тел:
     - v₁_final = v₁_initial - (2 * m₂ / (m₁ + m₂)) * v₁_initial
     - v₂_final = v₂_initial - (2 * m₁ / (m₁ + m₂)) * v₂_initial

4. **Проверка на столкновение:**
   - Проверка на столкновение между двумя телами основана на расстоянии между центрами тел:
     - d = √((x₁ - x₂)² + (y₁ - y₂)²)
       - где d — расстояние, (x₁, y₁) и (x₂, y₂) — координаты тел.
       - Столкновение происходит, если d меньше или равно сумме радиусов тел.

## Как использовать

1. **Запуск приложения:**
   - После скачивания и установки .exe файла запустите его двойным щелчком. Откроется графический интерфейс симуляции.

2. **Настройка параметров:**
   - Введите параметры столкновения:
     - **Масса тела 1:** Масса первого тела (по умолчанию 2.0)
     - **Масса тела 2:** Масса второго тела (по умолчанию 1.0)
     - **Скорость тела 1 (x, y):** Скорость первого тела по осям x и y (по умолчанию 2, 1)
     - **Скорость тела 2 (x, y):** Скорость второго тела по осям x и y (по умолчанию -2, -1)
     - **Размер области (ширина, высота):** Размер области симуляции (по умолчанию 500, 400)

3. **Запуск симуляции:**
   - После ввода всех необходимых параметров нажмите кнопку "Start Simulation" для запуска симуляции.
   - Вы можете управлять скоростью симуляции с помощью ползунка "Simulation Speed".

4. **Остановка симуляции:**
   - Чтобы остановить симуляцию, закройте приложение или нажмите соответствующую кнопку, если такая предусмотрена в интерфейсе.

## Требования
- Данная программа была разработана с использованием Python и библиотеки `tkinter`, которая обычно включена в стандартную библиотеку Python.
- Убедитесь, что у вас установлена актуальная версия Python.

## Видое
https://github.com/user-attachments/assets/1433f1da-96ac-4f6f-a06c-84c226c8bb23



