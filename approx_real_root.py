def approx_real_root(coeffs, interval):
    a = interval[0]
    b = interval[1]
    
    for i in range(1000):
        mid = (a + b) / 2.0
        
        val_mid = 0
        for k in range(len(coeffs)):
            val_mid = val_mid + coeffs[k] * (mid ** k)
            
        if abs(val_mid) < 0.000000001:
            return mid
            
        val_a = 0
        for k in range(len(coeffs)):
            val_a = val_a + coeffs[k] * (a ** k)
            
        if val_a * val_mid < 0:
            b = mid
        else:
            a = mid
            
    return mid