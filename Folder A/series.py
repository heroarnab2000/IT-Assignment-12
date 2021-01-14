import math

def division(x, y):
    if y <= x:
        z = division(x - y, y) + 1
    else:
        return 0
    return z

def nCr(n, r): 
    return (fact(n) / (fact(r) * fact(n - r))) 

def fact(n): 
    z = 1
    for i in range(2, n + 1): 
        z = z * i 
    return z 

def powerof2(n):
    if n >= 1:
        z = powerof2(n / 2) + 1
    else:
        return -1
    return z

def B(m, x):
    if x == 0:
        return 1
    elif m > x:
        z = math.factorial(m)/ (math.factorial(x) * math.factorial(m - x))
    else:
        z = B(m, x - 1) * [(m - x + 1) / x]
        
    return z