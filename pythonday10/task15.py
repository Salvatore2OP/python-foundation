def count_the_vowels(word):
    count = 0
    for char in word:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            count += 1
        else:
            continue
    print(count)
word = input()
count_the_vowels(word)
