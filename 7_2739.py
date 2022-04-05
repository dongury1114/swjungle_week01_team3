# # sol.1
a = int(input())
b = 0

while b < 10:
    b += 1
    c = a * b
    print(a, "*",b ,"=", c)

# sol.2
n = int(input())

for i in range(1, 10):
    print(n, "*", i, "=", n*i)
