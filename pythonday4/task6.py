n= int(input())
 
counter = 1
total = 0
while counter <= n:
    total = total + counter
    counter = counter + 1
avg = total / n
print(avg)    
