# sol.1
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

a=int(input())
b=int(input())
c=int(input())

times = str(a*b*c)
answer = list(times)
for i in range(0,9):
    print(answer.count(str(i)))


# sol.2

