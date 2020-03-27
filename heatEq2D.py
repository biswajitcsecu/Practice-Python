# coding=utf-8

from __future__ import  print_function, division
import numpy as np
import sympy as sp
import pylab as plt
from matplotlib.pylab import*
from mpl_toolkits.axes_grid1 import make_axes_locatable
import pylbm
import warnings
warnings.filterwarnings('ignore')


def main():
    try:
        def solution(x, y, t):
            return np.sin(np.pi * x**2) * np.sin(np.pi * y**2) * np.exp(-2 * np.pi ** 2 * mu * t)

        # parameters
        xmin, xmax, ymin, ymax = 0., 2., 0., 2.
        N = 256
        mu = 1.
        Tf = .1
        dx = (xmax-xmin)/N # spatial step
        la = 1./dx
        s1 = 2./(1+4*mu)
        s2 = 1.
        k, l = 1, 1 # number of the wave

        u, X, Y, LA = sp.symbols('u, X, Y, LA')

        def solution(x, y, t, k, l):
            return np.sin(k*np.pi*x)*np.sin(l*np.pi*y)*np.exp(-(k**2+l**2)*np.pi**2*mu*t)

        def plot(i, j, z, title):
            im = axarr[i,j].imshow(z)
            divider = make_axes_locatable(axarr[i, j])
            cax = divider.append_axes("right", size="20%", pad=0.05)
            cbar = plt.colorbar(im, cax=cax, format='%6.0e')
            axarr[i, j].xaxis.set_visible(False)
            axarr[i, j].yaxis.set_visible(False)
            axarr[i, j].set_title(title)



        dico = {
            'box': {'x':[xmin, xmax],
                    'y':[ymin, ymax],
                    'label': 0},
            'space_step': dx,
            'scheme_velocity': la,
            'schemes':[
                {
                    'velocities': list(range(5)),
                    'conserved_moments': u,
                    'polynomials': [1, X/LA, Y/LA, (X**2+Y**2)/(2*LA**2), (X**2-Y**2)/(2*LA**2)],
                    'equilibrium': [u, 0., 0., .5*u, 0.],
                    'relaxation_parameters': [0., s1, s1, s2, s2],
                }
            ],
            'init': {u: (solution, (0., k, l))},
            'boundary_conditions': {
                0: {'method': {0: pylbm.bc.AntiBounceBack,}},
            },
            'generator': 'cython',
            'parameters': {LA: la},
        }

        sol = pylbm.Simulation(dico)
        x = sol.domain.x
        y = sol.domain.y



        f, axarr = plt.subplots(2, 2)
        f.suptitle('Heat equation', fontsize=20)

        plot(0, 0, sol.m[u].copy(), 'initial')

        while sol.t < Tf:
            sol.one_time_step()

        sol.f2m()
        z = sol.m[u]
        ze = solution(x[:, np.newaxis], y[np.newaxis, :], sol.t, k, l)
        plot(1, 0, z, 'final')
        plot(0, 1, ze, 'exact')
        plot(1, 1, z-ze, 'error')
        plt.show()
        plt.grid(True)
        plt.close(f)



    finally:
        print("Error found")
        pass





if __name__ == "__main__":
    main()




