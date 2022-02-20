grade_list = input().split()
number_of_grades = len(grade_list)
grade_a = 0
for grade in grade_list:
    if grade == 'A':
        grade_a += 1
ratio_a = round(grade_a / number_of_grades, 2)
print(ratio_a)
