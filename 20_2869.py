# sol.1
import sys
import math
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

a, b, v= map(int,input().split())

n = ((v-b)/(a-b)) 
print(math.ceil((n)))

#파이썬 math 모듈
#math.ceil(): 올림하여 정수 반환
#math.floor(): 내림하여 정수 반환

#round(number, digit): number를 반올림하여 소숫점 digit 자리까지 보여준다