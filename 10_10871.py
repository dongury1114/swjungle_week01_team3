# sol.1
# import sys
# sys.stdin = open("input.txt", "rt")
# input = sys.stdin.readline

# N, X = map(int,input().split())
# A = list(map(int,input().split()))

# for i in range(N):
#     if A[i] < X:
#         print(A[i], end=" ")

#x 보다 작은 수를 A 수열에서 반복문을 돌려 찾아낸다

#end = " " -> 이스케이프 문자를 지워줌

#sol.2
import sys
sys.stdin = open("input.txt", "rt")
n, x = map(int,input().split())
A = list(map(int,input().split()))

for i in range(n):
    if A[i] < x:
        print(A[i], end = " ")