grades=[73,67,38,39]
print(grades)
for grade in grades:
    def rounding(val):
        actual_value = grade
        remainder_val = actual_value % 10
        if(remainder_val == (0 or 5)):
            rounded_value = actual_value
        elif(1 <= remainder_val < 5):
            rounded_value = (actual_value - remainder_val) + 5
        elif(5 < remainder_val <= 10):
            rounded_value = actual_value + (10 - remainder_val)
        return rounded_value
    round_val=rounding(grade)
    print(round_val)
    if (grade < 38):
        continue
    elif((round_val-grade) < 3):
        print(round_val - grade)
        grade1 =round_val
        grades.insert((grades.index(grade)),grade1)
        grades.remove(grade)
print(grades)