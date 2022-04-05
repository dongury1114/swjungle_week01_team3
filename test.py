import sys
sys.stdin = open("input.txt", "rt")
n = int(input())

for i in range(n):
    num, s = input().split()
    num = int(num)
    s = str(s)
    for i in range(len(s)):
        print(s[i] * num, end="")
    print()