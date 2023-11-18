# As mentioned in the hints, you might want to use the math package
import math

# perform the Sieve of Eratosthenes algorithm and return all primes <= n
def sieve_of_eratosthenes(n):
    # You need to change the functionality of this function to
    # create a (sorted) list of all primes <= n which will then be returned.
    # Use the Sieve of Eratosthenes algorithm from the description.
    # You may change the following initialization of the list to be returned.

    primes_up_to_n = ['empty']

    if n > 1:

        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

        p = 2
        while p * p <= n:
            if is_prime[p]:
                # all multiples of p are not prime
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1

        primes_up_to_n = [i for i in range(2, n + 1) if is_prime[i]]

    # You don't need to change the following line.
    # It simply returns the list created above.
    return primes_up_to_n

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(sieve_of_eratosthenes(1000))