# sol.1
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())

count = 0

for i in range (1, n+1):
        number = list(map(int,str(i)))
        # if n < 100:
        #     print(n)
        if i < 100:
            count += 1
            # print(n)
        elif number[0] - number[1] == number[1] - number[2]:
            count += 1
print(count)
# - 미완성 -
#sol.2
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

num = int(input())

hansu = 0
for i in range(1, num+1):
    num_list = list(map(int, str(i)))
    if i < 100:
        hansu += 1  # 100보다 작으면 모두 한수
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
        hansu += 1  # x의 각 자리가 등차수열이면 한수
print(hansu)

# 1자리수와 2자리수는 모두 한수이다 따라서 1 - 100; 99개 -> 예제 1번이 큰 힌트
# 1,2자리만 처리하는 부분 만들기
# 3자리 수의 경우 3개를 분리해서 각 숫자의 차이가 같은지 비교
# 숫자 -> 문자열 -> 리스트로 분리
# a = str(100)
# number = []

# for i in a:
#     number.append(i)
    
# print(number)