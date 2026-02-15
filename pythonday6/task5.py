n = int(input())

fac = 0

for i in range (1,n):
    if (n % i) == 0:
        print(i)
        fac = fac + i

if fac == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")