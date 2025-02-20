import pandas as pd
import time
import os
from sorting_algorithms import *

OUTPUT_DIR = "outputs/"

def run_sorting_test(dataset_file, algorithm):
    df = pd.read_csv(dataset_file)
    arr = df["values"].tolist()
    
    start_time = time.time()
    algorithm(arr)
    end_time = time.time()
    
    return end_time - start_time

def main():
    results = []
    for file in os.listdir(OUTPUT_DIR):
        if file.endswith(".csv"):
            parts = file[:-4].split("_")
            dataset_type = "_".join(parts[:-1])  # Join all but the last part as dataset type
            size = parts[-1]  # The last part should be the size
            size = int(size)  # Convert size to integer
            
            for algo_name, algo_func in [("Bubble Sort", bubble_sort), 
                                         ("Merge Sort", merge_sort), 
                                         ("Quick Sort", quick_sort)]:
                exec_time = run_sorting_test(os.path.join(OUTPUT_DIR, file), algo_func)
                results.append({"Dataset Type": dataset_type, "Size": size, 
                                "Algorithm": algo_name, "Time": exec_time})
    
    df_results = pd.DataFrame(results)
    df_results.to_csv(f"{OUTPUT_DIR}simulation_results.csv", index=False)

if __name__ == "__main__":
    main()