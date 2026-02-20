#Reverse a string without slicing
n =int(input())
list_a = []
for i in range(n):
    num = int(input())
    list_a += [num]
list_a.reverse()
print(list_a)
