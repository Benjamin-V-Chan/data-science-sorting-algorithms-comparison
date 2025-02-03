import pandas as pd

RESULTS_FILE = "outputs/simulation_results.csv"

def analyze_results():
    df = pd.read_csv(RESULTS_FILE)
    
    summary = df.groupby(["Dataset Type", "Algorithm"])["Time"].agg(["mean", "median", "std"])
    summary.to_csv("outputs/summary_statistics.csv")

if __name__ == "__main__":
    analyze_results()