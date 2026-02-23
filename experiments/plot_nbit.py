# experiments/plot_nbit.py

import sys
import matplotlib.pyplot as plt
from run_nbit import run_experiment

def plot(key_size, iterations):
    counts = run_experiment(key_size, iterations)

    plt.figure(figsize=(7, 4))
    plt.bar(counts.keys(), counts.values())
    plt.xlabel("Recovered Key")
    plt.ylabel("Counts")
    plt.title(f"Grover Key Recovery ({key_size}-bit)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    filename = f"results/hist_{key_size}bit.png"
    plt.savefig(filename)
    plt.show()
    print(f"Saved {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python plot_nbit.py <key_size> <iterations>")
        sys.exit(1)

    plot(int(sys.argv[1]), int(sys.argv[2]))
