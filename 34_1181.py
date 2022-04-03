# sol.1
import sys
sys.stdin = open("input.txt", "rt")
# input = sys.stdin.readline

n = int(input())
res= []
abc= []
for _ in range(n):
    res.append(input())

res = list(set(res))
res.sort()
res.sort(key=len)
for i in res:
    print(i)
#문자열 길이대로 정렬 -> 다시 값으로 변환 -> For 문 돌라서 출력
#중복제외, 사전순(sorted랑 sort) 사용 법이 조금 다름
#길이순 .sort(key=len)
#set() 사용후 한번 더 list 써줘야함
#람다식: 함수를 형태를 좀더 짧게 사용하게 해준다 map()과 함께 자주 사용된다