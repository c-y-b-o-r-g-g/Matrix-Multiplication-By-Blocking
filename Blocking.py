import numpy as np

def matrix_multiplication(matrix_size, block_size):
    # Generate random matrices
    matrix1 = np.random.rand(matrix_size, matrix_size)
    matrix2 = np.random.rand(matrix_size, matrix_size)
    
    # Initialize result matrix
    result = np.zeros((matrix_size, matrix_size))
    
    # Perform matrix multiplication using blocking
    for i in range(0, matrix_size, block_size):
        for j in range(0, matrix_size, block_size):
            for k in range(0, matrix_size, block_size):
                # Perform block multiplication
                # Select the current block from matrix1 and matrix2
                block1 = matrix1[i:i+block_size, k:k+block_size]
                block2 = matrix2[k:k+block_size, j:j+block_size]
                
                # Perform matrix multiplication of the selected blocks
                block_result = np.dot(block1, block2)
                
                # Update the result matrix with the computed block result
                result[i:i+block_size, j:j+block_size] += block_result
    
    return result
