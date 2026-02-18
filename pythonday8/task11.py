#Reverse Order
n = int(input())
rev_str = []
for i in range(n):
    sports = input()
    rev_str += [sports]
for i in range(n):
    print(rev_str[n-i-1])

