n = int(input())

for i in range(1,n+1):
    space1 = 2*(n -i)
    space2 = 2*i-4
    if i == 1:
        print(" " * space1 + "* " )
    elif i == n:
        print("* " * n)
    else:
        print(" " * space1 + "* " + " " * space2 + "*")