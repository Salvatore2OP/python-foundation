n = int(input())

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
index = 0

for i in range(1, n + 1):
    for j in range(i):
        print(alphabets[index], end=" ")
        index += 1
    print()
