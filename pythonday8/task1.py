country_name =input("Enter Country: ").capitalize()
name = input("Enter your Name: ").title()
phone = str(input("Enter Your Phone No: "))
list_a = [country_name,name,"+91",phone]

if country_name == "India" and len(phone) == 10 and phone.isdigit():
    print(list_a)
    print("He/She is from :" ,list_a[0])
    print("His/Her name is : " ,list_a[1]) 
    print("He/She has phone number: +91",list_a[3])
else:
    print("Invalid Details")