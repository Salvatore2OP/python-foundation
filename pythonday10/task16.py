def count_the_vowels(word):
    # Complete this function
    count_of_vowels = 0
    vowels = ["a" , "e" , "i" , "o" ,"u"]
    for char in word:
        for i in vowels:
            if char == i:
                count_of_vowels += 1
            else:
                continue
    print(count_of_vowels)
word = input()
count_the_vowels(word)