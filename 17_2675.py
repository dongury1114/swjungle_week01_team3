# sol.1
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
for i in range(n):
    num, s = input().split()
    answer=""
    for i in s:
        answer += int(num) * i
    print(answer)
# # sol.2
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
for i in range(n):
    num, s = input().split()
    answer=""
    for i in s:
        print( s*int(i),end="")