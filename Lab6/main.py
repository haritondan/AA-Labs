import time
import matplotlib.pyplot as plt

# BBP formula
def bbp(n):
    pi = 0
    for k in range(n):
        pi += (1/16**k) * ((4/(8*k+1)) - (2/(8*k+4)) - (1/(8*k+5)) - (1/(8*k+6)))
    return int(pi * 16) % 16

# Spigot algorithm
def spigot(n):
    digits = [2]
    for i in range(1, n+1):
        carry = 0
        for j in reversed(range(len(digits))):
            num = 10 * digits[j] + carry
            digits[j] = num // (2*i - 1)
            carry = num % (2*i - 1)
        while carry > 0:
            digits.insert(0, carry % 10)
            carry //= 10
    return digits[-1]

# Chudnovsky algorithm
from math import factorial, sqrt
from decimal import Decimal, getcontext


def chudnovsky(n):
    getcontext().prec = n+1
    k = n // 14
    sum = Decimal(0)
    for i in range(k+1):
        num = (-1)**i * factorial(6*i) * (13591409 + 545140134*i)
        den = factorial(3*i) * factorial(i)**3 * 640320**(3*i)
        sum += Decimal(num) / Decimal(den)
    sum *= Decimal(12)
    x = Decimal(sqrt(10005)) * sum
    y = int(x * 10**n) // 10
    return y % 10


# Measure the time it takes to compute each digit of PI
n_values = list(range(1, 1001, 10))
times_bbp = []
times_spigot = []
times_chudnovsky = []

for n in n_values:
    start_time = time.time()
    bbp(n)
    times_bbp.append(time.time() - start_time)

    start_time = time.time()
    spigot(n)
    times_spigot.append(time.time() - start_time)

    start_time = time.time()
    chudnovsky(n)
    times_chudnovsky.append(time.time() - start_time)

# Plot the results
plt.plot(n_values, times_bbp, label='BBP formula')
plt.plot(n_values, times_spigot, label='Spigot algorithm')
plt.plot(n_values, times_chudnovsky, label='Chudnovsky algorithm')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time taken to compute digits of PI')
plt.legend()
plt.show()
