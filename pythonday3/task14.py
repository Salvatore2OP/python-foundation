temp = float(input())

if temp < 0:
    print("Freezing Weather")
elif 0 <= temp < 10:
    print("Very Cold Weather")
elif 10 <= temp < 20:
    print("Cold Weather")
elif 20 <= temp < 30:
    print("Normal")
elif 30 <= temp < 40:
    print("Hot")
else:
    print("Very Hot")