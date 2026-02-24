#Functions_Arguements
def greeting(arg_1,arg_2):
    print(arg_1 + " " + arg_2)

greet = input("Enter Greet Message: ")
name = input("Enter Your Name: ")

greeting(arg_1=greet,arg_2=name)
greeting(name,greet)