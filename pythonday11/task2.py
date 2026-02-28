n = int(input())
for i in range(1,n+1):
    spaces = n - i
    num_1 = (str(i)+" ") * i
    print(spaces * " " + num_1)
for i in range(n-1,0,-1):
    spaces = n-i
    num_2 = (str(i) + " ") * i
    print(spaces * " " + num_2)