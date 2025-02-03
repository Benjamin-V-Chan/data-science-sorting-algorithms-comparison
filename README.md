# data-science-sorting-algorithms-comparison

# Project Overview

This project is a statistical simulation that analyzes the efficiency of different sorting algorithms on various types of datasets. The analysis involves multiple mathematical techniques, including probability theory, statistical inference, and complexity analysis, to understand sorting efficiency under different conditions.

### **Mathematical Analysis of Sorting Algorithms**

Sorting algorithms have different worst-case, best-case, and average-case time complexities. Let’s formally define these complexities and prove some fundamental results.

#### **1. Time Complexity and Asymptotic Analysis**
Given an input list of size $\( n \)$, the time complexity $\( T(n) \)$ describes the number of fundamental operations performed by a sorting algorithm. The Big-O notation provides an upper bound on this complexity.

- **Bubble Sort:** Worst-case: $\( O(n^2) \)$, Best-case: $\( O(n) \)$, Average-case: $\( O(n^2) \)$
- **Merge Sort:** Worst-case: $\( O(n \log n) \)$, Best-case: $\( O(n \log n) \)$, Average-case: $\( O(n \log n) \)$
- **Quick Sort:** Worst-case: $\( O(n^2) \)$, Best-case: $\( O(n \log n) \)$, Average-case: $\( O(n \log n) \)$

For a divide-and-conquer algorithm like Merge Sort, we derive its time complexity using the recurrence relation:

$$T(n) = 2T\left(\frac{n}{2}\right) + O(n)$$

Applying the Master Theorem, where $\( a = 2 \)$, $\( b = 2 \)$, and $\( d = 1 \)$:

$$T(n) = O(n \log n)$$

For Quick Sort, the recurrence relation depends on pivot selection:

$$T(n) = T(k) + T(n-k-1) + O(n)$$

Assuming an even split, we get:

$$T(n) = 2T(n/2) + O(n)$$

Again, using the Master Theorem:

$$T(n) = O(n \log n)$$

In the worst case (poor pivot selection), Quick Sort behaves as:

$$T(n) = T(n-1) + O(n) = O(n^2)$$

#### **2. Statistical Analysis of Sorting Performance**
Each sorting algorithm’s execution time is measured over multiple trials. The results are modeled using a normal distribution:

$$X \sim \mathcal{N}(\mu, \sigma^2)$$

where $\( X \)$ represents execution time, $\( \mu \)$ is the mean execution time, and $\( \sigma^2 \)$ is the variance. The confidence interval for the mean is computed as:

$$CI = \mu \pm z \frac{\sigma}{\sqrt{n}}$$

where $\( z \)$ is the critical value from the standard normal distribution. Hypothesis testing is used to compare means across algorithms:

**Null Hypothesis (H₀):** There is no significant difference between two sorting algorithms.

**Alternative Hypothesis (H₁):** The performance difference is statistically significant.

Using a two-sample t-test:

$$t = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{S_1^2}{n_1} + \frac{S_2^2}{n_2}}}$$

where $\( S^2 \)$ represents sample variance. The p-value determines if we reject $\( H_0 \)$.

---

# Folder Structure

```
project-root/
├── scripts/
│   ├── 01_generate_datasets.py
│   ├── 03_run_simulations.py
│   ├── 04_analyze_results.py
│   ├── 05_visualize_results.py
│   └── sorting_algorithms.py
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
python scripts/02_run_simulations.py
```

### **4. Analyze Results**
Compute summary statistics of the sorting times:

```sh
python scripts/03_analyze_results.py
```

### **5. Visualize Results**
Generate visualizations of sorting performance:

```sh
python scripts/04_visualize_results.py
```

---

# Requirements

Ensure the following dependencies are installed:

```sh
pip install numpy pandas matplotlib
```

The project is designed for Python 3.7+.
