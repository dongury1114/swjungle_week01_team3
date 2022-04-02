# sol.1
# import sys
# sys.stdin = open("input.txt", "rt")
# input = sys.stdin.readline

# n = int(input())
# numbers = list(map(int, input().split()))
# count =0


# sol.2
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
count =0

for num in numbers:
    tmp = 0
    if num >1:
        for i in range (2, num):
            if num % i == 0:
                tmp += 1
        if tmp == 0:
            count += 1
print(count)


# for num in numbers:
#     error = 0
#     if num >1:
#         for i in range (2, num):
#             if num % i == 0:
#                 error += 1
#         if error == 0:
#             count += 1
# print(count)

# sol.3
# import sys
# sys.stdin = open("input.txt", "rt")
# input = sys.stdin.readline

# def prime_number(numbers):
#     for i in (2,numbers):
#         if numbers % i == 0:
#             return False
#     return True

# n = int(input())
# numbers = map(int,input().split())
# count =0

# for _ in range(n):
#     if prime_number(numbers) == "True":
#         count += 1
# print(count)    

# 소수 판별함수
# def is_prime_number(x):    # 2부터 (x - 1)까지의 모든 수를 확인하며
#     for i in range(2, x):        # x가 해당 수로 나누어떨어진다면
#         if x % i == 0:
#             return False # 소수가 아님
#     return True # 소수임


#여러 숫자를 받아서 Int로 변환할때는 map 사용하는거 기억하기!

#map을 한것만으로는 쓸수 없다. 리스트로 만들어 리스트에서 뽑아오는 것을 로직을 사용해야한다 

#아리스토텔레스의 채
