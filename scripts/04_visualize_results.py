import pandas as pd
import matplotlib.pyplot as plt
import os

RESULTS_FILE = "outputs/summary_statistics.csv"
OUTPUT_DIR = "outputs/"

def plot_results():
    df = pd.read_csv(RESULTS_FILE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    for dtype in df["Dataset Type"].unique():
        subset = df[df["Dataset Type"] == dtype]
        subset.plot(x="Algorithm", y=["mean", "median"], kind="bar", title=f"Sorting Times - {dtype}")
        plt.ylabel("Time (s)")
        plt.savefig(f"{OUTPUT_DIR}{dtype}_performance.png")
        plt.close()

if __name__ == "__main__":
    plot_results()