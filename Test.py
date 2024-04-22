import Blocking
import numpy as np
import time
import matplotlib.pyplot as plt


def matrix_multiplication(matrix_size, block_size):
    # Initialize matrices
    matrix1 = np.random.rand(matrix_size, matrix_size)
    matrix2 = np.random.rand(matrix_size, matrix_size)
    result = np.zeros((matrix_size, matrix_size))

    # Perform matrix multiplication using blocking
    for i in range(0, matrix_size, block_size):
        for j in range(0, matrix_size, block_size):
            for k in range(0, matrix_size, block_size):
                # Perform block multiplication
                block1 = matrix1[i:i+block_size, k:k+block_size]
                block2 = matrix2[k:k+block_size, j:j+block_size]
                block_result = np.dot(block1, block2)
                
                # Update result matrix
                result[i:i+block_size, j:j+block_size] += block_result
    
    return result

# Define matrix sizes and block sizes to test
matrix_sizes = [100, 200, 300, 400, 500]
block_sizes = [10, 20, 30, 40, 50 ,60,70]

times = {size: [] for size in matrix_sizes}

for matrix_size in matrix_sizes:
    for block_size in block_sizes:
        start_time = time.time()
        result = matrix_multiplication(matrix_size, block_size)
        end_time = time.time()
        times[matrix_size].append(end_time - start_time)
        
for matrix_size, time_list in times.items():
    plt.plot(block_sizes, time_list, label=f'Matrix size {matrix_size}')
plt.xlabel('Block size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()




# Relation between Block Size and Performance:

# Small Blocking Size:
# If the blocking size is too small,
# the computer has to manage many small blocks of data
# This can slow down the multiplication process
# because the computer spends alot of time just to manage the blocks

# Large Blocking Size:
# if the blocking size is too large,
# the blocks are too big, this can slow down the multiplication process
# because the computer has to move data in and out of memory due to cache misses

# Sweet Spots:
# There's usually a "sweet spot" block size for each matrix size. 
# This is the block size where the time taken for multiplication is minimal.
# It represents a balance between cache utilization and the overhead of managing smaller blocks.