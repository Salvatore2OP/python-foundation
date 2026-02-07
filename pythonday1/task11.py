#hard one
a = input()
b = input()
a_length= len(a)
b_length= len(b)
c = a_length-b_length
final_word= a[c:]
result = final_word == b
print(result)