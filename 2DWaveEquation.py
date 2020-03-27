# coding=utf-8
from __future__ import  print_function
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
import warnings
warnings.filterwarnings('ignore')







if __name__ == '__main__':
    axis_size = 50
    side_length = 1
    dx, dy = side_length / axis_size, side_length / axis_size
    axis_points = np.linspace(0, side_length, axis_size)
    c = 1 / np.sqrt(2)

    # Set up the time grid
    T = 20
    dt = 0.5 * (1 / c) * (
                1 / np.sqrt(dx ** (-2) + dy ** (-2)))
    n = int(T / dt)


    def initial_cond(x, y):
        return np.sin(2 * np.pi * x + 2 * np.pi * y)


    X, Y = np.meshgrid(axis_points, axis_points)

    U = initial_cond(X, Y)

    B1 = U[:, 0]
    B2 = U[:, -1]
    B3 = U[0, :]
    B4 = U[-1, :]
    U1 = np.zeros((axis_size, axis_size))

    # Calculate the 2nd initial condition
    U1[1:-1, 1:-1] = (
                U[1:-1, 1:-1] + (c ** 2 / 2) * (dt ** 2 / dx ** 2) * (U[1:-1, 0:-2]
            - 2 * U[1:-1, 1:-1] + U[1:-1, 2:]) +
                (c ** 2 / 2) * (dt ** 2 / dy ** 2) * (U[0:-2, 1:-1]
            - 2 * U[1:-1, 1:-1] + U[2:, 1:-1]))

    # Reinforce the boundary conditions
    U1[:, 0] = B1
    U1[:, -1] = B2
    U1[0, :] = B3
    U1[-1, :] = B4

    # initial boundary conditions
    B5 = U1[:, 0]
    B6 = U1[:, -1]
    B7 = U1[0, :]
    B8 = U1[-1, :]
    U2 = np.zeros((axis_size, axis_size))

    map_array = np.zeros((axis_size, axis_size, n))
    # Initialize
    map_array[:, :, 0] = U
    map_array[:, :, 1] = U1

    # Numerically solve the PDE
    for i in range(2, n):
        U2[1:-1, 1:-1] = (2 * U1[1:-1, 1:-1] - U[1:-1, 1:-1] +
                          (c ** 2) * ((dt / dx) ** 2) * (U1[1:-1, 0:-2] - 2 * U1[1:-1, 1:-1]
        + U1[1:-1, 2:]) + (c ** 2) * ((dt / dy) ** 2) * (U1[0:-2, 1:-1] - 2 * U1[1:-1, 1:-1]
                                                 + U1[2:, 1:-1]))

        # Direchlet boundary conditions
        U2[:, 0] = B5
        U2[:, -1] = B6
        U2[0, :] = B7
        U2[-1, :] = B8
        U1[:, 0] = B5
        U1[:, -1] = B6
        U1[0, :] = B7
        U1[-1, :] = B8
        U[:, 0] = B1
        U[:, -1] = B2
        U[0, :] = B3
        U[-1, :] = B4
        map_array[:, :, i] = U2
        U = U1
        U1 = U2

    movie_frames = map_array[:, :, 0::40]
    fig = plt.figure(figsize=(640,480))

    # Create a 3D projection view
    ax = fig.gca(projection='3d')
    surf = (ax.plot_surface(X, Y, movie_frames[:, :, 0], rstride=2, cstride=2,
                            cmap='coolwarm', vmax=1, vmin=-1, linewidth=1))

    # Title of plot.
    ax.set_title('2D Sine Wave')

    # Add a colorbar to the plot.
    fig.colorbar(surf)
    ax.view_init(elev=30, azim=70)
    ax.dist = 8

    # Axis limits and labels.
    ax.set_xlim3d([0.0, 1.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([0.0, 1.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([-1.0, 1.0])
    ax.set_zlabel('Z')


    def animate(i):
        ax.clear()
        surf = (ax.plot_surface(X, Y, movie_frames[:, :, i], rstride=2, cstride=2,
                                cmap='coolwarm', vmax=1, vmin=-1, linewidth=1))
        ax.view_init(elev=30, azim=70)
        ax.dist = 8

        # Axis limits and labels.
        ax.set_xlim3d([0.0, 1.0])
        ax.set_xlabel('X')

        ax.set_ylim3d([0.0, 1.0])
        ax.set_ylabel('Y')

        ax.set_zlim3d([-1.0, 1.0])
        ax.set_zlabel('Z')
        ax.set_title('2D Sine Wave')
        return surf

    anim = animation.FuncAnimation(fig, animate, frames=movie_frames.shape[2])
    plt.show()
    plt.close(fig)


