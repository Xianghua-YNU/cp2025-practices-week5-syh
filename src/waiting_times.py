import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

plt.rcParams['axes.unicode_minus'] = False

def generate_coin_tosses(n, p):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("抛硬币的次数 n 必须为正整数。")
    if not (0 <= p <= 1):
        raise ValueError("正面朝上的概率 p 必须在 0 到 1 之间。")
    return np.random.choice([0, 1], size=n, p=[1 - p, p])


def calculate_waiting_times(tosses):
    heads_indices = np.nonzero(tosses)[0]
    if len(heads_indices) < 2:
        return np.array([])
    return np.diff(heads_indices).flatten()


def plot_histograms(waiting_times, title):
    if len(waiting_times) == 0:
        print(f"{title} 中没有足够的正面出现以计算等待时间，无法绘制直方图。")
        return
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.hist(waiting_times, bins=20, edgecolor='k')
    plt.title(f'{title} - 等待时间直方图')
    plt.xlabel('等待时间')
    plt.ylabel('频数')

    plt.subplot(1, 2, 2)
    plt.hist(waiting_times, bins=20, edgecolor='k', log=True)
    plt.title(f'{title} - 半对数坐标等待时间直方图')
    plt.xlabel('等待时间')
    plt.ylabel('频数 (对数坐标)')

    plt.tight_layout()
    plt.show()


def run_experiment(n, p, title):
    try:
        tosses = generate_coin_tosses(n, p)
        waiting_times = calculate_waiting_times(tosses)
        plot_histograms(waiting_times, title)

        if len(waiting_times) > 0:
            average_waiting_time = np.mean(waiting_times)
            theoretical_waiting_time = 1 / p
            print(f'{title} - 平均等待时间: {average_waiting_time}')
            print(f'{title} - 理论等待时间: {theoretical_waiting_time}')
        else:
            print(f"{title} 中没有足够的正面出现以计算等待时间。")
    except ValueError as e:
        print(f"实验 {title} 出错: {e}")

run_experiment(1000, 0.08, '基础实验（1000 次抛掷）')

run_experiment(1000000, 0.08, '大样本实验（1000000 次抛掷）')
