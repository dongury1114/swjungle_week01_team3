# sol.1
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

a, b= input().split()

r_a = int(str(a)[::-1])
r_b = int(str(b)[::-1])

if r_a > r_b:
    print(r_a)
else:
    print(r_b)

# sol.2
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

a, b= input().split()

r_a = int(str(a)[::-1])
r_b = int(str(b)[::-1])
print(r_a if r_a > r_b else r_b)
#리스트 -> [시작:끝:스탭]
#삼항연산자 [true_value] if [condition] else [false_value]