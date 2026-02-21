def greet(word):
    msg = "how are you," + word + "?"
    return msg
greeting = ""
for i in range(2):
    name=input()    
    greeting += greet(word=name)
print(greeting)