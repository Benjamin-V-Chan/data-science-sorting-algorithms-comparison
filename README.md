# data-science-sorting-algorithms-comparison

# Project Overview

This project is a statistical simulation that analyzes the efficiency of different sorting algorithms on various types of datasets. The analysis involves multiple mathematical techniques, including probability theory, statistical inference, and complexity analysis, to understand sorting efficiency under different conditions.

# Folder Structure

```
project-root/
├── scripts/
│   ├── 01_generate_datasets.py
│   ├── 02_sorting_algorithms.py
│   ├── 03_run_simulations.py
│   ├── 04_analyze_results.py
│   └── 05_visualize_results.py
├── outputs/
│   ├── simulation_results.csv
│   ├── summary_statistics.csv
│   ├── *.png
├── requirements.txt
├── README.md
```

---

# Usage

### **1. Setup the Project:**
Clone the repository. Ensure you have Python installed. Install required dependencies using the `requirements.txt` file:

```sh
pip install -r requirements.txt
```

### **2. Generate Datasets**
Run the following command to generate datasets of different types and sizes:

```sh
python scripts/01_generate_datasets.py
```

### **3. Run Sorting Algorithms and Simulations**
Run the sorting algorithms on the generated datasets and record execution times:

```sh
python scripts/03_run_simulations.py
```

### **4. Analyze Results**
Compute summary statistics of the sorting times:

```sh
python scripts/04_analyze_results.py
```

### **5. Visualize Results**
Generate visualizations of sorting performance:

```sh
python scripts/05_visualize_results.py
```

---

# Requirements

Ensure the following dependencies are installed:

```sh
pip install numpy pandas matplotlib
```

The project is designed for Python 3.7+.