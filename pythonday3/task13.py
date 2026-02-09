#To get season
a = int(input("Number of Month(1 - 12): "))

if a == 11 or a == 12 or a == 1:
    print("Winter is Coming")
elif a == 2 or a == 3:
    print("Spring is Coming")
elif a == 4 or a == 5 or a == 6:
    print("Summer is Beginning")
elif a == 7 or a == 8:
    print("Rainy Season. Ah ha!!")
elif a == 9 or a == 10:
    print("Autumn Arrived")
else:
    print("You are a Fool. There are only 12 Seasons.")