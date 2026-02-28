n = int(input())

for i in range(1 , n+1):
    if i == 1 or i == n:
        print("* " * n)
    else:
        star = "* "
        space = "  "
        print(star * (n-(n-1)) + space * (n-2) +star * (n-(n-1)) )