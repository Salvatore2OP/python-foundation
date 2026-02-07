a = input()
b = input()
i = int(input())
b_length = len(b)
c = i + b_length
part = a[i:c]
result = part == b
print(result)