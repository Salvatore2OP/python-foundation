#Divisible by 3
n = input()
list_a = n.split()
list_b = []

for char in list_a:
    number = int(char)
    if number % 3 == 0:
        list_b += [number]

print(list_b)