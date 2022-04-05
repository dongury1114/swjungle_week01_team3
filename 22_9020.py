# sol.1

import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
number = []
part = []
n = int(input())
for i in range(n):
    number.append(int(input()))

for num in number:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                part.append(num)
        print(part)