x = int(input())
n = int(input())

base = 1
sum = 0

for i in range(1,n+1):
    base = x ** (2*i)
    sum += base
print(sum)