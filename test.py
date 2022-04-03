from itertools import permutations
import sys
sys.stdin = open("input.txt", "rt")

n, k = int(input()), int(input())
nums = []
result = set()
for i in range(n):
    num = input()
    nums.append(num)
print(nums)
# for per in permutations(nums, k):
#     result.add(''.join(per))
    
# print(len(result))