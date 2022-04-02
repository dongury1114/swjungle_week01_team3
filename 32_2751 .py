# sol.1 - 반복문(while)
from math import factorial
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())

result = 1
i=1
while i <= n:
    result *= i
    i += 1
print(result)

# sol.2 - 반복문(for)
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
result = 1
if n> 0:
    for i in range(1,n+1):
        result *= i
print(result)

# sol.3 - 재귀함수

def factorial(n):
    result = 1
    if n > 0:
        result = n * factorial(n-1)
    return result

n = int(input())
print(factorial(n))