import time
start = time.time()

def fib(n):
    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)

    return F[0][0]


def multiply(F, M):
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


def power(F, n):
    M = [[1, 1],
         [1, 0]]

    # n - 1 times multiply the
    # matrix to {{1,0},{0,1}}
    for i in range(2, n + 1):
        multiply(F, M)

for n in range(1,1001):
    print(n ,":", fib(n))

end = time.time()
print(end - start)