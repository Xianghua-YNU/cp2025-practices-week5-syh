import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial


def plot_poisson_pmf(lambda_param=8, max_l=20):
    try:
        l_values = np.arange(max_l)
        pmf = (lambda_param ** l_values * np.exp(-lambda_param)) / factorial(l_values)

        plt.figure(figsize=(10, 6))
        plt.plot(l_values, pmf, 'bo-', label='Theoretical Distribution')
        plt.title(f'Poisson Probability Mass Function (λ={lambda_param})')
        plt.xlabel('l')
        plt.ylabel('p(l)')
        plt.grid(True)
        plt.legend()
        return pmf
    except Exception as e:
        print(f"绘制泊松分布 PMF 时出错: {e}")


def simulate_coin_flips(n_experiments=10000, n_flips=100, p_head=0.08):
    try:
        results = []
        for _ in range(n_experiments):
            coins = np.random.choice([0, 1], n_flips, p=[1 - p_head, p_head])
            results.append(coins.sum())
        return np.array(results)
    except Exception as e:
        print(f"模拟抛硬币实验时出错: {e}")


def compare_simulation_theory(n_experiments=10000, lambda_param=8):
    try:
        results = simulate_coin_flips(n_experiments)

        max_l = max(int(lambda_param * 2), max(results) + 1)
        l_values = np.arange(max_l)
        pmf = (lambda_param ** l_values * np.exp(-lambda_param)) / factorial(l_values)

        plt.figure(figsize=(12, 7))
        plt.hist(results, bins=range(max_l + 1), density=True, alpha=0.7,
                 label='Simulation Results', color='skyblue')
        plt.plot(l_values, pmf, 'r-', label='Theoretical Distribution', linewidth=2)

        plt.title(f'Poisson Distribution Comparison (N={n_experiments}, λ={lambda_param})')
        plt.xlabel('Number of Heads')
        plt.ylabel('Frequency/Probability')
        plt.grid(True, alpha=0.3)
        plt.legend()

        print(f"实验均值: {np.mean(results):.2f} (理论值: {lambda_param})")
        print(f"实验方差: {np.var(results):.2f} (理论值: {lambda_param})")
    except Exception as e:
        print(f"比较实验结果与理论分布时出错: {e}")


if __name__ == "__main__":
    np.random.seed(42)
    plot_poisson_pmf()
    compare_simulation_theory()

    plt.show()
