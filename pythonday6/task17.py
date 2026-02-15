n = int(input())

for i in range(n,0,-1):
    spaces = 2*(n-i)
    stars = 2*i - 1
    rows = (" ")*spaces + ("* ")*stars + (" ")*spaces
    print(rows)
