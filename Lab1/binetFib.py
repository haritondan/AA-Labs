import time
start = time.time()

# Python3 program to find n'th
# fibonacci Number
import math


def fib(n):
    phi = (1 + math.sqrt(5)) / 2

    return round(pow(phi, n) / math.sqrt(5))


# Driver code
for n in range(1,1001):
    print(n ,":", fib(n))

# This code is contributed by prasun_parate

end = time.time()
print(end - start)
