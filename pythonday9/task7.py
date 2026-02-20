#Print sum of Even Number index in List
n =int(input("Enter number of items in List: "))
list_a = []

for i in range(n):
    num = int(input("Enter the list value: "))
    list_a += [num]
sum = 0
for num in list_a[0:n:2]:
    sum += num
print(sum)
