#Electric_bill (Hard)
units = int(input())
bill = 0

if units <= 50:
    bill = units * 2
elif units <= 150:
    bill = (((units-50) * 3) + 2 * 50)
elif units <= 250:
    bill = (((units-150) * 5) + (2 * 50) + (3 * 100))
elif units > 250:
    bill = (((units-250) * 8) + (50 * 2) + (100 * 3) + (100 * 5))

add_sur = bill * 0.2
total_bill = bill + add_sur

print("Your Total Bill(inc. 20% taxes) : " ,total_bill)