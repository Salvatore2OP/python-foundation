#program that stores a sequence of N numbers in a list and then, based on T test cases, prints the number at a specific index for each test case.
n = int(input())
t = int(input())

list_n = []
for i in range(1,n+1):
    num = int(input())
    list_n +=  [num]
for j in range(t):
    index = int(input())
    print(list_n[index])