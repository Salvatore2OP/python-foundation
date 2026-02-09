marks = int(input())

if marks < 50:
    print("No Discount")
elif 50 <= marks < 90:
    print("Discount is 100")
else:
    print(" Discount is 200")