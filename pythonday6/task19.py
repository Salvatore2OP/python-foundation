#Shuffled string with index
s = input()
length = len(s)

shuffled = ""

for i in range(length):
    n = int(input())
    shuffled += s[n]
print(shuffled)