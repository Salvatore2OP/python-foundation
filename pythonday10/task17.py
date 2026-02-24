def count_of_uppercase(word):
    count = 0
    for char in word:
        if char == char.upper():
            count += 1
        else:
            continue
    return count
word = input()
result = count_of_uppercase(word)
print(result)