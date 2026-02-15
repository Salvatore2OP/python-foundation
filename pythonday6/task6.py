n = int(input())
first_input = int(input())
greatest_number = first_input

for i in range(n-1):
    number = int(input())
    if number > greatest_number:
        greatest_number = number

print(greatest_number)