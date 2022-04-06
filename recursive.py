# #피보나치 수열
# m = int(input())
# def sum (n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return sum(n-1) + sum(n-2)

# print(sum(m))
# #팩토리얼
# n = int(input())
# def fac (m):
#     if m == 1:
#         return 1
#     else:
#         return m * fac(m-1)

# print(fac(n))
#지수함수
# a, n = map(int,input().split())

# def pow(x, y):
#     if y == 0:
#         return 1
#     else:
#         return x * pow(x, y-1)

# print(pow(a, n))
#별찍기
# n = int(input())

# def star(x):
#     if x == 0:
#         return
#     else:
#         print('*' * x)
#         star(x-1)
#         return print('*' * x)
        
# star(n)

#2진수 변환
# n = int(input())
# def print_binary(n):
#     if n <2:
#         print(n, end="")
#     else:
#         print(n%2, end="")
#         print_binary(n//2)
# print_binary(n)

# 0 부터 n 까지의 합
# n = int(input())

# def sum(n):
#     if n == 0:
#         return 0
#     return n + sum(n-1)

# print(sum(n))

# 1 부터 N 까지의 곱
# n = int(input())
# def times(n):
#     if n == 1:
#         return 1
#     return n * times(n-1)
# print(times(n))

#최대공약수

def gcd(m, n):
    if m<n:
        m,n = n, m
    if m % n == 0:
        return n
    return gcd(n, m%n)

print(gcd(12, 8))