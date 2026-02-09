distance = int(input("Enter you Distance: "))
score = 0
bonus = 50

if 0 < distance <= 40:
    score = distance * 2
elif distance <= 60:
    score = ((distance-40) * 4) + 40 * 2
elif distance <= 120:
    score = ((distance-60) * 6) + (40 * 2) + (20 * 4)
elif distance > 120:
    score = ((distance-120) * 8) + (60 * 6) + (40 * 2) + (20 * 4)

Total_Score = score + bonus
print("Total Score for covered distance(inc. bonus) :" ,Total_Score)