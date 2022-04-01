# sol.1
a, b= input().split()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)

# sol.2
a, b = map(int,input().split())
print(a+b, a-b, a*b, a//b, a%b, sep='\n')

#map

# sep: 구분자 -> ''