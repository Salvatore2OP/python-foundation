#Alphabet printing
n_rows = int(input())
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(n_rows):
    for j in range(i+1):
        print((alphabets[j]), end = " ")
    print()