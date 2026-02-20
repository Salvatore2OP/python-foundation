#Count Frequency
n =int(input("Enter number of items in List: "))
list_a = []

for i in range(n):
    num = int(input("Enter the list value: "))
    list_a += [num]
target = int(input("Enter Target value to check: "))
count = 0
for num in list_a:
    if num == target:
        count+=1
print(count)