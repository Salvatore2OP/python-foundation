n = int(input())

for i in range(1 , n+1):
    space = (2*n-i)
    number = (2*i)-1
    row = (("  ")*space + ((str(i)+ " ")*number)  + (" ") * space)
    print(row)
    