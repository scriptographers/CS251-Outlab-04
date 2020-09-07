import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative as der

cut = 1000


def fn_plot1d(fn, x_min, x_max, filename):
    func = np.vectorize(fn, otypes=[float])
    x = np.linspace(x_min, x_max, num=cut, dtype=float)
    y = func(x)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Plot of the function')
    fig.savefig(filename)


def fn_plot2d(fn, x_min, x_max, y_min, y_max, filename):
    func = np.vectorize(fn, otypes=[float])
    x = np.linspace(x_min, x_max, num=cut, dtype=float)
    y = np.linspace(y_min, y_max, num=cut, dtype=float)
    xv, yv = np.meshgrid(x, y)
    z = func(xv, yv)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(xv, yv, z)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Surface plot of the function')
    fig.savefig(filename)


def nth_derivative_plotter(fn, n, xmin, xmax, filename):
    dx = (xmax - xmin) / (2 * cut)
    func = np.vectorize(lambda x: der(fn, x0=x, dx=dx, n=n, order=3))
    x = np.linspace(xmin, xmax, num=cut, dtype=float)
    y = func(x)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Plot of {}-derivative of the function'.format(n))
    fig.savefig(filename)


def h(x):
    if x > 0:
        return np.exp(-1 / x**2)
    else:
        return 0


def g(x):
    h2 = h(2 - x)
    h1 = h(x - 1)
    return h2 / (h2 + h1)


def b(x):
    if x >= 0:
        return g(x)
    else:
        return g(-x)


def sinc(x, y):
    sq = (x**2 + y**2)**0.5
    if sq > 0:
        return np.sin(sq) / sq
    else:
        return 1


fn_plot1d(b, -2, 2, 'fn1plot.png')
fn_plot2d(sinc, -1.5 * np.pi, 1.5 * np.pi, -1.5 * np.pi, 1.5 * np.pi, 'fn2plot.png')
nth_derivative_plotter(b, 1, -2, 2, 'bd_1.png')
nth_derivative_plotter(b, 2, -2, 2, 'bd_2.png')
