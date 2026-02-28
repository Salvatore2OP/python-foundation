n = int(input())

for i in range(1,n+1,1):
    space1 = 2*i - 2
    space2 = 2*(n-i-1)
    if i == 1:
        print("* " * n)
    elif i == n:
        print(space1 * " " + "* ")
    else:
        print(" " * space1 + "* " + " " * space2 + "* ")