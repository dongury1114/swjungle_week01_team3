# sol.1
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
numbers = map(int,input().split())

for num in numbers:
    error = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                error += 1
            if error == 0:
                s




# 소수 판별함수
# def is_prime_number(x):    # 2부터 (x - 1)까지의 모든 수를 확인하며
#     for i in range(2, x):        # x가 해당 수로 나누어떨어진다면
#         if x % i == 0:
#             return False # 소수가 아님
#     return True # 소수임


#여러 숫자를 받아서 Int로 변환할때는 map 사용하는거 기억하기!