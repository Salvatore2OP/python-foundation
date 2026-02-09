#Find The Group
num = int(input())

if num < 0 or num > 30:
    print("Invalid Credentials")
elif num % 6 == 1:
    print("Group 1")
elif num % 6 == 2:
    print("Group 2")
elif num % 6 == 3:
    print("Group 3")
elif num % 6 == 4:
    print("Group 4")
elif num % 6 == 5:
    print("Group 5")
else:
    print("Group 6")