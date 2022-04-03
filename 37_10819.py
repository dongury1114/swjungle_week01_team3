# sol.1
from itertools import combinations
import sys
sys.stdin = open("input.txt", "rt")
# input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
sum= 0


for i in range(2,N+1):
    sum = abs(A[i-2]-A[i-1])
    print(sum)