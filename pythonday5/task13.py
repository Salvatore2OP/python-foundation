#Identify the mistake - Styled World
n = input()

length = len(n)
b = n[0]
for i in range(1,length):
    b = b + "-" + n[i]
print(b)   