import numpy
from matplotlib import pyplot
import time, sys


def main():
    nx = 401
    dx = 2 / (nx - 1)
    nt = 25  # nt is the number of timesteps
    dt = 0.025  # dt is the amount of time each timestep
    c = 1
    u = numpy.ones(nx)
    u[int(0.15 / dx):int(1 / dx + 1)] = 6

    un = numpy.ones(nx)
    for n in range(nt):
        un = u.copy()
        for i in range(1, nx):
            u[i] = un[i] - c * dt / dx * (un[i] - un[i - 1])

    pyplot.plot(numpy.linspace(0, 2, nx), u)


if __name__ == "__main__":
    main()




