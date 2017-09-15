import math

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

def estimate_pi(error):
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    keep_going = True
    while keep_going == True:
        numerator = float(factorial(4*k) * (1103 + 26390 * k))
        denominator = float(factorial(k)**4) * 396**(4*k)
        term = factor * float(numerator/denominator)
        total += term
        k += 1
        if term < error:
            keep_going == False
            print("Iteration: ", k, " Error < ", error)
            break
    return 1 / total

for i in range(3, 1000):
    print(estimate_pi((10**(-1*i))))
