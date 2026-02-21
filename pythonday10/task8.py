def greet(word):
    msg = "hello " + word +" "
    return msg
greeting = ""
for i in range(2):
    name = input("Name: ")
    second_num = int(input("Number: "))
    second_num = str(second_num)
    greeting += greet(word=name)
    greeting += greet(word=second_num)
print(greeting)
