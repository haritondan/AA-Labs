# Algorithm 4
# C[1] = false;
# i = 2;
# While (i<=n){
#   j=1;
#   while (j<i){
#     if ( i % j == 0)
#     {
#       c[i] = false
#     }
#     j=j+1;
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
        j = 2 # error ?
        while j < i:
            if i % j == 0:
                c[i] = False
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
