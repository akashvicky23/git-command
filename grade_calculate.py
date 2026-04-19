from marks import marks

def marks_grade(marks_grade_avg):
    total = 0
    for sum_of_grade in marks_grade_avg.values():
        total += sum_of_grade
    grade = total/len(marks_grade_avg)
    print("Total Marks:",total)
    print(print(grade))
marks_grade(marks)
