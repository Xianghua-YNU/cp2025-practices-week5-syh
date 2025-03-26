iimport matplotlib.pyplot as plt
import numpy as np


def random_walk_2d(steps):
    x_step = np.random.choice([-1, 1], steps)
    y_step = np.random.choice([-1, 1], steps)

    x_coords = np.cumsum(x_step)
    y_coords = np.cumsum(y_step)

    x_coords = np.insert(x_coords, 0, 0)
    y_coords = np.insert(y_coords, 0, 0)

    return x_coords, y_coords


def plot_single_walk(path):
    x_coords, y_coords = path

    plt.plot(x_coords, y_coords, marker='.')
    plt.scatter([x_coords[0]], [y_coords[0]], color='green', s=100, label='Start')
    plt.scatter([x_coords[-1]], [y_coords[-1]], color='red', s=100, label='End')
    plt.axis('equal')
    plt.legend()


def plot_multiple_walks():
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    axes = axes.ravel()

    for i in range(4):
        path = random_walk_2d(1000)
        x_coords, y_coords = path

        axes[i].plot(x_coords, y_coords, marker='.')
        axes[i].scatter([x_coords[0]], [y_coords[0]], color='green', s=100, label='Start')
        axes[i].scatter([x_coords[-1]], [y_coords[-1]], color='red', s=100, label='End')
        axes[i].axis('equal')
        axes[i].legend()
        axes[i].set_title(f'Trajectory {i + 1}')

    plt.tight_layout()


if __name__ == "__main__":
    plt.figure(figsize=(8, 8))
    path = random_walk_2d(1000)
    plot_single_walk(path)
    plt.title('Single Random Walk Trajectory')
    plt.show()

    plot_multiple_walks()
    plt.show()
