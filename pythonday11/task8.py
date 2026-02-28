m = int(input())
n = int(input())

for i in range(1 , m+1):
    if i == 1 or i == m:
        print("* " * n)
    else:
        star = "* "
        space ="  "
        print(star * (n-(n-1)) + space * (n-2) + star * (n-(n-1)))