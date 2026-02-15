#Patter following positive with negative
x = int(input())
n = int(input())

sum = 0

for i in range(1,n+1):
    if i % 2 == 0:
        sum = sum - (x ** (2*i))
    else:
        sum = sum + (x ** (2*i))

print(sum)
    