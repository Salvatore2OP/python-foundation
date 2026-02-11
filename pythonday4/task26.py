x = int(input())
n = int(input())

counter = 1
sum_n = 0
product = 1
while counter <= n:
    sum_n = counter + x
    counter = counter+1
    product = sum_n * product
print(product)