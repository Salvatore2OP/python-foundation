def calculate_percentage(number):
    if number < 1000:
        value = (number * 0.05)
    else:
        value = (number * 0.1)
    return value
number = int(input())
result = calculate_percentage(number)
print(result)