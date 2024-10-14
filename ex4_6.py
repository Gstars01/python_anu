#ex 
score = int(input(" input someones score : "))
if score <= 100 and score >=  90:
    grade = 'A'
elif score < 90 and score >= 80:
    grade = 'B'
elif score < 80 and score >= 70:
    grade = 'C'
elif score < 70 and score >= 60:
    grade = 'D'
elif score < 60 and score >= 50:
    grade = 'F'

print(f'ur grade : {grade}')