#list of numbers that are divisible by 5 from a given set of N numbers. 
n = int(input())
list_a = []

for i in range(1,n+1):
    number = int(input())
    if number % 5 == 0:
        list_a += [number]
print(list_a)