n = int(input())

for i in range(1,n):
    spaces = (n-i)
    stars = i
    row = (" ")*spaces + ("*")*stars
    print(row)
print(("#")*(n))