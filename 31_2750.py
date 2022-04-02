# sol.1 - 반복문(while)
from math import factorial
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
# number = list(input() for _ in range(n)) n 줄을 입력받아 리스트 만들기
Number = []
number = list(input() for _ in range(n))
print(number)

for i in number:
    Number.append(i.replace("\n",""))
print(Number)
Number.sort()
print(Number)
for i in range(len(Number)):
    Number[i]
print(Number)