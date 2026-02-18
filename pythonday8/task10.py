n = int(input())
list_a = []
for i in range(1,n+1):
    names = input()
    list_a += [names]
print(list_a[:3] + list_a[-3:])