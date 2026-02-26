def valid_string(string):
    length = len(string)
    if (string[0] == "s") or length >= 6 or string[0].isdigit():
        value = "Valid String"
    else:
        value = "Invalid String"
    return value
string = input()
result = valid_string(string)
print(result)