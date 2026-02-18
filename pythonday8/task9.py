num_list = [1, 6, 32, 93, 71, -20, 30, -90, 50]

n = int(input())
list_a = []

for char in num_list:
    if int(char) > n:
        list_a += [char]
print(list_a)
if list_a == []:
    print("There is no bigger value.Try Again")
    