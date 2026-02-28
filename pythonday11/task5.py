m = int(input())
n = int(input())

star_1 = ("* " * n)
print(star_1)

for i in range(1,m-1):
    stars = "* "
    zeros = "0 "
    print(stars * (n - (n-1)) + zeros * (n-2) + stars * (n - (n-1)))
print(star_1)