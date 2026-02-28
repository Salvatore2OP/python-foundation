n = int(input())
print("* " * (2*n - 1))
for i in range(n-1,0,-1):
    stars = "* " 
    space_1 = n-i
    space_2 = 2*(n-i-1)
    print(space_1 *" " + (stars * i)+ " " * space_2 + i * stars)
    