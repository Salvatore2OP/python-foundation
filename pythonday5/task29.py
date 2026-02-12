m = int(input())
n = int(input())

result = ""
for i in range(m,n+1):
    if i % 2 == 1:
        result = result + str(i) + " "
print(result)