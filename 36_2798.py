# sol.1
from itertools import combinations
import sys
sys.stdin = open("input.txt", "rt")
# input = sys.stdin.readline

N, M = map(int,input().split())
card_list = list(map(int,input().split()))
big_num = 0
A = []
for i in combinations(card_list,3):
    tmp = sum(i)
    if tmp <= M:
        A.append(tmp)
print(max(A))
# sol.2
# from itertools import combinations
# import sys
# sys.stdin = open("input.txt", "rt")
# # input = sys.stdin.readline

# N, M = map(int,input().split())
# nums = list(map(int,input().split()))
# sum = 0 
# # result = set()
# tmp = []
# result = ()
# for i in combinations(nums,3):
#     tmp.append(i)

# print(tmp[1])
# print(len(tmp))

# for i in range(len(tmp)):
#     for j in range(3):
#         a = tmp[j]
#         sum += a[j]
#     print(sum)
# # print(sum)

# # result = set()
# # for i in permutations(nums, k):
# #     result.add(''.join(i))
# # print(len(result))
