import numpy as np
import matplotlib.pyplot as plt

def random_walk_finals(num_steps=1000, num_walks=1000):
    x_finals = np.zeros(num_walks)
    y_finals = np.zeros(num_walks)
    for i in range(num_walks):
        x_finals[i] = np.sum(np.random.choice([-1,1],num_steps))
        y_finals[i] = np.sum(np.random.choice([-1,1],num_steps))
    return (x_finals,y_finals)


def calculate_mean_square_displacement():
    steps = np.array([1000, 2000, 3000, 4000])
    msd = []
    
    for i in steps:
        x_finals, y_finals = random_walk_finals(num_steps=i)  # Fixed function name
        ds = x_finals**2 + y_finals**2
        msd.append(np.mean(ds))
    
    return steps, np.array(msd)

def analyze_step_dependence():
    steps, msd = calculate_mean_square_displacement()
    msd = np.array(msd)
    
    k = np.sum(steps * msd) / np.sum(steps**2)
    
    return steps, msd, k

if __name__ == "__main__":
    steps, msd, k = analyze_step_dependence()
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(steps, msd, 'ro', ms=10, label='Experimental Data')
    plt.plot(steps, k*steps, 'g--', label=f'Fitted: $r^2={k:.2f}N$', lw=2)
    plt.plot(steps, 2*steps, 'b-', label='Theory: $r^2=2N$', lw=2)
    
    plt.xlabel('Number of Steps $N$', fontsize=14)
    plt.ylabel('Mean Square Displacement $\\langle r^2 \\rangle$', fontsize=14)
    plt.title('Relationship between Steps and Mean Square Displacement', fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=12, loc='best')
    
    print("步数和对应的均方位移：")
    for n, m in zip(steps, msd):
        print(f"步数: {n:5d}, 均方位移: {m:.2f}")
    
    print(f"\n拟合结果：r² = {k:.4f}N")
    print(f"与理论值k=2的相对误差: {abs(k-2)/2*100:.2f}%")
    
    plt.show()
