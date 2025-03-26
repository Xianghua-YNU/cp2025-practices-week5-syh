import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

plt.rcParams['axes.unicode_minus'] = False


def generate_coin_sequence(n_flips, p_head=0.08):
    return np.random.choice([0, 1], size=n_flips, p=[1 - p_head, p_head])


def calculate_waiting_times(coin_sequence):
    head_indices = np.nonzero(coin_sequence)[0]

    waiting_times = np.diff(head_indices) - 1
    return waiting_times


def plot_waiting_time_histogram(waiting_times, log_scale=False, n_flips=None):
    plt.figure(figsize=(10, 6))

    max_wait = max(waiting_times) if len(waiting_times) > 0 else 0
    bins = np.arange(0, max_wait + 2) - 0.5

    plt.hist(waiting_times, bins=bins, density=True, alpha=0.7)
    plt.xlabel('等待时间（反面次数）')
    plt.ylabel('频率' if not log_scale else '频率（对数刻度）')

    if log_scale:
        plt.yscale('log')
        title = '等待时间分布（半对数刻度）'
    else:
        title = '等待时间分布'

    if n_flips is not None:
        title += f' - {n_flips:,} 次抛硬币'

    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.show()


def analyze_waiting_time(waiting_times):
    if len(waiting_times) == 0:
        return {"mean": None, "std": None, "theoretical_mean": None, "exponential_mean": None}

    mean_wait = np.mean(waiting_times)
    std_wait = np.std(waiting_times)

    p_head = 0.08  # 硬币正面概率
    theoretical_mean = (1 - p_head) / p_head

    exponential_mean = 1 / p_head  # 1/λ = 1/0.08 = 12.5

    return {
        "mean": mean_wait,
        "std": std_wait,
        "theoretical_mean": theoretical_mean,
        "exponential_mean": exponential_mean
    }


def run_experiment(n_flips, title):
    print(f"===== {title} =====")

    coin_sequence = generate_coin_sequence(n_flips)
    waiting_times = calculate_waiting_times(coin_sequence)

    stats = analyze_waiting_time(waiting_times)
    print(f"平均等待时间: {stats['mean']:.2f}")
    print(f"理论平均等待时间（几何分布）: {stats['theoretical_mean']:.2f}")
    print(f"理论平均等待时间（指数分布）: {stats['exponential_mean']:.2f}")

    plot_waiting_time_histogram(waiting_times, log_scale=False, n_flips=n_flips)
    plot_waiting_time_histogram(waiting_times, log_scale=True, n_flips=n_flips)

    return waiting_times, stats


if __name__ == "__main__":
    np.random.seed(42)

    waiting_times_1k, stats_1k = run_experiment(1000, "任务一：1000 次抛硬币")
    
    print("\n")
    waiting_times_1m, stats_1m = run_experiment(1000000, "任务二：1,000,000 次抛硬币")
