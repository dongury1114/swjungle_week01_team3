# sol.1
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
number = []
sum = 0

for i in range(9):
    number.append(int(input()))
    sum += number[i]


for i in range (9):
    for j in range (i+1, 9):
            if  100 == sum - (number[i] + number[j]):
                num1, num2 = number[i],number[j]
number.remove(num1)
number.remove(num2)
number.sort()
for i in number:
    print(i)
#9개에서 7개를 뽑아서 100을 만들어라
#9개를 다 더해서 2개를 빼서 100을 만들까?
#del 리스트[인덱스]: 인덱스에 해당하는 값을 삭제
#리스트.remove(값): 값을 제거
#total = sum(list)
