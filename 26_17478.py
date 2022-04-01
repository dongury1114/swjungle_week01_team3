# sol.1 - 반복문(while)
from math import factorial
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
for i in range (1, n):
    print(" 1  "*i ) 