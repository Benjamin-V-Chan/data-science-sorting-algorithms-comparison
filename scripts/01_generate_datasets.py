import numpy as np
import pandas as pd
import os

OUTPUT_DIR = "outputs/"

def generate_dataset(size, dataset_type):
    """Generate dataset based on the type."""
    if dataset_type == "random":
        return np.random.randint(0, 10000, size).tolist()
    elif dataset_type == "sorted":
        return list(range(size))
    elif dataset_type == "reversed":
        return list(range(size, 0, -1))
    elif dataset_type == "nearly_sorted":
        data = list(range(size))
        swap_count = size // 10
        for _ in range(swap_count):
            i, j = np.random.randint(0, size, 2)
            data[i], data[j] = data[j], data[i]
        return data

def save_dataset(size, dataset_type):
    """Generate and save dataset as CSV."""
    data = generate_dataset(size, dataset_type)
    df = pd.DataFrame({"values": data})
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df.to_csv(f"{OUTPUT_DIR}{dataset_type}_{size}.csv", index=False)

if __name__ == "__main__":
    for size in [10, 50, 100, 500]:
        for dtype in ["random", "sorted", "reversed", "nearly_sorted"]:
            save_dataset(size, dtype)