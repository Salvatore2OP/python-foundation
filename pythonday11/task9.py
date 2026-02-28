n = int(input())
print("_" * (n+1))

for i in range(n , 0 , -1):
    space = (i -1)
    print("|" * (1) + " " * space + "/" * (1) )
    