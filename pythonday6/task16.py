n = int(input())

for i in range(n,0,-1):
    space = 2*(n-i)
    number = str(i) + " "
    print(" "*space + i*number)
    