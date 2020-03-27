
from __future__ import print_function
import sys, os
import  numpy as np
import random as rd
import matplotlib.pyplot as plt
import math
import cmath
plt.style.use('ggplot')



def main ():
    x = []
    y = []
    N = 250
    for i in range (N):
        y.append(rd.random()/np.sinc(i))
        x.append(i)

    x = np.array(x)
    y = np.sin(np.array(y))
    print(("X=%d:", x), end='')
    print(("Y=%f:", y), end='')

    fig = plt.figure(figsize=(10,4), dpi = 125)
    ax = fig.gca()
    plt.axis("on")
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    plt.plot(x, y, c='r', ls='-', lw=1)
    plt.grid(True)
    plt.title("Random Time Series")
    plt.show()
    plt.close(fig)


if __name__ == "__main__" :
    main()