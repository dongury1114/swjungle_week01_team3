import sys
sys.stdin = open("input.txt", "rt")

N, r, c = map(int, input().split())
n = 4 ** N
ans = 0
for i in range(N):
    R = r//(2**(N-1))
    C = c//(2**(N-1))
    t = 2*R + C
    r -= 2**(N-1) * R
    c -= 2**(N-1) * C

    carry = 4 ** (N-1) * t
    n //= 4
    N -= 1
    ans += carry
print(ans)