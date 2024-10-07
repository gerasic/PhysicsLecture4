import tkinter as tk
from tkinter import ttk
import math

class CollisionSimulation:
    def __init__(self, root):
        self.root = root
        self.root.title("Elastic Collision Simulation")

        # Инициализация параметров
        self.mass1 = 2.0
        self.mass2 = 1.0
        self.vel1 = [2, 1]
        self.vel2 = [-2, -1]
        self.shell_width = 500
        self.shell_height = 400
        self.simulation_speed = 1.0

        self.create_input_fields()
        self.create_canvas()

        self.running = False
        self.update_id = None

    def create_input_fields(self):
        # Поля ввода для параметров
        self.mass1_input = self.create_input_field("Mass of Body 1:", "2.0")
        self.mass2_input = self.create_input_field("Mass of Body 2:", "1.0")
        self.vel1_input = self.create_input_field("Velocity of Body 1 (x, y):", "2, 1")
        self.vel2_input = self.create_input_field("Velocity of Body 2 (x, y):", "-2, -1")
        self.shell_size_input = self.create_input_field("Shell Size (width, height):", "500, 400")

        # Поле ввода для контроля скорости симуляции
        speed_layout = tk.Frame(self.root)
        speed_label = tk.Label(speed_layout, text="Simulation Speed:")
        speed_label.pack(side=tk.LEFT)

        self.speed_input = ttk.Scale(speed_layout, from_=0.1, to=10.0, orient=tk.HORIZONTAL, command=self.update_speed)
        self.speed_input.set(1.0)  # Установка стандартного значения 1.0x
        self.speed_input.pack(side=tk.LEFT)

        self.speed_input_value = tk.Label(speed_layout, text="1.0")  # Для отображения текущего значения
        self.speed_input_value.pack(side=tk.LEFT)

        speed_layout.pack()

        # Кнопка старта
        self.start_button = tk.Button(self.root, text="Start Simulation", command=self.start_simulation)
        self.start_button.pack()

    def create_input_field(self, label_text, default_value):
        frame = tk.Frame(self.root)
        label = tk.Label(frame, text=label_text)
        label.pack(side=tk.LEFT)
        entry = tk.Entry(frame)
        entry.insert(0, default_value)
        entry.pack(side=tk.LEFT)
        frame.pack()
        return entry

    def create_canvas(self):
        self.canvas = tk.Canvas(self.root, width=self.shell_width, height=self.shell_height, bg="white")
        self.canvas.pack()

    def start_simulation(self):
        try:
            self.mass1 = float(self.mass1_input.get())
            self.mass2 = float(self.mass2_input.get())

            vel1_values = list(map(float, self.vel1_input.get().split(',')))
            if len(vel1_values) != 2:
                raise ValueError("Velocity of Body 1 must have two components.")
            self.vel1 = vel1_values

            vel2_values = list(map(float, self.vel2_input.get().split(',')))
            if len(vel2_values) != 2:
                raise ValueError("Velocity of Body 2 must have two components.")
            self.vel2 = vel2_values

            shell_size_values = list(map(int, self.shell_size_input.get().split(',')))
            if len(shell_size_values) != 2:
                raise ValueError("Shell size must have two components (width, height).")
            self.shell_width, self.shell_height = shell_size_values

            # Начальные координаты тел
            self.body1 = [100, 100]
            self.body2 = [300, 300]

            # Радиусы тел
            self.radius1 = 20
            self.radius2 = 30

            self.running = True
            self.update_simulation()
        except ValueError as e:
            self.root.title(f"Error: {e}")

    def update_speed(self, value):
        self.simulation_speed = float(value)
        self.speed_input_value.config(text=f"{self.simulation_speed:.1f}")  # Обновление метки

    def update_simulation(self):
        if not self.running:
            return

        self.handle_collisions()

        # Обновление координат тел с учетом коэффициента скорости
        self.body1[0] += self.vel1[0] * self.simulation_speed
        self.body1[1] += self.vel1[1] * self.simulation_speed
        self.body2[0] += self.vel2[0] * self.simulation_speed
        self.body2[1] += self.vel2[1] * self.simulation_speed

        self.update_view()

        # Установка таймера для обновления
        self.update_id = self.root.after(20, self.update_simulation)

    def handle_collisions(self):
        self.check_boundary_collision(self.body1, self.vel1, self.radius1)
        self.check_boundary_collision(self.body2, self.vel2, self.radius2)

        if self.check_body_collision():
            self.resolve_body_collision()

    def check_boundary_collision(self, body, velocity, radius):
        collided = False
        if body[0] - radius < 0:
            body[0] = radius
            velocity[0] = -velocity[0]
            collided = True
        elif body[0] + radius > self.shell_width:
            body[0] = self.shell_width - radius
            velocity[0] = -velocity[0]
            collided = True

        if body[1] - radius < 0:
            body[1] = radius
            velocity[1] = -velocity[1]
            collided = True
        elif body[1] + radius > self.shell_height:
            body[1] = self.shell_height - radius
            velocity[1] = -velocity[1]
            collided = True

        if collided:
            print(f"Collision detected with shell. New velocity: ({velocity[0]}, {velocity[1]})")

    def check_body_collision(self):
        dist = math.sqrt((self.body1[0] - self.body2[0]) ** 2 + (self.body1[1] - self.body2[1]) ** 2)
        return dist <= (self.radius1 + self.radius2)

    def resolve_body_collision(self):
        delta = [self.body1[0] - self.body2[0], self.body1[1] - self.body2[1]]
        distance = math.sqrt(delta[0] ** 2 + delta[1] ** 2)
        if distance == 0:
            distance = 0.1
            delta = [0.1, 0]

        normal = [delta[0] / distance, delta[1] / distance]

        relative_velocity = [self.vel1[0] - self.vel2[0], self.vel1[1] - self.vel2[1]]
        velocity_along_normal = relative_velocity[0] * normal[0] + relative_velocity[1] * normal[1]

        if velocity_along_normal > 0:
            return

        impulse = (2 * velocity_along_normal) / (self.mass1 + self.mass2)
        self.vel1[0] -= impulse * self.mass2 * normal[0]
        self.vel1[1] -= impulse * self.mass2 * normal[1]
        self.vel2[0] += impulse * self.mass1 * normal[0]
        self.vel2[1] += impulse * self.mass1 * normal[1]

        overlap = (self.radius1 + self.radius2) - distance
        if overlap > 0:
            correction = overlap / 2
            self.body1[0] += normal[0] * correction
            self.body1[1] += normal[1] * correction
            self.body2[0] -= normal[0] * correction
            self.body2[1] -= normal[1] * correction

        print(
            f"Collision resolved. New velocities:\nBody1: ({self.vel1[0]}, {self.vel1[1]})\nBody2: ({self.vel2[0]}, {self.vel2[1]})")

    def update_view(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, self.shell_width, self.shell_height, outline="black", fill="white")
        self.canvas.create_oval(
            self.body1[0] - self.radius1, self.body1[1] - self.radius1,
            self.body1[0] + self.radius1, self.body1[1] + self.radius1, fill="red"
        )
        self.canvas.create_oval(
            self.body2[0] - self.radius2, self.body2[1] - self.radius2,
            self.body2[0] + self.radius2, self.body2[1] + self.radius2, fill="blue"
        )

    def stop_simulation(self):
        self.running = False
        if self.update_id is not None:
            self.root.after_cancel(self.update_id)
            self.update_id = None

if __name__ == "__main__":
    root = tk.Tk()
    app = CollisionSimulation(root)
    root.mainloop()
