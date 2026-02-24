def calculate_bill(amount):
    if amount < 500:
        print(amount - (amount * 0.05))
    elif 500 <= amount < 2500:
        print(amount- (amount * 0.1))
    else:
        print(amount - (amount * 0.2))

amount = int(input())
# Call the calculate_bill function
calculate_bill(amount)
