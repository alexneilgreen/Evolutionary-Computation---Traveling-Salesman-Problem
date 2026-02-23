"""This file contains the logging and plotting functions"""

# Standard libraries or third-party packages
import os
import csv
import matplotlib
import matplotlib.pyplot as plt

LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log.txt")
log_file = open(LOG_PATH, "w")

# Logging function
def log(message):
    print(message, end="")
    log_file.write(message)
    log_file.flush()

# Save final results to csv
def save_tour_csv(tour, cities, distance, filename = "best_tour.csv"):
    path = os.path.join(filename)
    with open(path, "w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["Order", "City"])
        for order, idx in enumerate(tour, start=1):
            writer.writerow([order, cities[idx]])
        writer.writerow([])
        writer.writerow(["Total Distance (miles)", f"{distance:.4f}"])

# PLot Fitness over Generations
def plot_fitness(best_per_gen, filename="fitness_over_generations.png"):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(best_per_gen, linewidth=2)
    ax.set_xlabel("Generation")
    ax.set_ylabel("Tour Distance (miles)")
    ax.set_title("Best Tour Distance Per Generation")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)