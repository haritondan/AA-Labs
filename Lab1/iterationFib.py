import time
start = time.time()

def fib(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

for n in range(1,1001):
    print(n ,":", fib(n))

end = time.time()
print(end - start)