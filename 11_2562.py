# sol.1
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = 9
num = []
for _ in range(n):
    num += list(map(int,input().split()))

print(max(num))
print((num.index(max(num))+1))

#한줄로 펴서 만들고 인덱싱 하면 되지 않을까? 
# sol.2
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

num_list = []
for i in range(9):
    num_list.append(int(input()))
    
print(max(num_list))
print(num_list.index(max(num_list))+1)