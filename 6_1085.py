# sol.1
x, y, w, h = map(int,input().split())

a = min(x, y, w-x, h-y)
print(a)


# print(min(x, y,w-x, h-y))