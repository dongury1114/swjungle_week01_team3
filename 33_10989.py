# sol.1 - 반복문(while)
from math import factorial
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
number =[]
for i in range(n):
    number.append(int(input()))
number.sort()
for i in number:
    print(i)


#-풀어보기-
#버블정렬

#삽입정렬

