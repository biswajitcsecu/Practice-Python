
import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    return 2 * x + y

def main(a, b, c, d, nx, ny) :
    hx = (b - a) / nx
    hy = (d - c) / ny
    I = 0
    for i in range(nx):
        for j in range(ny):
            xi = a + hx / 2 + i * hx
            yj = c + hy / 2 + j * hy
            I = I + hx * hy * f(xi, yj)
    print(I)



if __name__ == "__main__":
    a = 0
    b = 2
    c = 2
    d = 3
    nx = 15
    ny = 25
    main(a,b,c,d,nx,ny)
