#Find the second maximum element
n =int(input())
list_a =[]

for i in range(n):
    num = int(input())
    list_a += [num]
print(list_a) 
#largest element
largest = list_a[0]
for char in list_a:
    if char > largest:
        largest=char

#second largest
list_a.remove(largest)
second_largest = list_a[0]
for char in list_a:
    if char > second_largest:
        second_largest=char
print(second_largest)