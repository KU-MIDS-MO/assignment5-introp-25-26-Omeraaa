import numpy as np
import matplotlib.pyplot as plt

def detect_turning_points(signal, filename="turning_points.pdf"):
    turning_points = []

    for i in range(1, len(signal) - 1):
        prev_val = signal[i-1]
        curr_val = signal[i]
        next_val = signal[i+1]
        
        is_peak = (curr_val > prev_val) and (curr_val > next_val)
        is_valley = (curr_val < prev_val) and (curr_val < next_val)
        
        if is_peak or is_valley:
            turning_points.append(i)
            
    turning_points = np.array(turning_points)
    
    plt.figure()
    plt.plot(signal)
    plt.plot(turning_points, signal[turning_points], 'ro')
    plt.savefig(filename)
    plt.close()
    
    return turning_points