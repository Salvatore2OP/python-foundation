s = input()

are_vowels = ""

for char in s:
    if((char == "a") or (char == "e") or (char == "i") or (char == "o") or (char == "u")):
        are_vowels = are_vowels + char   
print(are_vowels)