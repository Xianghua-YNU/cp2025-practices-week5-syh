import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

plt.rcParams['font.sans-serif'] = ['SimHei']

plt.rcParams['axes.unicode_minus'] = False


def random_walk_2d(steps):
    x_step = np.random.choice([-1, 1], steps)
    y_step = np.random.choice([-1, 1], steps)
    x = x_step.cumsum()
    y = y_step.cumsum()
    r_squared = x ** 2 + y ** 2
    return r_squared, (x, y)


def plot_single_walk(path):
    x_coords, y_coords = path
    plt.plot(x_coords, y_coords, marker='.')
    plt.scatter([x_coords[0]], [y_coords[0]], color='green', s=100, label='起点')
    plt.scatter([x_coords[-1]], [y_coords[-1]], color='red', s=100, label='终点')
    plt.axis('equal')
    plt.legend()


def plot_multiple_walks():
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    axes = axes.ravel()

    for i in range(4):
        _, path = random_walk_2d(1000)
        x_coords, y_coords = path

        axes[i].plot(x_coords, y_coords, marker='.')
        axes[i].scatter([x_coords[0]], [y_coords[0]], color='green', s=100, label='起点')
        axes[i].scatter([x_coords[-1]], [y_coords[-1]], color='red', s=100, label='终点')
        axes[i].axis('equal')
        axes[i].legend()
        axes[i].set_title(f'轨迹 {i + 1}')

    plt.tight_layout()

num_simulations = 1000
steps = 1000
all_r_squared = []
for _ in range(num_simulations):
    r_squared, _ = random_walk_2d(steps)
    all_r_squared.append(r_squared)


msd = np.mean(all_r_squared, axis=0)

step_counts = [1000, 2000, 3000, 4000]
msd_values = []
for step in step_counts:
    all_r_squared = []
    for _ in range(num_simulations):
        r_squared, _ = random_walk_2d(step)
        all_r_squared.append(r_squared)
    msd = np.mean(all_r_squared, axis=0)[-1]
    msd_values.append(msd)

plt.figure(figsize=(10, 6))
plt.plot(step_counts, msd_values, 'o-')
plt.xlabel('步数')
plt.ylabel('均方位移')
plt.title('均方位移与步数的关系')
plt.grid(True)

slope, intercept, r_value, p_value, std_err = linregress(step_counts, msd_values)
print(f"均方位移与步数的定量关系：均方位移 = {slope:.2f} * 步数 + {intercept:.2f}")
print(f"拟合的相关系数 r = {r_value:.2f}")

plt.show()

plt.figure(figsize=(8, 8))
_, path = random_walk_2d(1000)
plot_single_walk(path)
plt.title('单条随机游走轨迹')
plt.show()

plot_multiple_walks()
plt.show()
