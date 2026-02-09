#Leap Year Question
Year = int(input("Enter a Year: "))

divby400 = Year%400 == 0
divby4 = (Year%4 == 0) and (Year%100 != 0)

if divby400 or divby4:
    print("True")
else:
    print("False")