# Blocked Matrix Multiplication with Performance Analysis

This Python program implements blocked matrix multiplication and analyzes its performance for different matrix and block sizes.

## Features

- Performs matrix multiplication using blocking for improved cache utilization.
- Generates random matrices of various sizes.
- Measures and records the time taken for multiplication with different block sizes.
- Generates plots to visualize the relationship between blocking size and execution time.

## Getting Started

### Prerequisites

This code requires the following Python libraries:
- NumPy (numpy)
- Matplotlib (matplotlib.pyplot)


### Run the script

Navigate to the project directory and execute the script using `python main.py`.

## Understanding the Code

- `blocked_matrix_multiply.py`: This file defines the function for blocked matrix multiplication using blocking techniques.
- `main.py`: This file is the main entry point for the program. It sets up the experiment parameters, runs the multiplication with different block sizes, records the time taken, and generates plots for analysis.

## Benefits of Blocking

The program utilizes blocking, which improves the performance of matrix multiplication by optimizing memory access patterns. Here's how blocking helps:

- **Cache Utilization**: Modern CPUs have a small but very fast internal memory called cache. Blocking breaks down large matrices into smaller sub-matrices (blocks) that are more likely to fit entirely in the cache. This reduces the need to constantly swap data between the slower main memory and the faster cache, significantly improving performance.

- **Reduced Memory Pressure**: While blocking doesn't directly reduce memory usage, it can help alleviate memory pressure during matrix multiplication. By processing smaller blocks at a time, the overall memory footprint might be lower compared to working with the entire matrices at once. This becomes more relevant when dealing with very large matrices.

## Analysis of Results

The generated plots will show the time taken for matrix multiplication (on the y-axis) for different block sizes (on the x-axis) for various matrix sizes (represented by different lines). We expect to see a U-shaped curve for each matrix size:

- Initially, the time taken might decrease as the block size increases due to better cache utilization.
- However, if the block size becomes too large, the time taken will increase due to increased data movement between memory and cache when blocks become too large to fit in the cache entirely.

The "sweet spot" block size for each matrix size can be identified from the plot where the time taken is minimal. This represents the optimal balance between cache utilization and the overhead of managing smaller blocks.

## Further Enhancements

- This code can be extended to include a wider range of block sizes for testing.
- You can explore different blocking algorithms and compare their performance.
- The code could be optimized to handle non-square matrices or incorporate parallelization techniques.