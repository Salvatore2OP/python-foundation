n = input()
length = len(n)
sum = 0
for i in n:
    power = (int(i) ** length)
    sum = sum + power

if sum == int(n):
    print("Armstrong")
else:
    print("Not an Armstrong")