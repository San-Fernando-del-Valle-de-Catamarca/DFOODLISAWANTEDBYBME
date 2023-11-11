import tkinter as tk
import random


class Ball:
    def __init__(self, canvas, color, radius, power):
        self.canvas = canvas
        self.color = color
        self.power = power
        self.radius = radius
        self.x = random.randint(50, 450)
        self.y = random.randint(50, 350)
        self.dx = random.uniform(-1, 1) * self.power
        self.dy = random.uniform(-1, 1) * self.power
        self.ball = canvas.create_oval(self.x - self.radius, self.y - self.radius,
                                       self.x + self.radius, self.y + self.radius, fill=self.color)

    def move(self):
        self.canvas.move(self.ball, self.dx, self.dy)
        self.x += self.dx
        self.y += self.dy
        if self.x - self.radius <= 0 or self.x + self.radius >= 500:
            self.dx = -self.dx
        if self.y - self.radius <= 0 or self.y + self.radius >= 400:
            self.dy = -self.dy


class Simulation:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=500, height=400)
        self.canvas.pack()

        self.red_power_label = tk.Label(master, text="Red Ball Power:")
        self.red_power_label.pack()
        self.red_power_entry = tk.Entry(master)
        self.red_power_entry.pack()

        self.blue_power_label = tk.Label(master, text="Blue Ball Power:")
        self.blue_power_label.pack()
        self.blue_power_entry = tk.Entry(master)
        self.blue_power_entry.pack()

        self.start_button = tk.Button(master, text="Start Experiment", command=self.start_experiment)
        self.start_button.pack()

        self.red_power = 0
        self.blue_power = 0
        self.red_ball = None
        self.blue_ball = None

    def reset_experiment(self):
        if self.red_ball:
            self.canvas.delete(self.red_ball.ball)
        if self.blue_ball:
            self.canvas.delete(self.blue_ball.ball)

        self.red_power_entry.delete(0, tk.END)
        self.blue_power_entry.delete(0, tk.END)

        self.red_ball = None
        self.blue_ball = None

    def start_experiment(self):
        self.red_power = float(self.red_power_entry.get())
        self.blue_power = float(self.blue_power_entry.get())

        if self.red_ball:
            self.canvas.delete(self.red_ball.ball)
        if self.blue_ball:
            self.canvas.delete(self.blue_ball.ball)

        self.red_ball = Ball(self.canvas, 'red', 15, self.red_power)
        self.blue_ball = Ball(self.canvas, 'blue', 15, self.blue_power)
        self.animate()

    def animate(self):
        self.red_ball.move()
        self.blue_ball.move()
        self.master.after(10, self.animate)


if __name__ == "__main__":
    root = tk.Tk()
    simulation = Simulation(root)
    root.mainloop()