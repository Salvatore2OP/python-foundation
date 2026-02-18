L = ["5", "eat", "9.80", "Water", "python", "-678", "7685.26", "-2.5", "sing"]

# Write your code here
list_str = input()
is_Present = False

for i in L:
    if i == list_str:
        is_Present = True
        break
print(is_Present)