#Denomination-2 (4 Notes)
amount = int(input("Enter Amount: "))

rupee500 = int(amount / 500)
remaining_500 = amount % 500

rupee50 = int(remaining_500 / 50)
remaining_50 = remaining_500 % 50

rupee10 = int(remaining_50 / 10)
remaining_10 = remaining_50 % 10

rupee1 = int(remaining_10 / 1)

print("500:" + str(rupee500) + "   " + "50: " + str(rupee50) + "  " + "10:" + str(rupee10) + "  " + "1:" + str(rupee1))

