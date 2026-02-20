#Remove Duplicates
n =int(input("Enter number of items in List: "))
list_a = []

for i in range(n):
    num = int(input("Enter the list value: "))
    list_a += [num]
    
list_b = []
for num in list_a:
    if num not in list_b:
        list_b += [num]
print(list_b)