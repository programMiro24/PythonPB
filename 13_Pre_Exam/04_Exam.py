# •	На първия ред – броя на студентите явили се на изпит – цяло число в интервала [1...1000]
# •	За всеки един студент на отделен ред – оценката от изпита – реално число в интервала [2.00...6.00]
count_students = int(input())
grade = 0
students_with_fail_grades = 0
students_with_grades_between_3_and_4 = 0
students_with_grades_between_4_and_5 = 0
students_with_top_grade = 0
sum_grades = 0
result = ""

for _ in range(count_students):
    grade = float(input())
    if 2.00 <= grade <= 2.99:
        students_with_fail_grades += 1
    elif 3.00 <= grade <= 3.99:
        students_with_grades_between_3_and_4 += 1
    elif 4.00 <= grade <= 4.99:
        students_with_grades_between_4_and_5 += 1
    elif 5.00 <= grade <=  6.00:
        students_with_top_grade += 1
    sum_grades += grade

count_grades = count_students
result = f"Top students: {students_with_top_grade / count_students * 100:.2f}%\n"
result += f"Between 4.00 and 4.99: {students_with_grades_between_4_and_5 / count_students * 100:.2f}%\n"
result += f"Between 3.00 and 3.99: {students_with_grades_between_3_and_4 / count_students * 100:.2f}%\n"
result += f"Fail: {students_with_fail_grades / count_students * 100:.2f}%\n"
result += f"Average: {sum_grades / count_grades:.2f}"

print(result)
