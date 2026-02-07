#Write a program that reads a string S and checks if the length of S is between 2 and 7 or the first character of S is not equal to "a"
s = input()
length = len(s)
if (length >= 2 and length <= 7) or s[0] != "a":
    print("Valid String")
else:
    print("Not Valid")