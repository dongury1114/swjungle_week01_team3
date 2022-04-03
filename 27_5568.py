# sol.1
from itertools import permutations
import sys
sys.stdin = open("input.txt", "rt")

# input = sys.stdin.readline

n, k= int(input()), int(input())
nums = []

for i in range(n):
    num = input()
    nums.append(num)
# print(nums)
result = set()
for i in permutations(nums, k):
    result.add(''.join(i))
print(len(result))

# print(int(str(a[0])+str(a[1]))) -> join 함수: 문자열 합치기 
#n장에서 k개를 선택해서 정수를 만든다
#예외처리 신경쓰기
#순열 조합
#조합으로 뽑은거를 합쳐서 숫자표현

#중복제거 방법
#numpy 패키지의 unique() 함수 활용
#set() : 집합자료형 변환 함수 -> 중복요소 제거
#''.join(리스트): 리스트에 있는 요소 하나하나를 합쳐서 문자열로 반환
#리스트 개행문자!!!! ㅅㅂ
# https://heytech.tistory.com/78
# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline