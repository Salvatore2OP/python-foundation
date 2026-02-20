#Find the maximum element
n =int(input())
list_a =[]
for i in range(n):
    num = int(input())
    list_a += [num]
print(list_a)
for char in list_a:
    if char > list_a[0]:
        list_a[0]=char
print(list_a[0])