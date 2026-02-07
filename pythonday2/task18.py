#Room Number without reading first letter "R"
a = input()

number = int(a[1:])
if number < 30:
    print("Ground Floor")
else:
    print("Not Ground Floor")