# sol.1
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
avg = 0
for _ in range(n): # n번 반복을 해서 각각 체점 
    score = list(map(int,input().split())) 
    avg=sum(score[1:])/score[0] #score[0] 학생수, score[1:] 학생들 각각의 점수
    count = 0
    for i in score[1:]:
        if i > avg:
            count += 1
    rate = count/score[0]*100
    print(f'{rate:.3f}%') #.3f : 셋째자리까지 표시(넷째자리에서 반올림 하여)
# sol.2

