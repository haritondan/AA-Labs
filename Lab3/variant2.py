# Algorithm 2
# C[1] =false;
# i=2;
# while (i<=n){
#   j=2*i;
#   while (j<=n){
#     c[j] =false;
#     j=j+i;
#   }
#   i=i+1;
# }
import time
start = time.time()
def sieve_of_eratosthenes(n):
    c = [True] * (n + 1)
    c[1] = False
    i = 2
    while i <= n:
        j = 2 * i
        while j <= n:
            c[j] = False
            j += i
        i += 1

    # Collect all prime numbers into a list
    primes = []
    for i in range(1, n+1):
        if c[i] == True:
            primes.append(i)

    return primes


# Example usage
n = 500
primes = sieve_of_eratosthenes(n)
print("All prime numbers up to", n, "are:", primes)
end = time.time()
print(end - start)