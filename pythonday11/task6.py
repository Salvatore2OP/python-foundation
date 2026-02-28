n = int(input())

for i in range(1,n+1):
    if i == 1 or i == 2 or i == n:
        print(". " * i)
    else:
        print(". " * (n-(n-1)) + "0 " * (i-2) + ". " * (n-(n-1)))