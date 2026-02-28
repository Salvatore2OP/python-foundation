n = int(input())
stars1 = ("* " * n)
print(stars1)

for i in range(1,n -1):
    star = "* "
    zero = "0 "
    print(star * (n-(n-1)) + zero * (n -2) + star * (n-(n-1)))
print(stars1)