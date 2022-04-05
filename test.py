import sys
sys.stdin = open("input.txt", "rt")
import math

def isPrime(num):
    sieve = [False, False] + (True * (n-1))
    primes = []
    for i in (2, n + 1):
        if sieve[i]:
            primes.append(i)
        for j in range(i * 2, n + 1, i):
            sieve[j] = False
    print(primes)

n = int(input())
numbers = list(map(int, input().split()))
count = 0 

for n in numbers:
    tmp = 0
    if n > 1:
        for i in range(2, int(n**0.5)):
            if n % i == 0:
                tmp += 1
        if tmp ==0:
            count += 1
print(count)