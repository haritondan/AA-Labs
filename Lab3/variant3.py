# Alghorithm 3
# C[1] = false;
# i=2;
# while (i<=n){
#   if (c[i] == true){
#   j=i+1;
#   while (j<=n){
#     if (j % i == 0) {
#       c[j] = false;
#     }
#     j=j+1;
# }
# }
#   i=i+1;
# }
import time
start = time.time()
def sieve_of_eratosthenes(n):
    c = [True] * (n + 1)
    c[1] = False
    i = 2
    while i <= n:
        if c[i]:
            j = i + 1
            while j <= n:
                if j % i == 0:
                    c[j] = False
                j = j + 1
        i = i + 1

    # Collect all prime numbers into a list
    primes = []
    for i in range(1, n + 1):
        if c[i] == True:
            primes.append(i)

    return primes


# Example usage
n = 50000
primes = sieve_of_eratosthenes(n)
print("All prime numbers up to", n, "are:", primes)
end = time.time()
print(end - start)