#Sum of List Elements
n = input()
list_num = n.split()
sum = 0

for i in list_num:
    number = int(i)
    sum += number
print(sum)