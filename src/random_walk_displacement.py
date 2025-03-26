import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

def random_walk_displacement(num_steps, num_simulations):
    displacements = np.zeros((2, num_simulations))
    for i in range(num_simulations):
        x, y = 0, 0
        for _ in range(num_steps):
            dx = np.random.choice([-1, 1])
            dy = np.random.choice([-1, 1])
            x += dx
            y += dy
        displacements[0, i] = x
        displacements[1, i] = y
    return displacements

def plot_displacement_distribution(final_displacements, bins=30):
    displacements = np.sqrt(final_displacements[0]**2 + final_displacements[1]**2)
    plt.hist(displacements, bins=bins, density=True, alpha=0.7, color='b', label='Empirical')
    mean_square = np.mean(displacements**2)
    scale = np.sqrt(mean_square / 2)
    x = np.linspace(0, np.max(displacements), 100)
    pdf = (x / scale**2) * np.exp(-x**2 / (2 * scale**2))
    plt.plot(x, pdf, 'r-', label='Rayleigh Fit')
    plt.title('Random Walk Displacement Distribution')
    plt.xlabel('Final Displacement')
    plt.ylabel('Probability Density')
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_displacement_square_distribution(final_displacements, bins=30):
    displacements_square = final_displacements[0]**2 + final_displacements[1]**2
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.hist(displacements_square, bins=bins, density=True, alpha=0.7, color='b')
    plt.title('Random Walk Displacement Square Distribution (Linear)')
    plt.xlabel('Final Displacement Square')
    plt.ylabel('Probability Density')
    plt.grid(True)

    plt.subplot(1, 3, 2)
    plt.hist(displacements_square, bins=bins, density=True, alpha=0.7, color='b')
    plt.yscale('log')
    plt.title('Random Walk Displacement Square Distribution (Semi-Log)')
    plt.xlabel('Final Displacement Square')
    plt.ylabel('Log Probability Density')
    plt.grid(True)

    plt.subplot(1, 3, 3)
    plt.hist(displacements_square, bins=bins, density=True, alpha=0.7, color='b')
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Random Walk Displacement Square Distribution (Log-Log)')
    plt.xlabel('Log Final Displacement Square')
    plt.ylabel('Log Probability Density')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

    df = 2
    chi2_params = chi2.fit(displacements_square)
    x = np.linspace(np.min(displacements_square), np.max(displacements_square), 100)
    pdf = chi2.pdf(x, *chi2_params)
    plt.figure()
    plt.hist(displacements_square, bins=bins, density=True, alpha=0.7, color='b', label='Empirical')
    plt.plot(x, pdf, 'r-', label='Chi-Square Fit')
    plt.title('Random Walk Displacement Square Distribution with Chi-Square Fit')
    plt.xlabel('Final Displacement Square')
    plt.ylabel('Probability Density')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    num_steps = 1000
    num_simulations = 1000
    bins = 30

    displacements = random_walk_displacement(num_steps, num_simulations)

    plot_displacement_distribution(displacements, bins)
    plot_displacement_square_distribution(displacements, bins)
