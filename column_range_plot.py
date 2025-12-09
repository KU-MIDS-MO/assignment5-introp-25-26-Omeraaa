import numpy as np
import matplotlib.pyplot as plt

def column_range_plot(A, filename="column_ranges.pdf"):
    num_rows, num_columns = A.shape
    ranges = []

    for i in range(num_columns):
        current_column = A[:, i]
        col_max = np.max(current_column)
        col_min = np.min(current_column)
        
        diff = col_max - col_min
        ranges.append(diff)

    ranges = np.array(ranges)

    x_positions = np.arange(num_columns)
    
    plt.figure()
    plt.bar(x_positions, ranges)
    plt.savefig(filename)
    plt.close()

    return ranges