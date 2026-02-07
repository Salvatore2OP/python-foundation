a = int(input())
b = int(input())

if (a or b > 300) and (a + b < 500):
    print("Can Team Up")
else:
    print("No Team Up")