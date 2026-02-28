n = int(input())
for i in range(1,n+1):
    space1 = n-i
    space2 = 2*i-3
    if i ==1:
        print(" "*space1 + "*")
    else:
        print(" "*space1 + "*" + " " * space2 + "*")
for j in range(n-1,0,-1):
    space1 = n-j
    space2 = 2*j-3
    if j ==1:
        print(" "*space1 + "*")
    else:
        print(" "*space1 + "*" + " " * space2 + "*")
