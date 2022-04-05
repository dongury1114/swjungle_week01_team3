import sys
sys.stdin = open("input.txt", "rt")

A, B  = map(int, input().split())

if str(A)[::-1] >str(B)[::-1]:
    print(str(A)[::-1])
else:
    print(str(B)[::-1])