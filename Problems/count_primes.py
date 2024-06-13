# count the prime till a given number

def count_primes(num):
    for n in num:
        if n%n == 1 and n%1 == n:
            return sum(n)