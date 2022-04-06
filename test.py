n = int(input())
def fac (m):
    if m == 1:
        return 1
    else:
        return m * fac(m-1)
print(fac(n))