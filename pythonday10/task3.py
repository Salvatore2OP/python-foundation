#Split Numbers
num = input()
list_num = num.split()
list_num2 = []
for i in list_num:
    number = int(i)
    list_num2+= [number]
print(list_num2)