#Check Palindrome List
n =int(input("Enter number of items in List: "))
list_a = []
for i in range(n):
    num = int(input("Enter the list value: "))
    list_a += [num]
if list_a == list_a[::-1]:
    print(True)
else:
    print(False)


