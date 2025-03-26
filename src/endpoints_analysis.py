import numpy as np
import matplotlib.pyplot as plt


def random_walk_finals(num_steps, num_walks):
    x_finals = np.zeros(num_walks)
    y_finals = np.zeros(num_walks)
    for i in range(num_walks):
        x_finals[i] = np.sum(np.random.choice([-1, 1], num_steps))
        y_finals[i] = np.sum(np.random.choice([-1, 1], num_steps))
    return (x_finals, y_finals)


def plot_endpoints_distribution(endpoints):
    x_coords, y_coords = endpoints
    plt.scatter(x_coords, y_coords, alpha=0.5)
    plt.axis('equal')
    plt.title('Endpoint Distribution Scatter Plot')
    plt.xlabel('X')
    plt.ylabel('Y')


def analyze_x_distribution(endpoints):
    x_coords = endpoints[0]

    mean = np.mean(x_coords)
    var = np.var(x_coords, ddof=1)

    plt.hist(x_coords, bins=50, density=True, alpha=0.7)

    x = np.linspace(min(x_coords), max(x_coords), 100)
    plt.plot(x, 1 / np.sqrt(2 * np.pi * var) * np.exp(-(x - mean) ** 2 / (2 * var)),
             'r-', label='Theoretical Normal Distribution')

    plt.title('X-Coordinate Distribution Histogram')
    plt.xlabel('X')
    plt.ylabel('Frequency')
    plt.legend()

    print(f"Sample mean of X-coordinates: {mean:.2f}")
    print(f"Sample variance of X-coordinates: {var:.2f}")
    return mean, var


def single_step_analysis():
    print("单步随机行走的概率分布：")
    print("在x和y方向上，移动+1或 - 1的概率均为0.5。")
    print("单步x和y坐标的期望值为 E(X) = E(Y) = 0。")
    print("单步x和y坐标的方差为 Var(X) = Var(Y) = 1。")


def central_limit_theorem_analysis(num_steps):
    print("\n中心极限定理分析：")
    print(f"经过{num_steps}步随机行走后，根据中心极限定理，终点的x和y坐标近似服从正态分布。")
    print("由于每一步的期望值为0，方差为1，且各步相互独立。")
    print(f"所以终点x和y坐标的期望值为 E(X_total) = E(Y_total) = 0 * {num_steps} = 0。")
    print(f"终点x和y坐标的方差为 Var(X_total) = Var(Y_total) = 1 * {num_steps} = {num_steps}。")


if __name__ == "__main__":
    np.random.seed(42)
    num_steps = 1000
    num_walks = 1000

    endpoints = random_walk_finals(num_steps, num_walks)

    plt.figure(figsize=(12, 5))

    plt.subplot(121)
    plot_endpoints_distribution(endpoints)

    plt.subplot(122)
    analyze_x_distribution(endpoints)

    plt.tight_layout()
    plt.show()

    single_step_analysis()
    central_limit_theorem_analysis(num_steps)
