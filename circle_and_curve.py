import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


class C(object):
    def __init__(self, radius, curve_x, curve_y, down=True):
        self.down = down
        self.r = radius

        self.number_of_points = 1000
        self.t = np.linspace(-4, 4, self.number_of_points)
        self.curve_x = self.load_curve(curve_x)
        self.curve_y = self.load_curve(curve_y)

        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal')

        self.animation = None

        # self.print_curve, = self.ax.plot(self.t, self.curve_y)

        ######
        self.print_curve, = self.ax.plot(self.curve_x, self.curve_y)
        #######
        # self.print_curve, = self.ax.plot([], 'b-')

        theta = np.linspace(0, 2 * np.pi, 360)
        start_x = self.r * np.sin(theta)
        start_y = self.r * np.cos(theta)

        a, b = self.straight_parameters(0)
        x, y = self.find_point(a,0)

        self.x_dot_data = []
        self.y_dot_data = []

        # self.dot, = self.ax.plot(self.t[0] + start_x[0] + x, self.curve_y[0] + start_y[0] - y, 'ko', ms=1)
        # self.circle, = self.ax.plot(self.t[0] + start_x + x, self.curve_y[0] + start_y - y, 'b-')
        ################
        self.dot, = self.ax.plot(self.curve_x[0] + start_x[0] + x, self.curve_y[0] + start_y[0] - y, 'ko', ms=1)
        self.circle, = self.ax.plot(self.curve_x[0] + start_x + x, self.curve_y[0] + start_y - y, 'b-')
        #######################

    def load_curve(self, curve):
        t = self.t
        return eval(curve)

    def straight_parameters(self, step):
        a = (self.curve_y[step + 1] - self.curve_y[step]) / (self.curve_x[step + 1] - self.curve_x[step])
        b = self.curve_y[step] - a * self.curve_x[step]

        return a, b

    def print_circle(self, x, y, step):
        theta = np.linspace(0, 2 * np.pi, 360)
        circle_x = x + self.r * np.sin(theta)
        circle_y = y + self.r * np.cos(theta)
        self.circle.set_data(circle_x, circle_y)

        #print(f"x: {circle_x[0]}  y: {circle_y[0]}\n")

        # if 0.03 < abs(circle_x[90]) and 0.04 < abs(circle_y[90]):
        self.print_dot(x, y, step)

    def print_dot(self, x, y, step):
        angle = np.radians(-3*step)
        #angle = np.arctan2(self.curve_y[step + 1] - self.curve_y[step] , self.curve_x[step + 1] - self.curve_x[step])
        dot_x = x + self.r * np.sin(angle)
        dot_y = y + self.r * np.cos(angle)

        self.x_dot_data.append(dot_x)
        self.y_dot_data.append(dot_y)

        self.dot.set_data(self.x_dot_data, self.y_dot_data)

    def find_point(self, a, step):
        #angle = np.arctan2(a, 1)
        angle = np.arctan2(self.curve_y[step + 1] - self.curve_y[step] , self.curve_x[step + 1] - self.curve_x[step])
        #print(np.degrees(angle))

        x = self.r * np.sin(angle)
        y = self.r * np.cos(angle)

        return x, y
    #
    # def angle(self, a):
    #     angle = np.arctan2(a,1)
    #     #print(np.degrees(angle))
    #
    #     return angle

    def running_circle(self):
        self.animation = FuncAnimation(self.fig, self.animate_circle, frames=self.number_of_points - 1, interval=1)

    def animate_circle(self, step):
        a, b = self.straight_parameters(step)
        #a2, b2 = self.straight_parameters(step + 1)

        if self.down:
            x, y = self.find_point(a,step)
            self.print_circle(self.curve_x[step] + x, self.curve_y[step] - y, step)
            # if self.angle(a) * self.angle(a2) > 0:
            #     self.print_circle(self.curve_x[step] + x, self.curve_y[step] - y, step)
            # else:
            #     self.print_circle(self.curve_x[step] - x, self.curve_y[step] + y, step)

        else:
            x, y = self.find_point(a,step)
            # self.print_dot(self.t[step] - x, self.curve[step] + y, step)
            # self.print_circle(self.t[step] - x, self.curve_y[step] + y, step)
            ######
            self.print_circle(self.curve_x[step] - x, self.curve_y[step] + y, step)
            ######
