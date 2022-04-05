# sol.1
import sys
sys.stdin = open("input.txt", "rt")

n = int(input())

for _ in range(n): # n번 반복을 해서 각각 체점 
    OX_list = list(input())#ox 받기
    score = 0
    sum_score = 0
    for OX in OX_list:
        if OX == 'O':
            score += 1 #연속되는 o가 나오게 되었을때 1,2,3이 되도록 구현
            sum_score += score
        else:
            score = 0 #연속되지 않을때 점수를 더하지 않을 뿐더러 연속성이 되지 않도록 지점생성
    print(sum_score)
    
    
    # for 를 돌려서 o를 체크
    #n 개의 testcase를 받고 -> 점수를 매길 수 있는 로직을 짠다
    #연속성에 따라 1,2,3 .. 의 점수를 얻어 합계를 구해야한다.

# sol.2
