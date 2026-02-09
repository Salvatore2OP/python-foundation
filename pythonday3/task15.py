#Permission to attemp exam
percentage = input()
medical = input()
length = len(percentage)

percentage = int(percentage[:(length-1)])

if percentage >= 75 or medical == "Y":
    print("Allowed to write exam")
else:
    print("Not Allowed to write exams")