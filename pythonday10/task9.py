#Join Third Letter of Words
string_a = input()
string_b = string_a.split()
length = len(string_b)
final_string = []
for i in range(length):
    if len(string_b[i])>=3:
        final_string += string_b[i][2]
print(",".join(final_string))