n = int(input())

counter = 0
sum = 0

while counter < n:
    number = int(input())
    sum = sum + number
    counter +=1
    
avg = sum / n
print(avg)