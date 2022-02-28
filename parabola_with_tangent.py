import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


class P(object):
    def __init__(self):
        self.a = -0.5
        self.number_of_points = 500
        self.t = np.linspace(-3, 3, self.number_of_points)

        self.parabola_y = self.a * self.t ** 2
        self.line_y = self.t

        self.fig, self.ax = plt.subplots()
        #self.ax.set_aspect('equal')

        self.animation = None

        self.line, = self.ax.plot(self.t, self.line_y)
        self.parabola, = self.ax.plot(self.t, self.parabola_y)

        #self.ran_dot = np.random.randint(1, self.number_of_points)
        self.ran_dot = 91
        self.x_dot_data = []
        self.y_dot_data = []
        self.dot, = self.ax.plot(self.t[self.ran_dot], self.parabola_y[self.ran_dot], 'ko', ms=2)

    def straight_parameters(self, step):
        a = (self.parabola_y[step + 1] - self.parabola_y[step]) / (self.t[step + 1] - self.t[step])
        b = self.parabola_y[step] - a * self.t[step]

        return a, b

    def create_straight(self, step, a, b, length=50):
        input_vector = np.linspace(self.t[step] - length / 2, self.t[step] + length / 2, self.number_of_points)
        values = a * input_vector
        values = values + b

        return input_vector, values

    def tangent_following_parabola(self):
        self.animation = FuncAnimation(self.fig, self.animate_tangent, frames=self.number_of_points - 1, interval=1)

    def parabola_following_tangent(self):
        self.animation = FuncAnimation(self.fig, self.animate_parabola,
                                       frames=np.arange(50, self.number_of_points - 50, 1),
                                       interval=1)

    def animate_parabola(self, step):
        a, b = self.straight_parameters(step)
        angle = np.arctan(a)

        x1_new = self.t * np.cos(angle) + self.parabola_y * np.sin(angle)
        y1_new = -self.t * np.sin(angle) + self.parabola_y * np.cos(angle)

        if self.a < 0:
            y1_new = y1_new - max(y1_new)
        else:
            y1_new = y1_new - min(y1_new)

        self.parabola.set_data(x1_new, y1_new)

        self.x_dot_data.append(x1_new[self.ran_dot])
        self.y_dot_data.append(y1_new[self.ran_dot])
        self.dot.set_data(self.x_dot_data, self.y_dot_data)

        self.line.set_data([-30, 30], [0, 0])

    def animate_tangent(self, step):
        a, b = self.straight_parameters(step)
        self.line.set_data(self.create_straight(step, a, b))

