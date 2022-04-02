# sol.1
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

y, x = list(map(int, input().split())) #가장큰 종이의 y는 세로 x는 가로
n = int(input()) #자르는 횟수

h =[0] #세로 잘리는 위치 저장
w =[0] #가로 잘리는 위치 저장

for _ in range(n):
    s, r = list(map(int,input().split())) # s = 가로 세로 판별 가로(w), 세로(h)의 위치
    if s == 0:
        h.append(r)
    else:
        w.append(r)

h.append(x)
w.append(y)
h.sort()
w.sort()

#제일 긴 h 구하기
maxH = 0
for i in range(1,len(h)):
    gap = h[i] - h[i-1]
    if gap > maxH:
        maxH = gap
#제일 긴 w 구하기

maxW = 0
for i in range(1, len(w)):
    gap = w[i] - w[i-1]
    if gap > maxW:
        maxW = gap

print(maxW * maxH)
#제일 긴 w와 제일긴 h를 뽑아내고 곱해서 제일 큰 넓이를 구한다


#문제가 안풀릴 때는 변수가 제 위치에 들어가고 동작하는지를 봐라

#이번문제에서 어려웠던 부분은 가로를 잘랐을때 세로의 위치 값이 나온다는 것

#문제 접근과 풀이에 도달하는 부분까지는 맞았다. 하지만 풀이를 구현하는 부분에 있어서 오랜 시간이 걸렸다. 문제를 해결할때 좀더 단위를 나누어 최종의 정답에 도달 할 수 있도록 해야겠다.